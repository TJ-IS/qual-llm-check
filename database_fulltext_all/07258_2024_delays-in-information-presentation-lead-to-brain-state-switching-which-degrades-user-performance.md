---
otero_id: 7258
otero_key: "5EK37EAS"
title: "Delays in Information Presentation Lead to Brain State Switching, Which Degrades User Performance, and There May Not Be Much We Can Do about It"
authors: "Kevin A. Harmon; Hansol Lee; Bahar Javadi Khasraghi; Harshit S. Parmar; Eric A. Walden"
year: "2024"
journal: "MIS Quarterly"
doi: "10.25300/misq/2023/17680"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DELAYS IN INFORMATION PRESENTATION LEAD TO BRAINSTATE SWITCHING, WHICH DEGRADES USER PERFORMANCE,AND THERE MAY NOT BE MUCH WE CAN DO ABOUT ${ \mathsf { T } } ^ { 1 }$

Kevin A. Harmon Department of Information Systems, Sam M. Walton College of Business, University of Arkansas, Fayetteville, AR, U.S.A. {kharmon@walton.uark.edu}

Hansol Lee and Bahar Javadi Khasraghi Information Systems & Quantitative Sciences, Rawls College of Business, Texas Tech University, Lubbock, TX U.S.A. {hansol.lee@ttu.edu} {bahar.javadi@ttu.edu}

Harshit S. Parmar Texas Tech Neuroimaging Institute, Texas Tech University, Lubbock, TX, U.S.A. {harshit.parmar@ttu.edu}

Eric A. Walden Information Systems & Quantitative Sciences, Rawls College of Business, Texas Tech University, Lubbock, TX, U.S.A. {eric.walden@ttu.edu}

System delays are a major factor that harms user experience. Long delays often result in system abandonment, decreased user performance, and lost revenue for businesses. Although studies have provided important contributions on the consequences of delays, less is known about why system delays harm the user experience. Using fMRI, we examined how long system delays—compared to short delays— can change a user’s brain state. Results showed that brain state switching was more likely during a long delay than during a short delay. Brain state switching was also more likely at the beginning of a task following a long delay than following a short delay. The default-mode network (brain regions associated with inattention) was more active during long delays than when users were engaged in the task. Furthermore, long delays were significantly related to worsened performance as measured in decision time in the task following a delay. This effect was mediated by brain state switching at the beginning of the task after the delay. We also attempted four different system design interventions to overcome this and found partial mitigation, but none eliminated the negative effect of delays.

Keywords: Brain state switching, NeuroIS, fMRI, system delays, delays, interventions, user performance

## Introduction

A common cause of unsatisfactory user experience is system delays (Hong et al., 2013; Lee et al., 2017; Mital, 2014; Patel, 2020). User performance on information search tasks suffers when experiencing delays on travel websites (Selvidge et al., 2002), e-commerce websites (Galletta et al., 2004, 2006), or when learning complex material in educational settings (Davis & Hantula, 2001). Delays reduce the proportion of correct transactions, the overall number of transactions, and the job satisfaction of users (Barber & Lucas, 1983). Although numerous studies have highlighted various consequences of delays on user performance (Barber & Lucas, 1983; Butler, 1983; DiClemente & Hantula, 2003; Galletta et al., 2004, 2006), the underlying mechanisms for why delays are detrimental are still unclear.

Despite improvements in IT infrastructure and network speeds, system delays remain a significant problem (Dennis & Taylor, 2006; Galletta et al., 2006). To fully load a webpage, it takes an average of 10.3 seconds on a desktop computer and between 15 and 27.3 seconds on a mobile device (An, 2018; Dean, 2019). Thus, delays remain an important issue. The persistence of the problem of delays indicates the importance of continuing to gain a better understanding of how delays impact users.

An examination of the literature yielded two gaps that we address through this research. First, there is a dearth of research examining the mechanisms by which delays can harm user performance. In fact, most research on system delays focuses on user attitudes toward delays or systems with delays rather than how and why performance can be harmed. Understanding why this phenomenon occurs is important so that we can better assess whether interventions can be designed to limit the impact of delays on performance. Second, research on interventions for delays has focused on user perceptions of wait time (Hong et al., 2013; Lee et al., 2012; Lee et al., 2017) but there has been no research on interventions to reduce the impact of delays on performance.

To address the first gap, we take a neuro-information systems (NeuroIS) approach to study system delays and explain a mechanism by which delays impact the user. Based on neurological evidence for different brain states and the default-mode network—a set of brain regions that tend to become active when we are not engaged in any task—in particular, we propose that an idle brain does not remain idle long. Rather, it switches from its task state. Thus, long system delays result in brain state switching from the task state into some other state, which means that the brain must switch back into the task state before continuing the task. Not only can this degrade performance, it is also metabolically costly to switch to and from the task state, potentially leading to fatigue and ego depletion. Using functional magnetic resonance imaging (fMRI) data we show that (1) brain state switching does occur because of long delays, (2) tasks are performed more slowly after long delays, (3) observable brain state switching predicts slower task performance, and (4) performing tasks become more metabolically costly after long delays.

To address the second gap, in a behavioral experiment, we then tested four possible system design interventions to overcome the effects of delays. Two of the design interventions partially mitigated but did not eliminate the effect, which is consistent with the problem of brain state switching. In addition, the behavioral study shows that overall users are less accurate, slower, less interested, and more bored when faced with delays, even if there is some sort of intervention.

## Study 1

## Theory

## Constructs

Delays can occur when users perform a series of tasks with an information system. As users perform a series of tasks, they provide some input into the system and wait for a system response. The system provides requested information to the user, who can then proceed with completing tasks. System delays can occur throughout this process between the instant in which a user requests information from the system and when the system supplies this information. Some amount of delay—even if it is brief—is always present between a user request and a system response. Despite numerous rules of thumb for tolerable delay times, there seems to be a consensus that delays of 2 seconds or fewer are considered acceptable (Dennis & Taylor, 2006; Galletta et al., 2004; Nah, 2004). Thus, we define short delays as delays lasting 2 seconds or less. Conversely, the literature suggests that delays of 8 seconds or more are consistently problematic (Galletta et al., 2004, 2006). Thus, we define long delays as delays lasting 8 seconds or more.

The next construct we consider is brain state switching. A brain state is a reliable pattern of interconnected activations between brain regions that correspond to a behavioral task (Lee & Dan, 2012; Tang et al., 2012). A brain state will change when a person’s behavioral task changes. Thus, brain state switching is a change in the global pattern of activity in many brain areas following a change in a behavioral task (Lee & Dan, 2012). This brain state switching can be observed using fMRI. Brain state switching occurs when the set of brain areas activated—as assessed using fMRI—changes.

Our last construct is performance. An important way that information systems improve performance is by helping managers and consumers make fast and efficient decisions (Leidner & Elam, 1993, 1995; Xiao & Benbasat, 2007). Thus, in this case, we defined performance as the amount of time in seconds it takes to make a decision after presenting the stimulus needed to make the decision.

## Model Specification

In Figure 1, we present a conceptual model of how we expect short and long delays to create the brain state switching process when users are engaged in a series of tasks. The idea is that while an information system displays task-relevant information, the user is in a task-appropriate brain state to make use of that information to perform the task.

![](/api/attachments/5EK37EAS/fulltext/images/820fab440913d441cd7fdab1782f859b65f9a5ac6246c8747f749d12e92c5211.jpg)  
Figure 1. Conceptual Model of Delays and Brain State Switching

A user can maintain this task-appropriate state for a short period of time after the task is complete and the current system information is no longer being used to perform the task. If the same task is given after a short delay, then the user is in the appropriate state to make use of the information presented for the second task. On the other hand, if the delay is too long then the user will switch out of the taskappropriate state into some other state. They will then need to switch back into the task-appropriate state when the system begins displaying new task-relevant information. Notice that the task-appropriate state maintains for some time after the delay starts and the task-relevant brain state takes some time to obtain after the delay ends.

This is roughly analogous to an athlete warming up for a sport. Before performing an athletic task, an athlete will try to get the blood flowing to the appropriate areas of their body for optimal response during the athletic task. However, if an athlete waits too long, they will cool down and the blood will flow instead to other body regions that need it. Indeed, in fMRI we are measuring oxygenated blood flow; thus, our paradigm is very similar to athletic performance. With fMRI, we can see which areas of the brain are performing work/expending energy.

In addition, our research model can be seen in Figure 2. Given that we can measure brain state switching, the research model proposes that a long delay will be more likely to induce brain state switching than a short delay. Brain state switching will in turn reduce task performance by increasing decision time, as the brain must switch brain states by rerouting blood flow when the task-relevant information is presented.

## Hypotheses<sup>2</sup>

## Brain State Switching

Studies using fMRI (Wig et al., 2005), positron emission tomography (Squire et al., 1992), EEG (Gruber & Müller, 2002), or single-cell recordings (Li et al., 1993) show that performing a task primes neurons to continue performing the same type of task. A primed brain can perform the primed task more quickly and efficiently. If information about this task is presented with only a short delay, the brain maintains the state and continues to process information quickly and efficiently. In this state, we would expect to see consistent and effective performance.

![](/api/attachments/5EK37EAS/fulltext/images/113a9962c4cf5cb31702fc1bb011ed60769a3945c85a763ecb9ad04aa837fd5c.jpg)  
Figure 2. Research Model

However, the brain does not stay in a primed state indefinitely. A long delay creates a task-negative environment—one in which no external stimuli are available for engagement. This should create a distinct brain state that will require a different representation in the brain. When the system finally delivers the user’s requested information, the brain must switch back to the task-appropriate state to engage with the user’s tasks.

There are two places in which this phenomenon of brain state switching can occur. First, brain state switching can occur during a long delay. Second, brain state switching can occur at the beginning of the task following a delay. After the delay has ended, users must reorient their attention to their task, which will change their brain state from that present during the task-negative delay period. We expect that a long delay increases the chance of both of these types of brain state switching to occur. Thus, we hypothesize:

H1a: A long delay increases the likelihood of brain state switching during the delay.

H1b: A long delay increases the likelihood of brain state switching during the task following the delay.

The default-mode network (medial prefrontal cortex, posterior cingulate cortex, and angular gyrus) (Raichle et al., 2001; Sridharan et al., 2008; Tang et al., 2012) often becomes active when attention turns inward away from the external environment (Weissman et al., 2006). When there is an active task in the environment, the default-mode network is deactivated and the appropriate networks (e.g., attention, salience, etc.) for the task become engaged (Sridharan et al., 2008; Weissman et al., 2006). When there is no task present in the environment, these other networks tend to be deactivated and the default-mode network is activated and remains active until another task emerges (Sridharan et al., 2008; Weissman et al., 2006).

Long delays create a task-negative environment. Research suggests that the default-mode network becomes active at least after 5.5 seconds in a task-negative environment (Hugdahl et al., 2019). Thus, a long delay (\~10 seconds in this study) would be of sufficient length to lead to default-mode network activity. During a long delay, the user’s primary task becomes unavailable, and they are left with nothing in which to engage. Because of this, we expect the default-mode network to become active during long delays. Thus, we hypothesize:

H2a: A long delay results in the activation of the default-mode network (which includes the medial prefrontal cortex, posterior cingulate cortex, precuneus, and angular gyrus) during the delay.

H2b: A long delay results in the activation of the default-mode network (which includes the medial prefrontal cortex, posterior cingulate cortex, precuneus, and angular gyrus) in the task following the delay.

## Long Delays, Brain State Switching, and Decision Time

We propose that brain state switching is a mechanism through which long delays slow down decision-making. Long delays interrupt the user’s primary task. Once the delay is over, the user must reengage with the primary task. The phenomenon of brain state switching may account for the extra steps that are involved in the brain for a task following a long delay compared to a task following a short delay. As hypothesized above, during a long delay we would expect to see brain state switching between the task-appropriate state and the default-mode network. Activation of the default-mode network in between the performance of similar tasks can result in slowed response times (Weissman et al., 2006). For a task following a short delay (in which there is little change in the task environment), the brain remains primed for the same type of task (Allport & Wylie, 1999; Monsell, 2003). We would then expect that the brain state will not switch, and each similar task should take about the same amount of time. Conversely, during a long delay, if brain state switching occurs, there are more steps involved in the process of completing the next task at a neurological level. If the brain state switches during a long delay, the brain’s neurons are no longer “warmed up” or primed for the task that will follow the delay. It will take time and effort to reengage the brain state needed for the task once the delay ends. Similarly, if the brain state switches at the beginning of the task following the delay, this represents time and effort being spent on something other than the task. Competition from the default-mode network may slow the brain in reactivating the brain state needed to perform the primary tasks (Sridharan et al., 2008; Weissman et al., 2006). It takes time to deactivate the default-mode network and reactivate the task-appropriate state. Therefore, we would expect brain state switching during the delay or during the task following the delay to require time, resulting in the subsequent decision-making task taking longer. As typical in mediation research, we hypothesize the direct a, b, and c paths as well as the expected indirect effects, allowing us to assess the presence of a c path effect that is mediated through a and b. Thus, we hypothesize:

H3: A long delay results in increased decision time in the task following the delay.

H4a: Brain state switching during a delay increases the decision time in the task following the delay.

H4b: Brain state switching during the task following a delay increases the decision time in the task following the delay.

H5a: Brain state switching during a delay mediates the effect of a long delay on the decision time in the task following the delay.

H5b: Brain state switching during the task following a delay mediates the effect of a long delay on the decision time in the task following the delay.

## Method

## Participants

The participants were 24 students (17 White, 2 Asian, 1 Native Hawaiian, 1 Black/African American, and three responded “Other”)<sup>3</sup> from a business school in the southwestern United States. The average age of participants was 20.71 years (Min = 19, Max = 33). There were 16 male participants. Among male participants, 12 were right-handed dominant. Among the eight female participants, six were right-handed dominant<sup>4</sup>. Because of the rapid time series nature of fMRI data, the total number of observations was 3,466,345,784, across 1894 judgment tasks with 1870 delays. As compensation, the participants earned course credit.

## Procedure

Before the experiment, participants signed a written consent form and an MRI safety screening form. Then, participants completed a practice stimulus to familiarize them with the experimental task before they entered the MRI scanner. The practice stimulus looked identical to the experimental stimulus, but it included different apps and the length of delay did not vary between trials (there was a consistent 4-second delay between trials in the demo). During the experiment, delays were either 0-2 seconds or 10-20 seconds uniformly distributed so that (1) participants never received an experimental trial with the same delay as the practice, (2) the experimental trials did not show any consistent pattern, and (3) due to the random order of presentation, roughly half the participants first saw a shorter and roughly half first saw a longer delay than in practice. Thus, we attempt to control for any effects of expectations. Participants were able to engage in practice trials on a laptop before entering the scanner and ask questions to make sure they understood the task. Once they understood the task, they entered the scanner.

After they entered the scanner, participants underwent a structural scan of their brain.<sup>5</sup> Then, they started the experimental task during which functional scans were recorded. The participants completed the experiment at their own pace and were allowed to take as long as they liked to evaluate each app. However, the scanner was limited to recording 4096 (2<sup>12</sup>) full brain volumes in a single experiment. Therefore, the entire experiment was limited to just over 37 minutes, and one participant did not complete all 80 trials in that amount of time; this participant completed 54 trials and is included in the analysis. When the experiment was over, participants were asked to complete a post-experimental survey. After the survey was complete, we thanked the participants and they were dismissed.

## Task

For the experimental task, we gathered pictures and descriptions of 80 apps from the Google Play Store used on Android devices. Text descriptions were matched for length (270-280 words and 17-18 seconds when converted to speech) so that each app had approximately the same length description.

For each trial, participants were presented with an app picture and description. The apps were presented to each participant in random order. For each picture and description, participants rated either their expected satisfaction (“How satisfied do you think you would be with this app?”) or dissatisfaction (“How dissatisfied do you think you would be with this app?”) for the app on a scale from 1 (not at all) to 4 (extremely). Whether they were asked about expected satisfaction or dissatisfaction for each app varied randomly with a probability of 50% for each question on each app. Example stimuli can be found at the Open Science Framework (OSF) site for this study.<sup>6</sup> Participants made this rating with a button box in the scanner. After making their rating, participants continued viewing the same app screen except the word “Loading…” was added to the bottom to indicate the next app was loading. This was the delay, which varied between short and long duration randomly, with each having a 50% probability for each trial.

Delays were implemented by varying the length of time in which the loading screen was viewed. For long delay trials, this screen stayed on for a uniform random value between 10 and 20 seconds before the next app appeared. Since a long delay was defined as more than 8 seconds (Galletta, 2004), we used a lower bound of 10 seconds to ensure that the delay was long enough. We used an upper bound of 20 seconds to prevent participants from being able to anticipate the length of the delay while keeping the experiment manageable. For short delay trials, this screen stayed on for a uniform random value less than 2 seconds before the next app appeared. Both short and long delay screens looked identical with the only difference being the length of the delay. We considered long delay trials to be apps that were preceded by a 10-20-second loading screen, whereas short delay trials were preceded by a less than 2-second loading screen. Note that in each case, the loading screen was the exact same screen with the word “Loading…” presented in small letters toward the bottom of the screen so as to not disrupt the input to the visual cortex by changing the visual display.

## Analysis

## Preprocessing

Data for all participants went through the same preprocessing pipeline: motion correction, co-registration, normalization, segmentation, brain masking, temporal signal drift reduction, temporal smoothing, and spatial smoothing. Preprocessing details can be found on the OSF site.<sup>7</sup>

## Brain State Switching Analyses

To detect brain state switches, we used t-distributed stochastic neighbor embedding (t-SNE), to reduce the data from high dimensional space to a single similarity dimension. Commonly used dimensionality reduction techniques include principal components analysis (PCA), linear discriminant analysis (LDA), multidimensional scaling (MDS), and t-SNE. Each technique has its advantages and disadvantages. The main advantage of t-SNE for fMRI is the ability to preserve neighborhood information while reducing dimensionality. That is, whereas traditional data reduction techniques focus on keeping distant points far apart, t-SNE strives to keep near points close together. In other words, feature points that are near one another in the original dimensionality space remain close to one another in the visualization. This allows for better detection of brain state switches (Parmar et al., 2021; Parmar et al., 2020).

Brain state switches were indirectly measured, independently for each participant, by computing the t-SNE distance between temporally adjacent fMRI brain volumes. The t-SNE distance between all adjacent time points can be represented in the form of a single time series known as the step distance plot. The time instances of the brain state switches can be detected from the step distance plot by identifying time points with significantly large step distances.

From this step distance plot, instances of brain state switches are identified by thresholding the step distance plot. The step distance plot is first sorted and the mean and standard deviation is then computed for the first 95 percentiles. This step gave us the mean and standard deviation of the noise floor in the step distance plot. The threshold was set to a value of mean + (10 x standard deviation). Any step distance higher than the threshold represents a significantly large step distance and indirectly indicates the temporal instance of the brain state switching. Time instances of all the step distances higher than the threshold were saved as an indication of a significant brain state switching. Additional description of the t-SNE process is provided in Appendix A.

## Results

## Brain State Switches

During delays, one (41.3 %) or more (6.6 %) brain state switches were detected in 47.9% of the long delays and only in 5.1% of the short delays, X<sup>2</sup>(1) = 436.84, p < 0.001. Overall, we saw a greater propensity for brain state switches during long delays than during short delays, providing support for H1a.

During the task immediately following a long delay there were one or more brain state switches 47.4% of the time. During the task immediately following a short delay, there were one or more brain state switches only 31.4% of the time X<sup>2</sup>(1) = 49.05, p < 0.001. Overall, we found support for H1b—that the likelihood of a brain state switching during the stimulus after a long delay is greater than that after a short delay.

## Imaging Results

For all imaging results, we conducted general linear model analyses, specific model details are included on the project’s OSF site<sup>8</sup> using FMRIB Software Library (FSL) (Jenkinson et al., 2012). To test H2a and H2b—that a long delay results in the activation of the default-mode network during the delay and in the task following the delay—we examined two contrasts. First, we compared the activation before the detected brain state switch to that after the switch during the long delay in trials with measured switches. In principle, if the default-mode network is activated during the long delay and then deactivated during the task, we would expect to see it in the contrast. However, we may fail to see it if the default-mode network takes too long to switch on relative to the delay or if default-mode network regions are also important for the task. Thus, we examined a second contrast comparing the activation in the first half of the task following a long delay vs. the activation in the first half of the task following a short delay. While the brain state may switch very quickly, fMRI measures the magnetic properties of oxygenated blood, which takes around six seconds to peak (Dimoka, 2012). Thus, if the default-mode network was activated the instant before the task started, we would expect to be able to observe some activation in that region for a short time.

The results of the first contrast are displayed in Figure 3 and Table 1. In refutation of H2a, we did not find evidence for the activation of the default-mode network in this contrast. However, we did find other significant areas of activation. Thus, it is possible that brain state switches induced by delays may result in the activation of different brain areas than the default-mode network.

Figure 4 and Table 2 show the results of the second contrast of greater brain activation during the first half of the app screen following a long delay (versus a short delay). These results show greater activation in the default-mode network and the dorsal attention network as well as the visual cortex after a long delay. The opposite contrast for areas of greater activation following a short delay during the first half of the task showed no significant activations. This is consistent with a participant starting in the default-mode network, and then having to switch attention—especially visual attention back to the task after a long delay but not after a short delay. Thus, this provides support for H2b.

For completeness, we also examined the differences in brain activation for the second half of the task (see Figure 5 and Table 3). There was still greater activation during the second half of the task after a long delay, though it was not nearly so dramatic. There were no regions of greater activation in the second half of the task following a short delay. This suggests that most of the difference appears in the first half of the task.

The results provide partial support for the idea that the defaultmode network is the brain state that is activated in response to a long delay. The results are consistent with the idea that it might take some time for the default-mode network to activate and then some additional time for it to deactivate.

## Behavioral Results: Descriptive Statistics by condition Are Displayed in Table 4.

We used regression models with random intercepts using restricted maximum likelihood (REML) estimation to account for the non-independence of app ratings made by the same participant. In other words, app rating responses were nested within participants. Using random intercept models increased trust in our parameter estimates for explanatory variables. We used the lme4 package (Bates et al., 2015) in R for these analyses. The significance of explanatory variables was determined with t-tests and degrees of freedom using the Satterthwaite method. Note that this method allows for partial degrees of freedom.

![](/api/attachments/5EK37EAS/fulltext/images/1c961dfa111072b7fe4706fe6bff682ebb2dec0b50c6c55cd6a371f3175dbb99.jpg)  
MNI Z = -12, 8, 28, 48; Heatmap Z Score 3.1  
6 ; Left is on the right

Figure 3. Areas of Greater Activation before the Detected Brain State Switch (versus after the Switch during the Long Delay in Trials with Measured Switches. Reverse Contrast (After Switch > Before Switch) on the Bottom

Table 1a. Before Switch > After Switch

<table><tr><td># of voxels</td><td>P-value cluster</td><td>Largest z-score</td><td>MNI152 coordinates of largest z</td><td>Region</td></tr><tr><td>7436</td><td>&lt;0.001</td><td>5.60</td><td>10, -72, -12</td><td>Visual cortex</td></tr><tr><td>954</td><td>5.13E-17</td><td>4.74</td><td>-14, -6, 24</td><td>Caudate</td></tr><tr><td>892</td><td>3.15E-16</td><td>4.70</td><td>34, 62, -14</td><td>Anterior prefrontal cortex</td></tr><tr><td>109</td><td>0.003</td><td>4.14</td><td>-52, 38, -10</td><td>Inferior frontal gyrus</td></tr><tr><td>106</td><td>0.003</td><td>4.61</td><td>-2, -20, 76</td><td>Supplementary motor cortex</td></tr><tr><td>104</td><td>0.004</td><td>4.45</td><td>-4, 40, 56</td><td>Superior frontal gyrus</td></tr><tr><td>98</td><td>0.006</td><td>4.28</td><td>-4, 22, 68</td><td>Premotor cortex</td></tr><tr><td>68</td><td>0.039</td><td>4.45</td><td>0, -20, 16</td><td>Thalamus</td></tr></table>

Table 1b. After Switch > Before Switch

<table><tr><td># of voxels</td><td>P-value cluster</td><td>Largest z-score</td><td>MNI152 coordinates of largest z</td><td>Region</td></tr><tr><td>520</td><td>4.95E-11</td><td>4.92</td><td>-40, -30, 62</td><td>Somatosensory cortex</td></tr><tr><td>395</td><td>5.07E-09</td><td>4.45</td><td>-50, -20, 20</td><td>Secondary somatosensory cortex</td></tr><tr><td>195</td><td>2.85E-05</td><td>4.22</td><td>-4, -4, 56</td><td>Premotor cortex</td></tr><tr><td>143</td><td>0.000418</td><td>4.2</td><td>-40, -2, 12</td><td>Insular cortex</td></tr><tr><td>139</td><td>0.00052</td><td>4.23</td><td>-58, 8, 28</td><td>Premotor cortex</td></tr><tr><td>72</td><td>0.03</td><td>4.15</td><td>-36, -38, 44</td><td>Intraparietal sulcus</td></tr></table>

![](/api/attachments/5EK37EAS/fulltext/images/12933b65215fa2f0ecbf4b7c35f67e3c70360007a961a72ca184fea51cd4e5b2.jpg)  
MNI Z = -12, 8, 28, 48; Heatmap Z Score 3.1 6 ; Left is on the right

Figure 4. Areas of Greater Activation during First Half of the App Screen Following a Long Delay (versus a Short Delay)

Table 2. Details of Clusters in Which the First Half of the App Screen Following a Long Delay Showed Greater Activation than the First Half of the App Screen Following a Short Delay

<table><tr><td># of voxels</td><td>P-value cluster</td><td>Largest z-score</td><td>MNI152 coordinates of largest z</td><td>Region</td></tr><tr><td>45235</td><td>&lt;0.001</td><td>5.79</td><td>-28, -78, 18</td><td>Superior parietal lobe</td></tr><tr><td>428</td><td>3.98E-05</td><td>4.25</td><td>30, 20, 10</td><td>Anterior insula</td></tr><tr><td>248</td><td>.002</td><td>4.31</td><td>46, -38, 4</td><td>Superior temporal sulcus</td></tr><tr><td>201</td><td>.007</td><td>4.16</td><td>0, -48, -32</td><td>Cerebellum</td></tr><tr><td>183</td><td>.011</td><td>4.32</td><td>56, 18, -2</td><td>Inferior frontal cortex</td></tr><tr><td>140</td><td>.038</td><td>3.98</td><td>-42, -12, -24</td><td>Anterior temporal lobe</td></tr></table>

![](/api/attachments/5EK37EAS/fulltext/images/16786db9a5ebab65673afdb34de4749014fc018f7342bf7343a367bfe1dc7a83.jpg)  
MNI Z = -12, 8, 28, 48; Heatmap Z Score 3.1 6 ; Left is on the right

Figure 5. Areas of Greater Activation During Second Half of the App Screen Following a Long Delay (versus a Short Delay)

Table 3. Details of Clusters in Which the Second Half of the App Screen Following a Long Delay Showed Greater Activation than the Second Half of the App Screen Following a Short Delay

<table><tr><td># of voxels</td><td>P-value cluster</td><td>Largest z-score</td><td>MNI152 coordinates of largest z</td><td>Region</td></tr><tr><td>1246</td><td>1.74E-11</td><td>4.7</td><td>12, -74, 8</td><td>Lingual gyrus</td></tr><tr><td>403</td><td>4.26E-05</td><td>4.15</td><td>-62, -40, 6</td><td>Superior temporal sulcus</td></tr><tr><td>240</td><td>.002</td><td>4.05</td><td>-38, -24, 62</td><td>Motor cortex</td></tr><tr><td>158</td><td>.019</td><td>4.06</td><td>-52, -4, 44</td><td>Premotor cortex</td></tr></table>

<table><tr><td colspan="3">Table 4. Means and Standard Deviations by Condition</td></tr><tr><td>Variable</td><td>Short delay</td><td>Long delay</td></tr><tr><td>Delay duration</td><td>0.99(0.57)</td><td>14.79 (2.90)</td></tr><tr><td>Decision time</td><td>11.95(6.51)</td><td>13.17(6.74)</td></tr><tr><td>Brain state switching (during delay)</td><td>0.05(0.22)</td><td>0.48(0.5)</td></tr><tr><td>Brain state switching (during task following delay)</td><td>0.31(0.46)</td><td>0.47(0.5)</td></tr></table>

We first tested H3—that a long delay results in an increased decision time in the task following the delay (see Table 5). We found support for this hypothesis, b = 1.17, t(1844.90) = 5.44, p < 0.001. Thus, there was a significant difference in decision time in a task following a long delay compared to a short delay. Specifically, we observed that it took an average of 1.17 seconds longer to make a decision following a long delay compared to a short delay. As a robustness check, we also ran a model with delay duration as the explanatory variable for response time. Similarly, we found a significant effect for delay duration, b = 0.07, t(1845) = 4.99, p < 0.001. This provides further support that longer delays result in increased decision times.

Next, we conducted several analyses that included brain state switching as an observed variable. For each observation, a dummy-coded variable (1 = brain state switching, 0 = no brain state switching) was created for the delay period and for the task following the delay. By using these variables, we were able to test our hypotheses that brain state switching during delays and during the task following delays both lead to increased decision time in the task following the delay and mediate the effect of long delays on decision time. See Table 5 for the results of these analyses.

First, we tested H4a—that brain state switching during a delay is associated with increased decision time in the task following the delay. This hypothesis was supported, b = 0.83 t(1845.63) = 3.32, p < 0.001. This result suggests that decision time—on average—was 0.83 seconds longer in a task following brain state switching during the delay. We then tested H4b—that brain state switching during the task following a delay is associated with increased decision time in the task following the delay. This hypothesis was supported, b = 2.39 t(1847.51) = 10.64, p < 0.001. This result suggests that decision time— on average—was 2.39 seconds longer when brain state switching occurred during the task following the delay.

To examine mediation, H5a and H5b, we used the “mediation” package (Tingley et al., 2014) in R. This package uses a general approach to mediation that accommodates binary mediators and random effects models (Imai et al., 2010; Tingley et al., 2014). This approach uses a quasi-Bayesian approach in which parameters’ posterior distributions are approximated using their sampling distributions (Imai et al., 2010). We used 5,000 simulations— well above the recommended minimum of 1,000 (Imai et al., 2010). Results of the mediation analyses can be seen in Table

6. Here we see in Model 1 that brain state switching during the delay does not significantly mediate the effect of long delays on decision time in the task following the delay, indirect effect = 0.10, 95% C.I. = (-0.15, 0.34). Therefore, H5a was not supported. Note that there was still a significant direct effect, just not a mediation effect. In Model 2, we see that brain state switching during the task following the delay, H5b, significantly mediates the effect of long delays on decision time in the task following the delay, indirect effect = 0.36, 95% C.I. = (0.23, 0.50). We also note that the direct effect of long delays on decision time in the task following the delay is still significant in this model. Thus, long delays may have both a mediated effect (i.e., brain state switches after the new task starts/switching back) and a direct effect. Therefore, there could be additional mechanisms through which long delays slow decision-making in subsequent tasks.

## Study 1 Summary

The results suggest that brain state switches can be detected and that they are most often detected during and following long delays. When they are detected, the time to make a decision increases by almost 20% vs short delays. When brain state switches are not detected there is no significant difference in decision time as compared to short delays. Thus, it seems that long delays do cause changes in brain states that degrade performance.

Much of this can be viewed in relation to task switching. Task switching or set switching occurs when a person switches from one type of cognitive task to another (Jersild, 1927). In experiments on task switching, participants perform multiple discrete tasks—say Tasks A and B. The ordering of the tasks influences the speed at which the tasks are completed. For example, the sequence A-B will take longer than the times for A-A and B-B suggest (Jost et al., 2013). This loss of efficiency is attributed to the cognitive cost of switching (Jersild, 1927). There seem to be two reasons for this loss of efficiency. First, when switching from A to B, the mental resources required for Task B need to be configured and brought online in the brain (Rogers & Monsell, 1995). Second, the mental resources for A need to be actively inhibited (Allport et al., 1994). These mental resources were originally called sets (Jersild, 1927)— hence the term “set switching”—but now the term “task switching” is more popular.

<table><tr><td colspan="5">Table 5. Decision Time Explained by Delays and Brain State Switching</td></tr><tr><td>Hypothesis</td><td>Explanatory variable</td><td>b</td><td>t</td><td>p</td></tr><tr><td>H3</td><td>Long delay</td><td>1.17</td><td>5.44</td><td>&lt; .001</td></tr><tr><td>H4a</td><td>Brain state switching (during delay)</td><td>0.83</td><td>3.32</td><td>&lt; .001</td></tr><tr><td>H4b</td><td>Brain state switching (during task following delay)</td><td>2.39</td><td>10.64</td><td>&lt; .001</td></tr></table>

Note: Delay is dummy coded (1 = long delay, 0 = short delay). Both brain state switching variables are dummy coded (1 = brain state switching, 0 = no brain state switching).

Table 6. Results of Brain State Switching Mediating the Effect of Long Delays on Decision Time in the Task after the Delay

<table><tr><td colspan="3">Task after the Delay</td></tr><tr><td>H5a Model 1</td><td>Estimate</td><td>95% C.I.</td></tr><tr><td>Indirect effect (brain state switching during delay)</td><td>0.10</td><td>(-0.15, 0.34)</td></tr><tr><td>Direct effect</td><td>1.07</td><td>(0.58, 1.56)</td></tr><tr><td>Total effect</td><td>1.17</td><td>(0.74, 1.58)</td></tr><tr><td>Proportion of effect mediated</td><td>0.09</td><td>(-0.12, 0.32)</td></tr><tr><td>H5b Model 2</td><td>Estimate</td><td>95% C.I.</td></tr><tr><td>Indirect effect (brain state switching during task after delay)</td><td>0.36</td><td>(0.23, 0.50)</td></tr><tr><td>Direct effect</td><td>0.81</td><td>(0.40, 1.22)</td></tr><tr><td>Total effect</td><td>1.17</td><td>(0.75, 1.59)</td></tr><tr><td>Proportion of effect mediated</td><td>0.30</td><td>(0.19, 0.49)</td></tr></table>

It is dangerous to say that task switching and brain state switching are the same thing because the former is a cognitive process and the latter a neural process. Thus, there may not be a one-to-one mapping between the two. It is possible that a task can switch while brain states remain constant or vice versa (Sakai, 2008). Nonetheless, our results show that participants are slower when a brain state switch is observed. This slower performance is the hallmark of task switching. This suggests several avenues for future research.

The first question is whether all brain states are tasks. The next question is whether the brain state that sometimes occurs during delays counts as a task. It could make sense to take a broad view that everything the brain does is a task, but then the definition of task would simply be that which the brain does, which does not seem to be the intention of task switching research. This is a philosophical question that cannot be answered here.

Assuming that the new brain state during a delay is a task, what sort of task is it? Does it have special characteristics? In particular, if task switching is associated with slower responses, then evolution would strongly select for default tasks that are particularly easy to switch out of. An organism that could switch more quickly into tasks like fight or flight, even if only by fractions of a second, would have a fitness advantage.

For the current study, this brings up questions about how much of the switching cost was due to an inhibition of the delay task and how much was due to loading the task set for the main task. If there is a standard task that occurs when not otherwise engaged, then organisms probably have a great deal of practice inhibiting that task and may hence be much better at it than at inhibiting other tasks. The current experiment is not set up to measure this and the temporal resolution of MRI may not be suited for it, but it is an interesting question.

Finally, one of the interesting experimental differences between this work and task switching studies—still assuming that the brain state switch is a task switch—is that our participants occasionally spontaneously chose to switch to the delay task. This is important for two reasons. First, in most task switching research, the researcher specifies the tasks and when to switch them. Some research has allowed participants to voluntarily choose to switch between two tasks (Arrington et al., 2007), but this is not the norm and the researchers still specified the tasks in these cases. In our study, participants chose what the delay task was. Second, a major issue with task switching is potential confusion between the effects of the cue versus the effects of the actual task. At least some of the task switching can be done proactively before the actual stimulus is presented, but some of the task switch needs to be done after the stimulus presentation (Jost et al., 2013). In our experiment, participants internally generated a cue that told them to switch to the delay task. However, they did not always do so. Thus, this may suggest a means by which task switching researchers could control for cue switching, which would allow them to develop new insights into the mechanisms that lead to slower response times. The caveat is that this is all based on the assumption that the brain state switching represents a task switch.

## Study 2: Potential Interventions

One question arising from Study 1 is whether there are viable interventions that could mitigate the effects of delays on user performance. To examine this, we conducted a second study, wherein we tested four interventions, and two baseline conditions (short delay and long delay conditions, respectively), for a total of six different experimental conditions. If long delays result in brain state switching, then possible interventions could include filling the delay with something that is task relevant. By doing so, users might remain engaged with the task and their brains might remain “warmed up” in the task-appropriate brain state when the delay ends. If these interventions can be identified, we could provide a practical tool for developers to deploy to help keep users’ brains engaged.

In addition, in Study 2, we built on Study 1 by including a task with an objective accurate response for each trial. Specifically, we used a vigilance task for Study 2. Vigilance is important for many domains including those related to information security, homeland security, or nuclear reactors. Furthermore, unlike the task that used apps from the Google Play store in Study 1, a vigilance task must have both a temporal component and an objective correct answer to allow us to measure both response time and accuracy.

Study 2 is a behavioral study designed to enhance and extend our neuroscience findings. Based on our findings in Study 1, we expected that long delays lead to brain state switching, which harms user performance. Accordingly, in Study 2, we expected participants encountering long delays to perform worse both in terms of accuracy and speed than those encountering short delays. Our interventions were designed to keep users engaged with the task, thereby reducing the chance of brain state switching and improving performance compared to those encountering long delays with no intervention. Accordingly, our interventions were designed to reduce the chance of brain state switching, and our outcomes of interest were response time and accuracy.

## Task

A standard response to targets vigilance task—as used in Helton (2009)—was employed to assess vigilance. This task follows a “go/no-go” paradigm. That is, certain stimuli (“go” trials) require a response, whereas other stimuli (“no-go” trials) require the withholding of a response. Standard measures of vigilance require a response to low-probability stimuli, with the response being withheld for most stimuli (Helton, 2009).

For the task in the current study, each trial participant viewed a single digit ranging from 1-9. Participants were instructed to only press the spacebar when the digit shown was a “3.” Otherwise, participants were instructed to not press the spacebar. For each trial, each digit had a 1/9 probability of being displayed. Therefore, 1/9 of trials were “go” trials (i.e., a “3” was shown) and 8/9 of trials were “no-go” trials (i.e., any digit other than “3” was shown). Because of the two types of trials, there were two types of errors that could be made. A “no-go” error occurred if a participant pressed the spacebar in a “no-go” trial. A “go” error occurred if a participant failed to push the spacebar in a “go” trial. Participants completed two blocks of 60 trials each. At the beginning of the study, participants completed a training block of 18 trials to familiarize them with the task.

Note that by manipulating delay duration, we are also manipulating the interstimulus interval that is present in “go-nogo” paradigm tasks. Research has shown that shorter interstimulus intervals tend to result in worse performance on these tasks (Hasegawa et al., 2021; Young et al., 2018). However, these studies examined interstimulus intervals of 250- 1000 milliseconds. In our research, we believe that long delays result in much longer interstimulus intervals, which we expect would harm performance based on the results of Study 1.

## Experimental Conditions

There were six experimental conditions: short and long delay conditions plus four intervention conditions. A betweenparticipants approach was used to isolate the effects of any interventions to one condition. Participants were randomly assigned to a condition when beginning the study. The same task was performed in all conditions. The differences between conditions occurred during the delay period. The length of the delay in the intervention conditions was equal to that of the long delay condition but what was displayed by the system during the delay varied.

## Short Delay

In the short delay condition, a delay ranging randomly between 100 milliseconds and 1 second was inserted between each trial. During the delay, a black screen with the word “Loading…” was displayed. After this short delay, the next trial began.

## Long Delay

In the long delay condition, a delay ranging randomly between 8 and 10 seconds was inserted between each trial. During the delay, a black screen with the word “Loading…” was displayed. After this long delay, the next trial began.

## Simultaneous Performance Display

For Intervention 1, during each long delay, participants were shown statistics of their performance on the task up to that point. Participants were shown how many trials they had completed, how many tasks they had performed correctly, the percentage of tasks performed correctly, the number of mistakes made when a “3” was displayed, and the number of mistakes made when a “3” was not displayed. Because these were statistics of performance up to that point, these numbers were updated after each trial. All of these statistics were shown simultaneously. After the long delay, the next trial began. The reasoning for including this intervention was that it would fill the delay with something that was task relevant. By reading about their performance up to that point, we anticipated that participants would be more likely to remain in the brain state appropriate for the current task.

## Gradual Performance Display

For Intervention 2, participants were shown the same performance statistics but were shown to them gradually rather than simultaneously. The reasoning for this is that it would provide more opportunities to keep participants in the taskrelevant brain state. If participants are shown the statistics all at once, they could quickly glance at them and then drift into another brain state for the rest of the delay. By presenting the information one piece at a time, we sought to “anchor” participants to the present task and prevent brain state switching. Therefore, in this condition, each piece of information was displayed for one fifth of the delay period before the next piece of information was added to the screen. After the long delay, the next trial began.

## Countdown Timer

Intervention 3 was developed as an alternative to our reasoning that it is important for users to maintain the task-appropriate brain state during the delay period. An alternative argument could be made that users only need to know when the next task is about to begin. Perhaps if they know that the next task is about to begin, they can “warm up” their brains for the taskappropriate brain state before the next task starts. If this is the case, it would be okay for brain state switching to occur during a delay as long as users are notified when it is time to switch back before beginning the next task. Accordingly, for Intervention 3 a countdown timer was included below the word “Loading…” that was included in the long delay condition. For example, if the delay for a trial was 8 seconds, the timer began counting down from 8 to 1. When 1 appeared, the participant would know that the next trial was about to begin.

## Dummy Task

Intervention 4 was developed as an active task to keep participants engaged in the task-appropriate brain state during a long delay. To do this, we inserted a “dummy task” into the long delay. That is, participants performed what seemed to be another trial during the long delay but this task was not counted toward their overall performance. The dummy task was inserted at the end of the long delay before the next real task so that participants’ brains could “warm up” during the dummy task and be ready once the real task began. Between the dummy task and the real task, a short delay (between 100 milliseconds and 1 second) was inserted.

The reasoning underlying this task was to address the possible limitations of presenting statistics about participants’ performance at a given point in time. Although the performance statistics in Interventions 1 and 2 offer a task-relevant means of keeping users in the taskappropriate brain state, since these interventions are passive, participants may drift into another brain state anyway. The dummy task intervention, on the other hand, is active and requires participants to maintain engagement with the system and may thus be a superior intervention for preventing brain state switching.

## Participants

The participants were 667 people from the research platform Prolific (short delay condition: n = 126, long delay condition: n = 103, simultaneous performance display condition: n = 115, gradual performance display condition: n = 103, countdown timer condition: n = 110, dummy task condition: n = 110. They received \$6.00 in compensation and took about 30 minutes to complete the study. Detailed demographic information by condition is presented in Appendix B.

## Results

The results for average error rates by condition are displayed in Figure 6. As the figure shows, participants performed better in the short delay trials compared to other conditions in both “go” and “no-go” trials. The first chart in Figure 6 shows the average error rate for “no-go” trials (when they should not have responded but did) and the second chart shows the average error rate for “go” trials (when they should have responded but failed to).

![](/api/attachments/5EK37EAS/fulltext/images/22dde753d9470ae30935041dac9f9f6f7a1b5b46e47b05ad491b0cb05b763045.jpg)

![](/api/attachments/5EK37EAS/fulltext/images/4812409b455fd7f6a0f4d304ff7ffd5c15d3659737168c8a1ceed108584ceade.jpg)  
Figure 6. Error Rates with Standard Errors for Interventions

Because participants engaged in multiple task trials, the trials completed by the same person were likely not independent: the trials were nested within participants. Therefore, as in Study 1, we used regression models with random intercepts using restricted maximum likelihood (REML) estimation to examine any differences in performance by the intervention conditions compared to the short delay condition. We again used the lme4 package (Bates et al., 2015) in R. The significance of explanatory variables was again determined with t-tests and degrees of freedom using the Satterthwaite method (which again allows for partial degrees of freedom). The results for this model for “go” trials are displayed in Table 7. This model suggests that in “go” trials, performance in all other conditions was worse than the performance in the short delay condition.

As with the go trials, we examined a random intercept regression model for “no-go” trials to assess differences in performance between groups (see Table 8). In “no-go” trials, performance in each intervention was significantly worse than the performance in the short delay condition

<table><tr><td colspan="5">Table 7. Vigilance Task Performance in Go Trials</td></tr><tr><td>Parameter</td><td>Estimate</td><td>df</td><td>t</td><td>p</td></tr><tr><td>Intercept</td><td>.0079</td><td></td><td></td><td></td></tr><tr><td>Long delay</td><td>.0686</td><td>667.9</td><td>4.17</td><td>&lt; .001</td></tr><tr><td>Simultaneous performance display</td><td>.0575</td><td>665.8</td><td>3.60</td><td>&lt; .001</td></tr><tr><td>Gradual performance display</td><td>.0699</td><td>665.7</td><td>4.25</td><td>&lt; .001</td></tr><tr><td>Countdown timer</td><td>.0436</td><td>662.7</td><td>2.71</td><td>&lt; .01</td></tr><tr><td>Dummy task</td><td>.0520</td><td>672.3</td><td>3.21</td><td>&lt; .01</td></tr></table>

Note: Short delay condition is the reference group (coded 0).

<table><tr><td colspan="5">Table 8. Vigilance Task Performance in No-Go Trials</td></tr><tr><td>Parameter</td><td>Estimate</td><td>df</td><td>t</td><td>p</td></tr><tr><td>Intercept</td><td>.0026</td><td></td><td></td><td></td></tr><tr><td>Long delay</td><td>.0068</td><td>658.2</td><td>5.00</td><td>&lt; .001</td></tr><tr><td>Simultaneous performance display</td><td>.0049</td><td>658.8</td><td>3.71</td><td>&lt; .001</td></tr><tr><td>Gradual performance display</td><td>.0041</td><td>659.2</td><td>2.99</td><td>&lt; .01</td></tr><tr><td>Countdown timer</td><td>.0059</td><td>660.1</td><td>4.45</td><td>&lt; .001</td></tr><tr><td>Dummy task</td><td>.0029</td><td>657.0</td><td>2.20</td><td>.03</td></tr></table>

Note: Short delay condition is the reference group (coded 0).

![](/api/attachments/5EK37EAS/fulltext/images/ccf048d313d81f2d2866d0e66c888cc80a3ff17c5df5124e51671e1762097e43.jpg)  
Figure 7. Average Response Times by Conditions

<table><tr><td colspan="5">Table 9. Vigilance Task Response Time Performance</td></tr><tr><td>Parameter</td><td>Estimate</td><td>df</td><td>t</td><td>p</td></tr><tr><td>Intercept</td><td>461.48</td><td></td><td></td><td></td></tr><tr><td>Long delay</td><td>103.55</td><td>639.3</td><td>8.28</td><td>&lt; .001</td></tr><tr><td>Simultaneous performance display</td><td>127.91</td><td>637.0</td><td>10.54</td><td>&lt; .001</td></tr><tr><td>Gradual performance display</td><td>49.96</td><td>641.6</td><td>3.98</td><td>&lt; .01</td></tr><tr><td>Countdown timer</td><td>-14.99</td><td>634.1</td><td>-1.22</td><td>.22</td></tr><tr><td>Dummy task</td><td>101.53</td><td>641.8</td><td>8.25</td><td>&lt; .001</td></tr></table>

Note: Short delay condition is the reference group (coded 0).

Because the dummy task condition essentially requires participants to complete twice as many tasks as other conditions, it is possible that participants in this condition become fatigued more quickly, which could have harmed performance. If so, it is possible that performance in the dummy task condition would become worse toward the end of the task. To check this, we reran the analyses to see how performance in the first half of the trials of the dummy task compared to the short delay condition during these trials. These analyses showed that in the first half of trials for “go” trials $( p \ < \ 0 . 0 0 1 )$ , the performance in the dummy task condition was still worse than the performance in the short delay condition. However, in the first half of trials for “no-go” trials $( p \ = \ 0 . 2 8 )$ there was no significant difference in performance between the dummy task condition and the short delay condition. Thus, there seemed to be some effect of fatigue in the dummy task intervention.

The results for average response time are shown in Figure 7 above. Note that the average response time was calculated for each participant only for trials in which the participant responded. If the participant did not press the space bar in a trial, that trial was not factored into the average response time. This should have little impact as there were many trials per participant. We again examined a random intercept regression model to assess condition differences in response time (see Table 9). In all interventions except for the countdown timer condition response times were slower than the short delay condition. Thus, in terms of response time, the performance in the short delay and countdown timer conditions was the best.

Because our interventions were designed to keep users engaged with the task, in addition to measuring performance, we also asked participants about their subjective feelings of interest and boredom (using a 7-point scale) at the beginning of the task, at the midpoint of the task, and at the end of the task. The results are depicted in Figure 8. As the charts show, participants in each condition began with fairly similar levels of interest and boredom, but for all of the interventions and the long delay condition, participants became much more bored and much less interested at the midpoint and end, whereas for the short delay condition interest and boredom changed very little.

An ANOVA explaining boredom scores prior to the task suggested that there was at least one between-group difference in boredom, F(5, 661) = 3.10, p < 0.01. Tukey’s HSD test for multiple mean comparisons showed a significant difference between the dummy task and gradual performance display conditions $( p < 0 . 0 1 )$ only, with those in the dummy task condition reporting less boredom before the beginning of the task. An ANOVA for boredom scores halfway through the task (Time 2) indicated that there was at least one between-group difference in boredom, F(5, 661) = 22.18, p < 0.001. Tukey’s HSD test for multiple mean comparisons showed significant differences between the short delay condition and each other condition only (ps < 0.001). An ANOVA for boredom scores after task completion (Time 3) indicated that there was at least one between-group difference in boredom, F(5, 661) = 26.22, p < 0.001. Tukey’s HSD test for multiple mean comparisons showed significant differences between the short delay condition and each other condition only (ps < 0.001).

An ANOVA explaining interest scores before the task suggested that there was at least one between-group difference in interest, F(5, 661) = 4.08, p < 0.01. Tukey’s HSD test for multiple mean comparisons showed that those in the dummy task condition reported significantly greater interest than those in the short delay (p < 0.01), simultaneous performance display $( p = 0 . 0 2 )$ , and gradual performance display conditions (p < 0.01). An ANOVA for interest scores halfway through the task (Time 2) indicated that there was at least one between-group difference in interest, F(5, 661) = 14.85, p < 0.001. Tukey’s HSD test for multiple mean comparisons showed significant differences between the short delay condition and each other condition only (ps < 0.001). An ANOVA for interest scores after completion of the task (Time 3) indicated that there was at least one between-group difference in interest, F(5, 661) = 18.72, p < 0.001. Tukey’s HSD test for multiple mean comparisons showed significant differences between the short delay condition and each other condition only (ps < 0.001).

![](/api/attachments/5EK37EAS/fulltext/images/2db6f740cecb9bc5adcb5ca7a2b03ace85f58fb33cdcd1bf441555e5627be2ab.jpg)

Boredom Over Time  
![](/api/attachments/5EK37EAS/fulltext/images/63313d2754a0a3c356ce56026cf1f7759ad96d4765139866c8fe2868c8e4801c.jpg)  
Figure 8. Subjective Feelings over Time on a 7-Point Scale

## Study 2 Summary

Overall, this study shows that long delays can harm performance both in terms of speed and accuracy. Moreover, it shows that performance can be improved somewhat relative to long delays with some interventions. In terms of improving speed, the performance in the countdown timer intervention was the best. In terms of improving accuracy, the dummy task performance was the best. However, the performance in all the interventions was still significantly worse than the performance in the short delay condition. We need to consider the possibility that there may be no perfect intervention for delay—other than the fix of removing the delay. In addition, short delays produced less boredom and more interest at the midpoint and endpoint of the task. In sum, while the problem of performance issues with delays can be mitigated but not eliminated with interventions, interventions appear to come at the cost of increased boredom and lack of interest.

## Discussion

## Contributions to Theory and Research

We contribute to the literature on system delays by identifying a mechanism by which long delays impact user performance. In theory development, the mechanism that explains a relationship can be thought of as the why of a theory (Whetten, 1989). The explanation of why is arguably the most important piece of theory development (Whetten, 1989). A greater understanding of why can help generate solutions for a problem (which was the inspiration for Study 2). We captured a mechanism of how long delays impact user performance by relying on the in-the-moment experience of users during long delays rather than relying on user recall after the fact. This allowed us to gain a realistic snapshot of what users experience during delays. What we found was striking. Users often cannot help but switch brain states when experiencing a long delay. Although there is no new task on the screen, their minds “go to a different place” and engage in something else. We also see that this disengagement from the primary task persists after the long delay ends—the user must reengage with the task. This requires users to return to their prior brain state. Although, in our study, long delays still had a direct effect on decision time, we did achieve our goal of identifying a mechanism by which long delays impact performance. It would be rash to assume that we could identify “the one and only” mechanism of this relationship, as most relationships have multiple mechanisms underlying them. Thus, we achieved our aim and thereby open the door to future research identifying additional mechanisms in addition to brain state switching that can explain the relationship between long delays and performance.

Brain activation measured by fMRI is based on oxygenated blood flow and is correlated with increased metabolic cost. The greater brain activation in the first half of a task following a long delay represents a greater metabolic cost to the user, compared to completing the task after a short delay. Furthermore, decision time is often used as a proxy or indirect measure of decision effort (Bettman et al., 1990; Cooper-Martin, 1994; Otto & Daw, 2019). This suggests that after long delays, the task may be more effortful. The present study shows that long delays are not only costly in terms of time lost during the delay but that the delay also makes the following task more metabolically costly and increases the time needed to complete it.

We found partial support for default-mode activation during tasks but not in the delay between tasks. This could be because the time within the task was not sufficient for the brain to switch fully into the default-mode network. We found that activation before the switch during a long delay was concentrated in the caudate and visual cortex. The caudate is known to play an important role in visual attention (Lawrence, Ross & Stein, 2002). Thus, having higher activation before the switch is consistent with someone trying to maintain attention and failing. More research on this is warranted.

We also found evidence that long delays negatively impact decision-making. Not only were decisions more metabolically costly but they also took longer to make after a long delay. Following a long delay, participants who showed measurable brain state switching took 2.40 seconds (20.63%) longer to complete the task than participants following a short delay with no brain state switching. However, participants who did not show measurable brain state switching after a long delay took only 0.45 seconds (3.91%) longer to make a decision. Although in one isolated decision, the slight increase in decision time might not seem like a problem, across hundreds of decisions each day, this increased time adds up. In addition, as stated above, decisions made after a long delay may also require more effort. Since long delays could force users to spend more time and/or effort making decisions, if many decisions must be made, this could contribute to increased decision fatigue or ego depletion (Polman & Vohs, 2016; Sjåstad & Baumeister, 2018). It is well known that system response time also has negative effects on the autonomic nervous system, including fatigue (for a review see Riedl & Fischer, 2018). In sum, long delays not only increase decisionmaking time due to the time lost to the delay but they may also increase decision-making time post-delay due to the increased time and effort needed to make decisions caused by brain state switching occurring after a long delay.

We also contribute to the NeuroIS community and the broader IS community through the use of the t-SNE algorithm to detect brain state switching. Up to this point, NeuroIS research using fMRI has primarily relied on general linear model analyses. We advance the NeuroIS field by combining brain data with data science to show an example of what else we can learn from these data by using cutting-edge methods. The data from neuroimaging already constitute Big Data (with more than 3.4 billion observations in this study), and advanced techniques can be used to fully leverage to benefits of these data.

In a follow-up study of potential interventions, we found some mitigation of long delays for a variety of interventions. However, all of the interventions had significantly higher error rates and all but one (countdown timer) had significantly slower response times than those in the short delay condition, which would make sense if the operative mechanism is brain state switching. In terms of accuracy, the most effective intervention was replicating the task exactly (dummy task). However, this led to problems as participants needed to complete twice as many tasks and thus became more bored and less engaged. In practical terms, if delays are unavoidable, we found that a warmup task is best for accuracy and a countdown timer is best for speed. Obviously, this may be distasteful for designers, but in other activities where performance is key—such as singing, acting, and sports— warm-up exercises are often used.

## Practical Implications

Our results suggest that system delays should be taken seriously by practitioners. For example, the average loading time for a mobile webpage is still 15 seconds (An, 2018). We found that delays in the range of 10 to 20 seconds could lead to brain state switching and impact the subsequent task. Therefore, while the typical loading times that users experience make them vulnerable to brain state switching, our study on interventions suggests that this brain state switching may not be fully avoidable.

Although system response time is not always fully under an organization’s control, there are steps that can be taken to improve response time and limit delays. Our results suggest that it may be worth the investment to take such steps to reduce delays. Given that mobile pages tend to take longer to load, it is particularly important for organizations to create separate mobile pages or apps that contain less content to load per page (An, 2018). Also, web designers could minimize graphics to speed up page loading (Galletta et al., 2006).

Perhaps the biggest implication concerns software as a service (SaaS). Many vendors offer product models where processing is done remotely from the user, typically via internet connectivity. This offers many advantages to the management of software, but if the internet results in delays that locally installed software does not produce, this may undermine employee efficiency and efficacy. Our results suggest that long delays increased decision-making time by around 10%, which reduces the number of decisions a person can make in a given time by approximately 10%. Of course, not every internet request results in a long delay and not every locally hosted software request results in a short one. Nonetheless, it is worth considering whether remotely managed SaaS decreases user productivity. This could be a game changer in the SaaS value proposition.

Recently, much of the research on system delays has focused on interventions to mitigate the negative impact of delays by reducing perceived wait times (Hong et al., 2013; Lee et al., 2012; Lee et al., 2017). Indeed, if effective interventions could be discovered, it would not be necessary to make the difficult decisions regarding whether and how to reduce or eliminate delays. However, our Study 2 on interventions suggests that these difficult decisions may be unavoidable. In Study 2, rather than perceived wait time, we examined interventions that might reduce the negative impact of delays on performance. None of the four interventions designed based on the results of Study 1 fully eliminated the negative impact of delays on user performance. It is possible that brain state switching is a biological process that cannot be completely avoided through interventions.

Practitioners must consider the trade-offs of when the negative impact of delays on performance is worth the benefits of cloud computing, mobile computing, and large software. If the benefits are still worth it, practitioners may then consider implementing either the countdown timer or the dummy task intervention to fill delays. If speed is particularly important for a given task, the countdown timer may be useful for filling delays. Conversely, if accuracy is more important than speed, an active intervention such as the dummy task could be used to fill delays. But it is important to remember that these interventions can only go so far. While smokers may try to use interventions such as exercise and a blueberry-rich diet to mitigate the negative impacts of smoking, smoking still causes cancer. Likewise, even though delays may be unavoidable, interventions can mitigate but not eliminate the negative impact of delays. There is no workaround.

## Limitations and Directions for Future Research

In this research, the delay was expected and of random length. Moreover, it occurred between tasks rather than during tasks. It is worth investigating how unexpected delays might affect users (as done by Kohrs et al., 2016). In such a case, it would be important to tease out the effect of the surprise versus the effect of the delay. User expectations might also have impacts on behavioral and NeuroIS outcomes and are worth investigating. Since the nature of the task might also play a role, it would be worthwhile to investigate multiple tasks of varying complexity, excitement, and importance to see if processes and perceptual measures are uniformly impacted.

Although the interventions in Study 2 were developed based on the results of Study 1, a limitation of Study 2 is that we did not have brain data to assess whether the same brain state switching mechanism was occurring. However, the behavioral nature of Study 2 allowed us to test more interventions with more participants. Future research could follow up on our study by combining brain data with one or more of these interventions.

Future research could dive deeper into the relationship between system delays and effort. Although we found some evidence that system delays may make tasks more metabolically costly, we could not definitively conclude that they make tasks more effortful. We speculated that system delays may make tasks more effortful but more research is needed with an a priori goal of assessing the impact of delays on effort. EEG is often used to measure cognitive load via the comparison of alpha and theta wave characteristics and may be one fruitful method for measuring effort or cognitive load in response to system delays (Dasari et al., 2017; Gevins, 2000).

The reviewers of this work suggested many interesting directions for future research based on this work. While this work explores expected delays, there is other work that explores the neural reactions to unexpected delays (Kohrs et al., 2016). Are there additional or different neural mechanisms at work for unexpected versus expected delays? More generally, are there multiple neural mechanisms at work in delays? There is a large literature on IT interruptions (Addas & Pinsonneault, 2015; Chen & Karahanna, 2018), which suggests that delays are one type of interruption. Are delays like other kinds of interruptions or do they have some unique properties, and, if so, are these properties measurable at a neural level? Similarly, there is a large literature on task switching (Kiesel et al., 2010; Koch et al., 2018; Monsell, 2003). Future research could evaluate whether brain state switching is the same as task switching, whether switching from Task A to Task B is the same as switching from Task A to a delay, and whether there are fundamental differences in these types of switching. The literature on “go/no-go” tasks may be of some use here (Scheil & Kleinsorge, 2022). Theories like the adaptive control of thought—rational (ACT-R, see Anderson et al., 1997) contain many of the constructs we use here, plus more to flesh out a full model of cognitive architecture based on neuroscience. Can these additional constructs be integrated with our findings to improve our understanding of delays?

## Conclusion

In Study 1, we took a NeuroIS approach to explore the realtime brain reactions to system delays. By using the t-SNE algorithm and general linear model analyses, we showed that long delays are more likely to induce brain state switching than short delays both during the delay and in the subsequent task. This brain state switching induced by long delays makes subsequent decisions more effortful, and users take longer to make the decisions.

In Study 2, we developed four interventions for delays during a vigilance task that has a speed and accuracy component. We found that two interventions can mitigate but not eliminate the negative impacts of delays. Specifically, a countdown timer can improve response time while a dummy task can improve accuracy. However, in these interventions, performance still did not match that of participants who experienced short delays only.

Our research demonstrates the importance of continuing to study system delays as a field. It also demonstrates the importance of practitioners making investments that reduce delay times. We also propose interventions that can mitigate some of the negative impact of delays. But we argue that interventions may not be able to eliminate brain state switching during delays. Future research could help to improve the understanding of other ways that long delays and brain state switching can impact user experience and performance.

## References

Addas, S., & Pinsonneault, A. (2015). The many faces of information technology interruptions: A taxonomy and preliminary investigation of their performance effects: Information technology interruptions taxonomy and performance effects. Information Systems Journal, 25(3), 231-273. https://doi.org 10.1111/isj.12064

Allport, A., Styles, E. A., & Hsieh, S. (1994). Shifting Intentional Set: Exploring the Dynamic Control of Tasks. In C. Umilta & M. Moscovitch (Eds.), Conscious and nonconscious information processing: Attention and performance (pp. 421-452). MIT Press.

An, D. (2018). Find out how you stack up to new industry benchmarks for mobile page speed. Think with Google. https://www.thinkwithgoogle.com/marketing-strategies/appand-mobile/mobile-page-speed-new-industry-benchmarks

Anderson, J. R., Matessa, M., & Lebiere, C. (1997). ACT-R: A theory of higher level cognition and its relation to visual attention. Human-Computer Interaction, 12(4), 439-462. https://doi.org/ 10.1207/s15327051hci1204\_5

Arrington, C. M., Logan, G. D., & Schneider, D. W. (2007). Separating cue encoding from target processing in the explicit task-cuing procedure: Are there “true” task switch effects? Journal of Experimental Psychology: Learning, Memory, and Cognition, 33(3), 484-502. https://doi.org/10.1037/0278- 7393.33.3.484

Barber, R. E., & Lucas, H. C. (1983). System response time operator productivity, and job satisfaction. Communications of the ACM, 26(11), 972-986. https://doi.org/10.1145/182.358464

Bates, D., Maechler, M., Bolker, B., & Walker, S. (2015). Fitting linear mixed-effects models using lme4. Journal of Statistical Software, 67(1), 1-48. https://doi.org/10.18637/jss.v067.i01

Bettman, J. R., Johnson, E. J., & Payne, J. W. (1990). A componential analysis of cognitive effort in choice. Organizational Behavior and Human Decision Processes, 45(1), 111-139. https://doi.org/ 10.1016/0749-5978(90)90007-V

Butler, T. W. (1983). Computer response time and user performance. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 58-62). https://doi.org/10.1145/ 800045.801581

Chen, A., & Karahanna, E. (2018). Life interrupted: the effects of technology-mediated work interruptions on work and nonwork outcomes. MIS Quarterly, 42(4), 1023-1042. https://doi.org/ 10.25300/MISQ/2018/13631

Cooper-Martin, E. (1994). Measures of cognitive effort. Marketing Letters, 5(1), 43-56. https://doi.org/10.1007/BF00993957

Dasari, D., Shou, G., & Ding, L. (2017). ICA-derived EEG correlates to mental fatigue, effort, and workload in a realistically simulated air traffic control task. Frontiers in Neuroscience, 11, 297. https://doi.org/10.3389/fnins.2017.00297

Davis, E. S., & Hantula, D. A. (2001). The effects of download delay on performance and end-user satisfaction in an internet tutorial. Computers in Human Behavior, 17(3), 249-268. https://doi.org/10.1016/S0747-5632(01)00007-3

Dean, B. (2019). We analyzed 5.2 million webpages. Here’s what we learned about pagespeed. Backlinko. https://backlinko.com/ page-speed-stats

Dennis, A. R., & Taylor, N. J. (2006). Information foraging on the web: The effects of “acceptable” Internet delays on multi-page information search behavior. Decision Support Systems, 42(2), 810-824. https://doi.org/10.1016/j.dss.2005.05.032

DiClemente, D. F., & Hantula, D. A. (2003). Optimal foraging online: Increasing sensitivity to delay. Psychology and Marketing, 20(9), 785-809. https://doi.org/10.1002/mar.10097

Dimoka. (2012). How to conduct a functional magnetic resonance (fMRI) study in social science research. MIS Quarterly, 36(3), 811. https://doi.org/10.2307/41703482

Galletta, D. F., Henry, R. M., McCoy, S., & Polak, P. (2006). When the wait isn’t so bad: the interacting effects of website delay, familiarity, and breadth. Information Systems Research, 17(1), 20-37. https://doi.org/10.1287/isre.1050.0073

Galletta, D. F., Henry, R., McCoy, S., & Polak, P. (2004). Web site delays: How tolerant are users? Journal of the Association for Information Systems, 5(1), 1-28. https://doi.org/10.17705/1jais. 00044

Gevins, A. (2000). Neurophysiological measures of working memory and individual differences in cognitive ability and cognitive style. Cerebral Cortex, 10(9), 829-839. https://doi.org/ 10.1093/cercor/10.9.829

Goldfarb, M. G., & Brown, D. R. (2022). Diversifying participation: The rarity of reporting racial demographics in neuroimaging research. NeuroImage, 254, Article 119122. https://doi.org/ 10.1016/j.neuroimage.2022.119122

Gruber, T., & Müller, M. M. (2002). Effects of picture repetition on induced gamma band responses, evoked potentials, and phase synchrony in the human EEG. Cognitive Brain Research, 13(3), 377-392. https://doi.org/10.1016/S0926-6410(01)00130-6

Hasegawa, A., Matsumoto, N., Yamashita, Y., Tanaka, K., Kawaguchi, J., & Yamamoto, T. (2021). Do shorter interstimulus intervals in the go/no‐go task enable better assessment of response inhibition? Scandinavian Journal of Psychology, 62(2), 118-124. https://doi.org/10.1111/sjop.12679

Helton, W. S. (2009). Impulsive responding and the sustained attention to response task. Journal of Clinical and Experimental Neuropsychology, 31(1), 39-47. https://doi.org/10.1080/138033 90801978856

Hong, W., Hess, T. J., & Hardin, A. (2013). When filling the wait makes it feel longer: A paradigm shift perspective for managing online delay. MIS Quarterly, 37(2), 383-406. https://doi.org/ 10.25300/MISQ/2013/37.2.04

Hugdahl, K., Kazimierczak, K., Beresniewicz, J., Kompus, K., Westerhausen, R., Ersland, L., Grüner, R., & Specht, K. (2019). Dynamic up- and down-regulation of the default (DMN) and extrinsic (EMN) mode networks during alternating task-on and task-off periods. PLOS ONE, 14(9), Article e0218358. https://doi.org/10.1371/journal.pone.0218358

Imai, K., Keele, L., & Tingley, D. (2010). A general approach to causal mediation analysis. Psychological Methods, 15(4), 309- 334. https://doi.org/10.1037/a0020761

Jenkinson, M., Beckmann, C. F., Behrens, T. E. J., Woolrich, M. W., & Smith, S. M. (2012). FSL. NeuroImage, 62(2), 782-790. https://doi.org/10.1016/j.neuroimage.2011.09.015

Jersild, A. T. (1927). Mental set and shift (Archives of Psychology, No. 89). n.p.

Jost, K., De Baene, W., Koch, I., & Brass, M. (2013). A Review of the Role of Cue Processing in Task Switching. Zeitschrift Für Psychologie, 221(1), 5-14. https://doi.org/10.1027/2151-2604/ a000125

Kiesel, A., Steinhauser, M., Wendt, M., Falkenstein, M., Jost, K., Philipp, A. M., & Koch, I. (2010). Control and interference in task switching—A review. Psychological Bulletin, 136(5), 849- 874. https://doi.org/10.1037/a0019842

Koch, I., Poljac, E., Müller, H., & Kiesel, A. (2018). Cognitive structure, flexibility, and plasticity in human multitasking—An integrative review of dual-task and task-switching research. Psychological Bulletin, 144(6), 557-583. https://doi.org/10.1037/ bul0000144

Kohrs, C., Angenstein, N., & Brechmann, A. (2016). Delays in human-computer interaction and their effects on brain activity. PLOS ONE, 11(1), Article e0146250. https://doi.org/10.1371/ journal.pone.0146250

Lee, Chen, & Ilie. (2012). Can online wait be managed? The effect of filler interfaces and presentation modes on perceived waiting time online. MIS Quarterly, 36(2), 365. https://doi.org 10.2307/41703460

Lee, S.-H., & Dan, Y. (2012). Neuromodulation of brain states. Neuron, 76(1), 209-222. https://doi.org/10.1016/j.neuron.2012. 09.012

Lee, Y., Chen, A., & Hess, T. (2017). The online waiting experience: Using temporal information and distractors to make online waits feel shorter. Journal of the Association for Information Systems, 18(3), 231-263. https://doi.org/10.17705/1jais.00452

Leidner, D. E., & Elam, J. J. (1993). Executive information systems: Their impact on executive decision making. Journal of Management Information Systems, 10(3), 139-155.

Leidner, D. E., & Elam, J. J. (1995). The impact of executive information systems on organizational design, intelligence, and decision making. Organization Science, 6(6), 645-664. https://doi.org/10.1287/orsc.6.6.645

Li, L., Miller, E. K., & Desimone, R. (1993). The representation of stimulus familiarity in anterior inferior temporal cortex. Journal of Neurophysiology, 69(6), 1918-1929. https://doi.org/10.1152/ jn.1993.69.6.1918

Mital, M. (2014). Zero patience, zero wait: The new customer reality. E-Commerce Times. https://www.crmbuyer.com/story/80474. html

Monsell, S. (2003). Task switching. Trends in Cognitive Sciences, 7(3), 134-140. https://doi.org/10.1016/S1364-6613(03)00028-7

Nah, F. F.-H. (2004). A study on tolerable waiting time: How long are web users willing to wait? Behaviour & Information Technology, 23(3), 153-163. https://doi.org/10.1080/0144929 0410001669914

Otto, A. R., & Daw, N. D. (2019). The opportunity cost of time modulates cognitive effort. Neuropsychologia, 123, 92-105. https://doi.org/10.1016/j.neuropsychologia.2018.05.006

Parmar, H., Nutter, B., Long, R., Antani, S., & Mitra, S. (2021). Visualizing temporal brain-state changes for fMRI using tdistributed stochastic neighbor embedding. Journal of Medical Imaging, 8(4), Article 046001. https://doi.org/10.1117/1.JMI. 8.4.046001

Parmar, H. S., Mitra, S., Nutter, B., Long, R., & Antani, S. (2020). Visualization and detection of changes in brain states using t-SNE. In Proceedings of the IEEE Southwest Symposium on Image Analysis and Interpretation. https://doi.org/10.1109/ SSIAI49293.2020.9094599

Patel, N. (2020). How loading time affects your bottom line. NEILPATEL. https://neilpatel.com/blog/loading-time/

Polman, E., & Vohs, K. D. (2016). Decision fatigue, choosing for others, and self-construal. Social Psychological and Personality Science, 7(5), 471-478. https://doi.org/10.1177/19485506 16639648

Rachakonda, S., Egolf, E., Correa, N., & Calhoun, V. (2007). Group ICA of fMRI toolbox (GIFT) Manual (Dostupnez [cit 2011-11- 5]) [Computer software].

Raichle, M. E., MacLeod, A. M., Snyder, A. Z., Powers, W. J., Gusnard, D. A., & Shulman, G. L. (2001). A default mode of brain function. In Proceedings of the National Academy of Sciences, 98(2), 676-682. https://doi.org/10.1073/pnas.98.2.676

Riedl, R., & Fischer, T. (2018). System response time as a stressor in a digital world: Literature review and theoretical model. In F. F.- H. Nah & K. Siau (Eds.), HCI in Business, Government, and Organizations (pp. 175-186). Springer. https://doi.org/10.1007/ 978-3-319-91716-0\_14

Rogers, R. D., & Monsell, S. (1995). Costs of a predictible switch between simple cognitive tasks. Journal of Experimental Psychology: General, 124(2), 207-231. https://doi.org/10.1037/ 0096-3445.124.2.207

Sakai, K. (2008). Task set and prefrontal cortex. Annual Review of Neuroscience, 31(1), 219-245. https://doi.org/10.1146/annurev. neuro.31.060407.125642

Scheil, J., & Kleinsorge, T. (2022). No-go trials in task switching: Effects on the task-set and task-space level. Psychological Research, 86(4), 1097-1107. https://doi.org/10.1007/s00426- 021-01566-7

Selvidge, P. R., Chaparro, B. S., & Bender, G. T. (2002). The world wide wait: Efects of delays on user performance. International Journal of Industrial Ergonomics, 29(1), 15-20.

Sjåstad, H., & Baumeister, R. F. (2018). The Future and the will: Planning requires self-control, and ego depletion leads to planning aversion. Journal of Experimental Social Psychology, 76, 127-141. https://doi.org/10.1016/j.jesp.2018.01.005

Squire, L. R., Ojemann, J. G., Miezin, F. M., Petersen, S. E., Videen, T. O., & Raichle, M. E. (1992). Activation of the hippocampus in normal humans: A functional anatomical study of memory. Proceedings of the National Academy of Sciences, 89(5), 1837- 1841. https://doi.org/10.1073/pnas.89.5.1837

Sridharan, D., Levitin, D. J., & Menon, V. (2008). A critical role for the right fronto-insular cortex in switching between centralexecutive and default-mode networks. Proceedings of the National Academy of Sciences, 105(34), 12569-12574. https://doi.org/10.1073/pnas.0800005105

Tang, Y.-Y., Rothbart, M. K., & Posner, M. I. (2012). Neural correlates of establishing, maintaining, and switching brain states. Trends in Cognitive Sciences, 16(6), 330-337. https://doi.org/10.1016/j.tics.2012.05.001

Tingley, D., Yamamoto, T., Hirose, K., Keele, L., & Imai, K. (2014). Mediation: R package for causal mediation analysis. Journal of Statistical Software, 59(5). https://doi.org/10.18637/jss.v059.i05

Weissman, D. H., Roberts, K. C., Visscher, K. M., & Woldorff, M. G. (2006). The neural bases of momentary lapses in attention. Nature Neuroscience, 9(7), 971-978. https://doi.org/10.1038 nn1727

Whetten, D. A. (1989). What constitutes a theoretical contribution? The Academy of Management Review, 14(4), 490-495.

Wig, G. S., Grafton, S. T., Demos, K. E., & Kelley, W. M. (2005). Reductions in neural activity underlie behavioral components of repetition priming. Nature Neuroscience, 8(9), 1228-1233. https://doi.org/10.1038/nn1515

Willems, R. M., der Haegen, L. V., Fisher, S. E., & Francks, C. (2014). On the other hand: Including left-handers in cognitive neuroscience and neurogenetics. Nature Reviews Neuroscience, 15(3), Article 3. https://doi.org/10.1038/nrn3679

Xiao & Benbasat. (2007). E-commerce product recommendation agents: Use, characteristics, and impact. MIS Quarterly, 31(1), 137-209. https://doi.org/10.2307/25148784

Young, M. E., Sutherland, S. C., & McCoy, A. W. (2018). Optimal go/no-go ratios to maximize false alarms. Behavior Research Methods, 50(3), 1020-1029. https://doi.org/10.3758/s13428-017- 0923-5

## About the Authors

Kevin A. Harmon is an assistant professor of information systems at the Sam M. Walton College of Business at the University of Arkansas. His research areas include user experience and performance, system delays, user emotions, and the gender gap in information technology careers. His work has appeared in journals including the Journal of the Association for Information Systems, Psychology of Men & Masculinity, Current Psychology, and Journal of American College Health. He is a member of the Association for Information Systems. He teaches Business Analytics and Quantitative Methods at the Walton College of Business. He received his Ph.D. from Texas Tech University. ORCiD: 0000-0003-2522-0491

Hansol Lee is a Ph.D. candidate in the Rawls College of Business at Texas Tech University. Her research areas include big data and machine learning, the societal impacts of information technology, and the impacts of emerging technological platforms. She teaches business intelligence at Rawls College of Business.

Bahar Javadi Khasraghi is a Ph.D. student in the Rawls College of Business at Texas Tech University. Her research areas include AI agents, knowledge sharing, system delays, crowdsourcing, and the gender gap in the information technology workforce. She teaches analytics and development with Python and data base management at Rawl College of Business.

Harshit S. Parmar is a research scientist at the Neuroimaging Institute at Texas Tech University. His research includes the application and development of machine learning and AI algorithms for biomedical data/signals/images. His work has appeared in journals including Journal of Medical Imaging, PLOS ONE, International Journal of Information Management, and Brain Science. He teaches undergraduate courses in the Department of Electrical and Computer Engineering at Texas Tech University. He received his Ph.D. from Texas Tech University. ORCiD: 0000- 0003-1506-6873

Eric A. Walden is the Rawls Chair in the Rawls College of Business and the Director of the Texas Tech Neuroimaging Institute at Texas Tech University. He researches whatever seems to need researching. His papers have appeared in Harvard Business Review, Neuroimage, MIS Quarterly, Journal of the Association for Information Systems, Information Systems Research, PLOS One, Brain Science, Journal of Hospitality and Tourism Research, Real Estate Economics, Algorithms, and other outlets. He received his Ph.D. from The University of Minnesota. ORCiD: 0000-0003- 2154-9257

## Appendix A

## t-Distributed Stochastic Neighbor Embedding (t-SNE)

A simplified view of the t-SNE process is shown in Figure A1. The first step is to compute a pairwise neighborhood matrix in the origina dimensionality space (NMO). The neighborhood matrix is computed by calculating the pairwise distance between each pair of data points in the original dimensionality space. For N datapoints, the size of NMO will be $\mathrm { \tilde { \Delta N } } \times \mathrm { N } . \mathrm { \tilde { \Delta } }$ Some commonly used distance measures include Euclidean, correlation, cosine, and Mahalanobis. The NMO is used as a target for the dimensionality reduction process. The next step is to randomly sample the same number of data points from a t-distribution in the lower dimensional space (usually 2 or 3). The neighborhood matrix is then computed using the reduced dimensional data (NMR). The size of NMR is also $\mathrm { { ^ { 6 } N } \times N . { ^ { , } } }$ Finally, similarity is computed between NMO and NMR. If they are not similar, then the difference between both matrices is used to update the random sampling. Again, NMR is computed with updated samples and this process is repeated until NMO and NMR are similar to each other. Being similar means that samples in the reduced dimensionality space have the same adjacency structure as the data in the original dimensionality space.

![](/api/attachments/5EK37EAS/fulltext/images/d121e45aa66d3cbe258ef80121c618611950d2a1323d6f8feb9b222c7bb1d39b.jpg)

Figure A1. Simplified View of the t-SNE Process

Group independent components analysis (ICA) analysis was performed on the preprocessed fMRI data for all the participants. The Group ICA fMRI Toolbox (GIFT) was used for ICA analysis with the number of components set to 50 (Rachakonda et al., 2007). The GIFT outputs spatial maps and time series corresponding to each component for all participants. The time series for all the components are combined in a 2D matrix of size $\mathrm { T } \times 5 0 .$ , with each column corresponding to one independent component and each row corresponding to a time point. Such components time series matrix is obtained for each participant. Figure A2 shows the graphical representation of the 2D matrix. From the entire 2D matrix, a small time window of length 256 time points is given as an input to the t-SNE algorithm. The t-SNE algorithm reduces the size of the matrix from $2 5 6 \times 5 0 ~ \mathrm { t o } ~ 2 5 6 \times 2 .$ Each row in the reduced dimensional matrix corresponds to a 2-dimensional point in the t-SNE space. A step distance plot is then generated by computing the distance between temporally adjacent time points in the t-SNE space. This entire process is visualized in Figure A2 by black arrows. The time window is then moved forward in time by 16 time points and the process is repeated until the last time window. The shifting of time windows is shown graphically with red and blue curly brackets. The windowed step distance plots from all the time windows are combined by averaging to form the step distance plot over the entire time duration. The step distance plot over the entire duration is indicated by the green step distance plot on the very right in Figure A2. Averaging will only retain the consistent peaks and get rid of any peaks obtained due to noise or instabilities in the t-SNE algorithm. In Figure A2, notice how the consistent peaks are retained while inconsistent peaks (second blue peak) are reduced in size. The t-SNE algorithm is applied independently to each participant’s independent components to obtain subject-wise step distance plots. These step distance plots are in turn used to identify brain state changes at the single-subject level.

![](/api/attachments/5EK37EAS/fulltext/images/2c296b8f5e1fd5451a3a4ad67a11fec5028f2b14bbdb5d83c84f17cf114bd7d7.jpg)  
Figure A2. Graphical Representation of the Windowed t-SNE Process

The t-SNE algorithm is described in detail in (van der Maaten & Hinton, 2008). However, one point does need to be made. The t-SNE algorithm relies on the subjective choice of a perplexity parameter. While it is fairly robust to a range of perplexity measures, it is still a subjective choice with implications. In particular, this measure changes the sensitivity of the model to brain state switches. This is important because at one extreme of sensitivity the brain will change states every time we measure it, and on the other it will change once, upon the death of an organism. As a practical matter, fMRI brain state data are noisy because they detect too much information. For example, in this experiment when presented with an app for ordering flowers, a participant may be reminded that Mother’s Day is in a few days and they need to get a present. Presumably, this would not require the same pattern of brain activation as evaluating the satisfaction that using an app would result in. More specifically, every new app will have some set of idiosyncratic associated activity, which could be considered a brain state switching. The t-SNE algorithm helps us avoid detecting these smaller changes. We deal with this by trying several different subjective parameters, and they all give similar results. If we are very sensitive to brain state switches, we find more of them during and following long delays than during and following short delays. If we are only slightly sensitive to brain state switches, we still find more during and following long delays than during and following short delays.

## Appendix B

<table><tr><td colspan="7">Table B1. Intervention Study Participant Demographics</td></tr><tr><td>Condition</td><td>Short delay</td><td>Long delay</td><td>Simultaneous performance display</td><td>Gradual performance display</td><td>Countdown timer</td><td>Dummy task</td></tr><tr><td>Age: M(SD)</td><td>29.89(10.63)</td><td>29.17(9.32)</td><td>28.50(9.12)</td><td>28.22(6.92)</td><td>33.39(11.68)</td><td>38.47(13.72)</td></tr><tr><td>Female</td><td>59.52%</td><td>60.19%</td><td>68.70%</td><td>67.96%</td><td>78.18%</td><td>74.55%</td></tr><tr><td>Male</td><td>34.92%</td><td>35.92%</td><td>27.83%</td><td>28.16%</td><td>17.27%</td><td>20.91%</td></tr><tr><td>Non-binary</td><td>2.38%</td><td>1.94%</td><td>2.61%</td><td>2.91%</td><td>2.72%</td><td>0%</td></tr><tr><td>Transgender</td><td>0.79%</td><td>0%</td><td>0.87%</td><td>0.97%</td><td>0.91%</td><td>1.81%</td></tr><tr><td>Genderqueer</td><td>0.79%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Other</td><td>1.59%</td><td>1.94%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Prefer not to answer</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0.91%</td><td>2.73%</td></tr><tr><td>White/European American</td><td>69.05%</td><td>72.82%</td><td>65.22%</td><td>72.82%</td><td>73.64%</td><td>73.64%</td></tr><tr><td>Asian/Asian American</td><td>8.73%</td><td>6.80%</td><td>9.57%</td><td>3.88%</td><td>3.64%</td><td>8.18%</td></tr><tr><td>Hispanic/Latino</td><td>7.94%</td><td>5.83%</td><td>12.17%</td><td>9.71%</td><td>7.27%</td><td>6.36%</td></tr><tr><td>African American/Black</td><td>7.14%</td><td>5.83%</td><td>5.22%</td><td>6.80%</td><td>1.82%</td><td>4.55%</td></tr><tr><td>Biracial/Multiracial</td><td>5.56%</td><td>6.80%</td><td>3.48%</td><td>3.88%</td><td>7.27%</td><td>2.73%</td></tr><tr><td>Asian Indian</td><td>1.59%</td><td>0.97%</td><td>2.61%</td><td>0%</td><td>0%</td><td>1.82%</td></tr><tr><td>American Indian/Native American</td><td>0%</td><td>0.97%</td><td>0%</td><td>0.97%</td><td>1.82%</td><td>0%</td></tr><tr><td>Middle Eastern</td><td>0%</td><td>0%</td><td>0.87%</td><td>0.97%</td><td>0.91%</td><td>0%</td></tr><tr><td>Other</td><td>0%</td><td>0%</td><td>0%</td><td>0.97%</td><td>1.82%</td><td>0.91%</td></tr><tr><td>Prefer not to answer</td><td>0%</td><td>0%</td><td>0.87%</td><td>0%</td><td>1.82%</td><td>1.82%</td></tr></table>
