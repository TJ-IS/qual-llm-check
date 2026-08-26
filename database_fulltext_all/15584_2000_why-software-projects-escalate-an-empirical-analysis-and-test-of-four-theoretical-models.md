---
otero_id: 15584
otero_key: "65Z8FQWP"
title: "WHY SOFTWARE PROJECTS ESCALATE: AN EMPIRICAL ANALYSIS AND TEST OF FOUR THEORETICAL MODELS"
authors: "Mark Keil; Joan Mann; Arun Rai"
year: "2000"
journal: "MIS Quarterly"
doi: "10.2307/3250950"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# WHY SOFTWARE PROJECTS ESCALATE: AN EMPIRICAL ANALYSIS AND TEST OF FOUR THEORETICAL MODELS<sup>1,</sup> <sup>2</sup>

By: Mark Keil Department of Computer Information Systems J. Mack Robinson College of Business Georgia State University P. O. Box 4015 Atlanta, GA 30302-4015 U.S.A. mkeil@gsu.edu

Joan Mann MIS/DS College of Business and Public Administration Old Dominion University Hughes 2096 Norfolk, VA U.S.A. jmann@odu.edu

Arun Rai Electronic Commerce Institute J. Mack Robinson College of Business Georgia State University Atlanta, GA 30303 U.S.A. arunrai@gsu.edu

## Abstract

Software projects can often spiral out of control to become ìrunaway systemsî that far exceed original budget and schedule projections. The behavior that underlies many runaway systems can best be characterized as ìescalation of commitment to a failing course of action.î The objectives of this study were to: (1) understand the extent to which IS projects are prone to escalate, (2) compare the outcomes of projects that escalate with those that do not, and (3) test whether constructs associated with different theories of escalation can be used to discriminate between projects that escalate and those that do not. A survey was administered to IS audit and control professionals and, to establish a baseline for comparison, the survey was designed to gather data on projects that did not escalate as well as those that did escalate.

The results of our research suggest that between 30% and 40% of all IS projects exhibit some degree of escalation. Projects that escalated had project outcomes that were significantly worse in terms of perceived implementation performance and perceived budget/schedule performance, as compared to projects that did not escalate. Using constructs from theories that have been used to explain the escalation phenomenon, we were able to test various logistic regression models for their ability to discriminate between projects that escalate and those that do not. To construct our models, we explored constructs derived from selfjustification theory, prospect theory, agency theory, and approach avoidance theory. While constructs derived from all four theories were significant in logistic regression models, the completion effect construct derived from approach avoidance theory provided the best classification of projects, correctly classifying over 70% of both escalated and non-escalated projects.

Keywords: Software project management, escalation, IS project failure

ISRL Categories: EE, EE01, EE101, EE06, EL0202

## Introduction

The reported statistics on information systems (IS) projects are bleak: by most accounts at least one in four projects ends in failure. Entire books are now available filled with cases of software project failure (see, for example, Flowers 1996; Glass 1998, 1999). In 1995, the Standish Group reported the results of a study of over 8,000 software development projects, revealing that only 16% were completed on time and on budget (Johnson 1995). Most of the remaining projects, if they were completed at all, came in over budget and behind schedule, with fewer functions and features than originally specified. Cost overruns for these projects averaged nearly 200%. Cases in which software projects go wildly over budget or drag on long past their originally scheduled completion date have been labeled ìrunaway systemsî in the trade press (Mehler 1991; Willbern 1989). Like a runaway train, these are projects that are hurtling out of control; difficult to stop, yet in need of redirection or termination.

The behavior that underlies many runaway systems resembles ìescalation of commitment to a failing course of actionî (Brockner 1992), a phenomenon that has been documented in the management literature and recently applied to the domain of software project management (Drummond 1996; Keil 1995; Keil et al. 1995a; Newman and Sabherwal 1996). Consider the following example:

In 1992, Californiaís Department of Social Services (DSS) began a project to develop a Statewide Automated Child Support System (SACSS). The development work was contracted out to Lockheed Martin under a \$75.5 million contract and scheduled to be completed by September 1995. Though the project quickly became plagued by cost overruns, a flawed procurement process, and political struggles, the stateís Department of Information Technology continued the project as though nothing was the matter all the way up until 1997. Finally, in April 1997, the California Assembly Information Technology Committee issued its oversight report on the project asking: ìHow bad does a particular project need to become before the stateís information technology czar considers termination?î Eventually, in November 1997, the SACSS project was cancelled by John Thomas Flynn, Californiaís chief information officer, after more than five years of work and direct expenditures of \$100 million. Final costs were estimated to be as high as \$345 million. (Newcombe 1998)

One purpose of this research study was to ascertain the frequency of software project escalation and the duration of escalation when it does occur. Whether we should be terribly concerned about cases such as the one just described depends upon the frequency of such events. There are some who would argue that software runaways are rare events in our field, but that when they do occur they are highly visible (Glass 1997). For every case of project escalation, they would argue that there are numerous cases of project success that go unnoticed. From this perspective, cases of software project escalation are seen as the exception, rather than the rule. If this perspective is true, examples such as Californiaís SACSS project should not be of great concern to either researchers or practitioners. However, a counter view might suggest that escalation occurs far more frequently than it makes the headlines, a natural consequence of the fact that companies and managers do not wish to advertise their project failures. Under this view, well-publicized examples such as the one above may represent the tip of the iceberg, in which case the problem of project escalation deserves the attention of both researchers and practitioners. To date, only a handful of case studies have been published on software project escalation (Drummond 1996; Kei 1995; Newman and Sabherwal 1996). Thus, there is no solid information concerning the actual frequency of this phenomenon or the impact that it has on project outcomes.

A second purpose of the study was to determine if escalation was associated with negative project outcomes. It is possible, for example, that escalationówhile it may represent a waste of organizational resourcesóleads to project outcomes that are not significantly worse than the outcomes observed among projects that do not escalate. In order to answer this question, though, one would need access to a sample of both escalated and non-escalated projects for comparison purposes.

Finally, knowing that some fraction of software projects undergo escalation, it would be useful to determine if central constructs from the most common theories of escalation behavior can be used to distinguish projects that escalate from those that do not. Such knowledge could potentially be of great benefit not only to researchers, but also to practitioners who must make resource allocation decisions on such projects. While several theories have been put forth to explain escalation behavior, there has been no attempt to determine if the constructs associated with these theories can be used to discriminate between projects that escalate and those that do not. Thus, the third objective of this study was to test different models of escalation by operationalizing specific constructs derived from different theories of escalation.

To summarize, our study was designed to answer three basic research questions:

1. What is the frequency and duration of software project escalation?

2. How do projects that escalate differ from projects that do not escalate in terms of project performance?

3. Can constructs associated with different theories of escalation be used to create models capable of distinguishing between projects that escalate and those that do not?

The first two questions are descriptive in nature while the third question, which is our primary focus here, is of a more theoretical nature.

The remainder of this paper is organized into four sections. First, we discuss the concept of escalating commitment and its application to software projects, focusing our literature review around four theories that have been used to explain the escalation phenomenon. From each theory, we derive one or more constructs that are later operationalized in an attempt to determine if they can be used to distinguish between projects that escalate and those that do not. Next, we describe the approach used to address the above research questions. Finally, we present our findings and conclude the paper with a short discussion of their implications for research and practice.

## Background and Literature Review

Escalation occurs when troubled projects are continued instead of being abandoned or redirected. Several researchers have applied the concept of escalation to the domain of software project management (Drummond 1996; Keil 1995; Keil et al. 1995a; Newman and Sabherwal 1996). While escalation is most frequently thought of as a ìbadî thing, it should be noted that there may be cases in which escalation is warranted (see, for example, Keil and Flatto 1999). In this paper, however, we focus on cases in which escalation, as judged through the eyes of a trained professionalóan IS auditoróis unwarranted.

Central to the concept of escalation is the notion of negative project status (Brockner 1992). In the context of software project escalation, negative project status refers to significant performance problems in one or more of the following areas: cost, schedule, functionality, or quality. For a variety of reasons, these performance problems may or may not be visible to the key decision maker responsible for the decision of whether or not to continue the project.

Traditionally, escalation has been defined as continued commitment to a previously chosen course of action in spite of negative feedback concerning the viability of that course of action. In order to have escalation under this definition, one might reasonably infer that the decision maker responsible for continuing a project must be aware of the negative project status. Within the escalation literature, however, this point is not well addressed and thus the definition of what constitutes escalation is subject to some debate and interpretation. In this paper, we address this issue by explicitly defining escalation in unambiguous terms that can then be more easily operationalized in a field setting.

The definitional issue associated with escalation is akin to the question: ìIf a tree falls in the forest and nobody hears it fall, does it still make a sound?î In some cases, negative project status information is present, but may not be available to those in a position to terminate or redirect the project. One reason for this is that individuals in the organization may conceal negative information from their superiors, thereby promoting the escalation process through what has been referred to as the ìmum effect.î In other cases, superiors are aware of negative information but choose to ignore it (or discount it heavily) due to certain cognitive biases, thereby promoting escalation through what has been referred to as the ìdeaf effectî (Keil and Robey 1999). Whether it results from the mum effect or the deaf effect (or some combination of the two), escalation can be said to occur within an organization when there is a presence of negative project status information that fails to be processed appropriately, resulting in continuation of what appears to be a failing course of action. Under this definition, it is not necessary that the decision maker be aware of negative project status. In other words, escalation can occur either because the project status information is biased, or is not available, or because it is not attended to and interpreted correctly.

Once escalation is recognized, the decision maker can take steps to de-escalate a troubled project by either terminating it or redirecting the project along some new course of action (e.g., redefining the project or breaking off a more manageable piece of the project on which to focus). Under this conceptualization, redirection represents a form of deescalation in the sense that it constitutes a reduction in commitment vis-‡-vis the previously chosen course of action.

## Theories to Explain Escalation Behavior

The escalation literature provides a solid theoretical base for explaining commitment to failing courses of action and may, therefore, shed light on runaway systems projects. Within the escalation literature, several different theories have been proposed to explain the phenomenon including self-justification theory (SJT), prospect theory (PT), agency theory (AT), and approach avoidance theory (AAT). We focus on these particular theories because they are among the most frequently invoked theories used to explain escalation.

## Self-Justification Theory

Grounded in Festinger's (1957) theory of cognitive dissonance, self-justification theory (SJT) posits that individuals tend to escalate their commitment to a course of action (and undergo the risk of additional negative outcomes) in order to selfjustify prior behavior (Staw and Fox 1977). SJT is based on the notion that ìindividuals seek to rationalize their previous behavior...against a perceived error in judgement" (Staw and Fox 1977, p. 432). Under SJT, escalation behavior is seen as arising from a kind of ìretrospective rationalityî whereby costs or losses that have been incurred in the past are considered relevant to decision making. Under retrospective rationality, the decision maker feels compelled to justify his actions in order to prove to himself (psychological self-justification) and to others (social selfjustification) that he is competent and rational. According to Whyte (1986, p. 313), ìit is this need to demonstrate rationality which is seen to activate behavior that runs counter to commonly accepted notions of rationality.î

Central to the concept of psychological selfjustification is the notion of personal responsibility (Staw 1976). Presumably, a decision maker with a high degree of personal responsibility for a previously chosen course of action will feel a greater need to justify the initial resource allocation decision and will, therefore, be more likely to engage in psychological self-justification (Brockner 1992). Using a role-playing methodology, Staw measured the effect of personal responsibility on subjects' willingness to allocate resources between two divisions of a hypothetical corporation. He found that subjects' allocation of resources toward a previously chosen alternative was greatest under conditions of high personal responsibility (for the previous investment decision). Staw's early work in this area represents the first and most frequently cited article invoking SJT to explain escalation behavior.

Since the mid-1970s when SJT was first proposed, there has been a steady stream of publications that have invoked or extended the theory to explain certain aspects of escalating commitment. The resulting body of literature associated with SJT now suggests that the psychological processes that underlie the need for self-justification can be reinforced by certain socia factors. As Staw and Ross (1987, p. 55) observe, ìone social determinant of commitment is the desire not to lose face or credibility with others.î In other words, it is now believed that socia pressures can heighten self-justification, leading to the need for social (or external) self-justification of a prior course of action in order to save face.

It should be noted that there have been some studies (e.g., Armstrong et al. 1993; Singer and

Singer 1985) that have failed to find escalation when attempting to create conditions very similar to Stawís classic escalation experiment in which self-justification theory was first postulated. Thus, in recent years researchers have advanced alternative theories to explain the phenomenon (Brockner 1992).

## Prospect Theory

Whyte (1986) has suggested that prospect theory may offer a better explanation for escalating commitment than SJT. Prospect theory (Kahneman and Tversky 1979; Tversky and Kahneman 1981), provides a framework for understanding the cognitive biases that influence human decision making under conditions of risk and uncertainty. Prospect theory posits that individuals exhibit risk averse or risk seeking behavior depending on how a problem is framed. Specifically, prospect theory suggests that individuals will exhibit risk seeking behavior in choosing between two negative alternatives, especially when the choice is between a sure lossóthe initial loss on the investmentóand the possibility of a larger loss combined with a chance to return to the reference point (Whyte 1986). In other words, someone who has not yet come to terms with an earlier loss is likely to adopt a negative frame of reference and is, therefore, more likely to engage in risk seeking behavior.

According to Whyte, the critical distinction between SJT and prospect theory is the role ascribed to personal responsibility in fostering commitment.

An approach based on self-justification theory would suggest that escalating commitment should not occur without a degree of culpability on the part of the decision maker for the initial failed outcomes. A prospect theory based analysis implies otherwise. A tendency towards entrapment should be observed whenever future choices can reasonably be framed as choices between losses, as after a series of failures. Personal responsibility is not a prerequisite of such a frame, although it may be a contributing element. (Whyte 1986, p. 319).

Whyte has suggested that prospect theory could explain the so-called sunk cost effect in which decision makers exhibit a tendency to "throw good money after bad." In particular, he suggests that sunk costs may influence decision makers to adopt a negative frame, thereby promoting risk seeking behavior which can be observed as escalating commitment to a failing course of action.

In a series of laboratory experiments, Garland and his colleagues (1990; Garland and Newport 1991) have documented the influence of sunk costs on decisions to abandon or continue a prior course of action. The results of these experiments were judged to be consistent with a prospect theory interpretation of escalation. It should be noted, however, that Garland and his colleagues did not control for the effect of personal responsibility in these experiments.

## Agency Theory

Jensen and Meckling define the concept of an agency relationship as ìa contract under which one or more persons (the principal(s)) engage another person (the agent) to perform some service on their behalf which involves delegating some decision making authority to the agentî (1976, p. 308). Under agency theory, goal incongruency between principal and agent can create a situation in which the agent acts to maximize his or her own utility, rather than acting in the best interests of the principal. The concept of information asymmetry is central to all principal-agent modelsóìthe agent is assumed to have private information to which the principal cannot costlessly gain accessî (Baiman 1990, p. 343). Finally, agents are generally presumed to be work-averse or risk-averse (Baiman 1990). The combination of information asymmetry and the agentís work or risk aversion is what typically allows self-interested behavior to emerge.

While various monitoring and bonding mechanisms can be used to reduce conflicts between principals and agents, these mechanisms are generally imperfect and costly to implement.<sup>3</sup>

Thus, one of the chief concerns of agency theorists is the so-called agency problem that arises when the goals of the principal and agent conflict and when it is expensive or impractical for the principal to monitor the behavior of the agent.

Agency relationships can exist between the owners of a firm and its senior management, but they can also exist between different levels within a firmís hierarchy. The agency problem is quite general and it ìexists in all organizations and in all cooperative effortsóat every level of management in firmsî (Jensen and Meckling 1986, p. 218). The agency problem within a firmís hierarchy is exacerbated by the fact that the firmís top executives frequently hold a significant amount of stock whereas those lower in the hierarchy may hold little, if any, stock (Scholes 1991). Motivated by their own self-interest, agents will ìmake themselves better off by deviating from their cooperative behaviorî which maximizes the firmís welfare (Baiman 1990, p. 342).

Harrison and Harrell (1993) have suggested agency theory as an alternative theoretical perspective from which to view the phenomenon of escalating commitment. They explain the application of agency theory to the problem of escalation as follows:

When an agent has private information about the projected future performance of a project, the principal is unable to completely monitor the agent's actions, and information asymmetry prevails. Here, the potential for goal conflict between the principal and agent arises. If, for instance, an agent's reputation was hurt by a decision to discontinue a project he or she had started, the event would negatively affect the agent's future career opportunities, thus providing an incentive to shirk. In this situation, agents are expected to reach decisions that maximize their self-interest at the expense of the principal's interests. (Harrison and Harrell 1993, pp. 636-637).

In a laboratory experiment, Harrison and Harrel demonstrated that subjects were more likely to continue with a questionable project when they were manipulated to believe that they possessed private information about the projectís prospects for success and that a decision to discontinue a project would damage their reputation and be potentially harmful to their career. These findings were interpreted to be consistent with an agency theory view of escalation. Subsequent studies have yielded similar results (Harrell and Harrison 1994; Tuttle et al. 1997).

Harrison and Harrellís application of agency theory to the problem of escalating commitment to a failing course of action appears to be theoretically sound and may be of particular salience in a software project management context. Logically, a risk averse agent in this context (e.g., the software project manager) whose actions are not observable will report good news, but will only report bad news if necessary, since bad news is more likely to get the agent fired than good news. Any bad news that is reported could be the result of either bad luck or shirking on the part of the agent. A rational executive would not fire a person who achieved a negative result because of chance alone. However, because of imperfect monitoring, the principal cannot tell the difference between lack of effort on the part of the agent and bad luck. Thus, the agency problem that promotes escalation behavior will exist within organizations because the principle cannot observe with certainty the actions and work effort of the agent.

To summarize, the source of the goal incongruency between principle and agent arises from the fact that the agent can get fired or suffer other negative impacts to his/her reputation or career simply for delivering bad news. The agency problem described here may be quite likely to occur in a software project context because such projects are notoriously difficult to monitor and contro (DeMarco 1982). What is more, the intangible, or invisible, nature of software itself (Abdel-Hamid and Madnick 1991) contributes to the problems of incomplete contracting and imperfect monitoring which give rise to the agency problem.

## Approach Avoidance Theory

Escalation situations can be viewed as instances of approach avoidance conflict (Rubin and Brockner 1975). Under approach avoidance theory, escalation is conceptualized as a behavior that results when driving forces that encourage persistence seem to outweigh restraining forces that encourage abandonment (Brockner and Rubin 1985). These competing forces create a conflict over whether to continue or withdraw (Mann 1996). According to approach avoidance theory, in escalation situations, the cost of persistence (a restraining force) is often overshadowed by one or more driving forces such as: (1) the size of the reward for goal attainment, (2) the cost of withdrawal, or (3) the proximity to the goal.

Derived from approach avoidance theory, the completion effect reflects the notion that the ìmotivation to achieve a goal increases as an individual gets closer to that goalî (Conlon and Garland 1993, p. 403). The completion effect is consistent with psychological research suggesting that the desire to achieve task closure, or completion, can have a significant influence on behavior (Katz and Kahn 1966). This view is also consistent with early work on escalation conducted by Brockner et al. (1979, p. 194), who observed that an individualís motivation for pursuing a course of action may shift over time ìdue in part to the presumed increased proximity to the goal.î Results from a series of experiments appear to provide support for the completion effect (Conlon and Garland 1993; Garland and Conlon 1998). Conlon and Garland suggest that the motivation to complete a task that has already been started and is perceived to be near completion can, in itself, bring about escalation behavior through a form of goal substitution.

Conlon and Garland go so far as to suggest that escalation behavior and what has been previously characterized as the sunk cost effect may be motivated by what they term the completion effect.

Noting that ìthere may be a strong positive correlation between sunk costs and project completion in many instances,î Conlon and Garland (p. 403) point out that they are two ìtheoretically different concepts.î Mann (1996) suggests that goal proximity, or the completion effect, represents ìa pull on the individualî because ìit relates to benefits to be received in the futureî (p. 46). The sunk cost effect, which is grounded in prospect theory, is ìmore concerned with how past behavior pushes the individual to proceedî (Mann 1996, p. 46).

Prior empirical work by Conlon and Garland suggests that the completion effect (associated with approach avoidance theory) may have a more pronounced impact on escalation behavior than does the sunk cost effect (associated with prospect theory). Work by Keil et al. (1995b), however, suggests the opposite. Because this matter remains unresolved in the literature, we included both constructs in our research.

Another rationale for including the completion effect is that it may be particularly germane to software projects, which frequently exhibit the socalled ì90% completeî syndrome (Abdel-Hamid 1988; DeMarco 1982). This syndrome refers to the tendency for estimates of work completed to increase steadily until a plateau of 90% is reached. Thereafter, programmer estimates of the fraction of work completed increase very slowly. In some cases, inaccurate estimation leads to situations in which software projects are reported to be 90% complete for half of the entire duration of the project, an obvious impossibility (Brooks 1975). This syndrome may promote escalation behavior by creating the impression that project completion is close at hand, even when it is not. Measuring the completion level of any medium to large sized software project is extremely difficult and, therefore, one of the reasons for escalation is lack of information about the true status of the project, leading to a false perception that the project is close to completion.

## Summarizing the Theories and the Constructs Derived

Table 1 compares the four theories just discussed and indicates the key constructs that were derived from each of these theories. We shall return to these later in the paper when we discuss the approach taken for model building.

## Research Method

In order to address our research questions, a cross-sectional survey of information systems audit and control professionals was used to collect information on both escalated projects and nonescalated projects. IS auditors were chosen for study because of their role in monitoring software projects. Auditors are a preferred source of information about troubled software projects because they are likely to be more objective than IS managers or project team members. Project managers or project sponsors, for example, would likely be reluctant to discuss escalation on projects with which they have been associated. Moreover, any information that they might provide would be subject to possible bias.

The sampling design used in this study was to select a sample of Information Systems Audit and Control Association (ISACA) members in the U.S. who would be most likely to be involved in information systems development. Toward this end, the study was focused on internal and external IS auditors. An internal auditor is one that is employed by the firm (usually reporting to the audit department). An external auditor is one that is hired by firms as an outside consultant to perform certain auditing tasks. Using the ISACA membership database, which contains selfreported job category information, we were able to limit the pool of potential participants to those individuals who were likely to have the greatest exposure to information systems development projects. This pool of individualsórepresenting all U.S. ISACA members who described themselves as an IS Audit Manager, IS Auditor, Internal Auditor, or External Auditoróincluded approximately 2,500 ISACA members in the U.S.

The survey instrument was designed to gather data concerning the frequency and magnitude of escalation as well as the constructs associated with each of the four theories. A mail survey, based on Dillmanís (1978) ìtotal design method,î was chosen as the most cost-effective means of collecting data on a large number of projects (Mann 1996). In order to provide a control group for comparison purposes, two different versions of the survey instrument were developed: one designed to gather information on cases of software project escalation and the other designed to gather information on projects that did not escalate. The purpose of the latter version of the survey was to provide a reference point, or baseline, to determine whether the outcomes associated with projects that escalate were significantly different from the outcomes associated with projects that did not escalate. This baseline sample also allowed us to test various models aimed at distinguishing escalated from non-escalated projects using constructs derived from different theories of escalation behavior.

<table><tr><td colspan="3">Table 1. Four Theories of Escalation and the Key Constructs Derived from Each Theory</td></tr><tr><td>Theory</td><td>How the Theory Explains Escalation</td><td>Key Construct(s) Derived from the Theorya</td></tr><tr><td>Self-justification theory (SJT).</td><td>Managers continue to commit resources to a failing course of action in order to self-justify the correctness of an earlier decision to pursue a particular course of action. The need to self-justify is both psychological and social in nature. Social pressures are hypothesized to heighten the need to self-justify, often leading to behaviors that are designed to save face.</td><td>Psychological self-justificationSocial self-justification</td></tr><tr><td>Prospect theory (PT).</td><td>Managers commit resources to a failing course of action because the decision is framed as a choice between losses which leads to risk seeking behavior.Sunk costs are believed to invoke a choice between losses which induces escalation behavior.</td><td>Sunk cost effect</td></tr><tr><td>Agency theory (AT).</td><td>Managers commit resources to a failing course of action because it is in their best interest to do so due to goal incongruency between the manager and his/her superior(s) and a condition of information asymmetry.</td><td>Goal incongruencyInformation asymmetry</td></tr><tr><td>Approach avoidance theory (AAT)</td><td>Managers commit resources to a failing project because the forces encouraging them to do so (driving forces) are stronger than those forces which suggest discontinuation (restraining forces). One of the key driving forces that can encourage escalation is the proximity to the goal, or what is sometimes labeled the completion effect.</td><td>Completion effect</td></tr></table>

<sup>a</sup>The construct(s) derived from each theory were chosen because they represented key features of the theory and because the literature has portrayed these particular constructs as being salient in the context of escalation. We make no claim to have fully operationalized each theory.

Participants who received the escalation survey were asked to select a project with which they were familiar that fit the definition of project escalation provided on the survey form (see Appendix A). Thus, for the purposes of this particular study, we limited ourselves to cases of escalation that were defined as unwarranted by a professional IS auditor. The survey was designed to allow the auditor to assess the presence or absence of certain attitudes or behaviors exhibited by the key decision maker responsible for the decision to continue the project (see Appendix B).

Under our conceptualization of escalation given earlier, it was not essential that the decision maker(s) responsible for continuation be aware of negative information. However, it was necessary to establish the presence of negative information within the organization. In our survey design, a trained professionalónamely an IS auditoró made the determination that negative information existed within the organization by identifying a troubled project which continued to received resources even though s/he thought that the project should have been discontinued or redirected.<sup>4</sup>

Participants who received the ìnon-escalationî version of the survey were asked to select a completed project that progressed smoothly enough that the respondent never thought it should be discontinued or redirected. It is important to note that the two different versions of the survey were identical except for the instructions regarding what type of project to select, thus allowing the nonescalation survey group to serve as a baseline for comparison purposes. Appendix A shows the instructions that the respondents received to help them select either an escalated or non-escalated project.

The survey was refined successively through two rounds of pre-testing, followed by a pilot study in which both versions of the survey were administered to a sample of approximately 300 IS audit and control professionals (for details, see Mann 1996). The full-scale administration involved 2,231 ISACA members and represented those individuals who met one of the four job-type categories described earlier and who had not participated in either the pre-test or pilot phases of the study. For the full-scale administration of the survey, a decision was made to split the sample 70:30 so that 70% of the participants would receive the escalation version of the survey and 30% would receive the non-escalation version of the survey. This was done to maximize the size of the escalation sub-sample while insuring an adequate number of projects in the comparison group. In all cases, the decision was random as to whether a participant received an escalation or a non-escalation survey.

## Construct Operationalization

In this section, we describe how we operationalized each of our constructs. First, the measurement items used to assess escalation frequency are described, and then the measures used to assess project performance are introduced. Next, we discuss the operationalization of the constructs derived from the different theories of escalation.

## Escalation Frequency

A series of three measurement items were designed to obtain an estimate of escalation frequency. At the beginning of this series of questions, escalation was clearly defined for the respondent as ìtroubled projects which continued to receive resources even though you thought the project should have been discontinued or redirected.î One item asked: ìOf the last five projects with which you have been associated... how many were cases of project escalation?î A second item asked: ìOf all the projects with which you have been associated during your years as an information systems control professional, what percentage would you classify as cases of project escalation?î Finally, as an additional means of triangulation, a third item asked: ìIn your judgment what percentage of all IS development projects are cases of project escalation?î

## Project Performance

Two different measures of project performance were developed: (1) a categorical measure designed to capture whether the system was ever successfully completed and if so, whether it was successfully implemented and used within the organization, and (2) whether the project was perceived as being delivered on schedule and within budget. The first we call ìperceived implementation performanceî and the second we shall refer to as ìperceived budget/scheduleî performance.

To assess perceived implementation performance, we developed a categorical measurement item representing different project outcomes (for details, see Mann 1996). If a subject felt that the outcome of the project did not fit into one of our categories, s/he was encouraged to provide an alternative description of the projectís outcome. These alternative descriptions were then content analyzed and used to augment the original categorization scheme. To measure perceived budget/schedule performance, each respondent was asked to indicate whether the project they reported on went over budget or beyond schedule and, if so, by what percentage.

We now turn to the operationalization of the constructs derived from different theories that have been used to explain escalation. To increase the reliability of the survey instrument, multiple measurement items were developed for each of these constructs. The actual measurement items are shown in Appendix B.

## Psychological Self-Justification Construct

Since psychological self-justification cannot be assessed directly (as this would require access to the subconscious mind of the key decision maker responsible for escalation), we operationalized this construct by tapping into observable behaviors that could serve as reliable indicators of the psychological need to self-justify. Staw and Ross (1987, p. 52) observe that one of the psychological mechanisms that may underlie selfjustification is the concept of self-inference, which implies ìthat individuals examine their own behavior in its social context so as to infer personal values and preferences from prior actions.î Thus, individuals are ìlikely to become committed to a course of action when their prior investments and actions supporting a project have been explicit, freely chosen, visible to others, irrevocable, repeated, and importantî (Staw and Ross 1987, p. 52). In order to tap into this notion, one of our items (PSJ\_1) was designed to measure the extent to which the key decision maker repeatedly expressed support for a project. This item would presumably pick up whether the decision maker had shown repeated signs of support that were visible to others in the organization.

The need to engage in psychological selfjustification is greatest under a condition of high personal responsibility. One of the principle ways in which personal responsibility has been operationalized in previous experiments involving SJT has been to manipulate subjects into believing that they were personally responsible for having initiated some course of action. Of course, a sense of personal responsibility can also be expected to develop over time, given extensive involvement with a project. As Staw and Ross (1987, p. 51) suggest, the level of involvement that an actor has in a project represents a factor that can foster ego-defensiveness, and hence psychological self-justification. Thus, one of our measurement items used to assess the need for psychological self-justification (PSJ\_2) was designed to measure the extent to which the key decision maker either initiated the project or was extensively involved with it.

Of course, other factors can cause a decision maker to engage in psychological self-justification. Emotional attachment to a failing project, for example, is one indicator of over-commitment (Keil 1995). When the key decision maker becomes emotionally attached and, therefore, over-committed to a project, he/she is more likely to engage in psychological self-justification. Hence, we developed a third measurement item (PSJ\_3) to tap into this aspect of the need for psychological self-justification.

## Social Self-Justification Construct

Decision makers may escalate their commitment to a failing course of action ìnot only because they do not want to admit to themselves that they made a mistake, but also because they may be especially hesitant to expose their errors to othersî (Staw and Ross 1987, p. 55). This concept of face-saving has been called social (or external) self-justification in the escalation literature. If abandoning a project would make the key decision maker look bad to others, this would suggest a high need for social self-justification. Thus, one of our measurement items (SSJ\_1) was designed to tap into this notion.

Closely related to the concept of social selfjustification is the notion of external binding, whereby ìpeopleís social identity can become bound or frozen by their actionsî (Staw and Ross 1987, p. 56). In escalation situations, external binding is likely to occur when the key decision maker becomes so closely identified with a project that it is viewed as his/her baby. An extreme instance of this is when a course of action becomes so closely identified with an individua that it carryís his/her name (e.g., ìReaganomicsî). This concept of external binding forms the basis for our second measurement item (SSJ\_2) designed to tap into the social self-justification construct.

## Sunk Cost Effect Construct

The sunk cost effect construct, derived from prospect theory, was operationalized by capturing the extent to which the key decision maker referred to past investments as a reason for project continuation. References to past investments in a project, when offered as a rationale for continuation, can be taken as evidence of the sunk cost effect, and this was the basis for one of our measurement items (SC\_1). Similarly, the decision maker may sometimes justify continuation by exhibiting an attitude that there is too much invested to quit, which formed the basis for our second measurement item (SC\_2). When this is the case, it is strongly suggestive that the sunk cost effect is operative.

Our operationalization is consistent with documented cases involving the sunk cost effect that have been cited in the literature. Arkes and Blumer (1985), for example, describe the TennesseeñTombigbee Waterway Project, which was scheduled for Congressional review in 1981. One senator, who was a proponent of the project, was quoted as saying: ìTo terminate a project in which \$1.1 billion has been invested represents an unconscionable mishandling of taxpayers dollarsî (Arkes and Blumer 1985, p. 124). Our operationalization of the sunk cost effect construct is also consistent with previous research that has employed content analysis to detect phrases that people use to express the notion of sunk cost as a rationale for continuing a troubled project (Keil et al. 1995b). Keil et al. (1995b) have noted that remarks such as ìtoo much money has already been invested to back out of the project nowî are typical of the way in which people express sunk cost as a rationale for continuation.

## Goal Incongruency Construct

Goal incongruency is one of two constructs that were derived from agency theory and used in this study. In our conceptualization, the goal incongruency between principal and agent arises because of powerful forces that inhibit the primary decision maker from transmitting bad news. One such force is the negative impact that transmitting bad news can have on the agentís reputation. Three measurement items were created to operationalize this construct within the context of our study.

As Kanodia et al. (1989) suggest, when managers discontinue a failing project or reveal negative information about a failing project, they reveal information that damages their reputations and can have an adverse effect on future job opportunities. Consistent with this line of reasoning, in the context of information systems projects, goal incongruency can be said to exist within an organizational hierarchy when the primary decision maker on a project (i.e., the agent(s)) acts out of self-interest and continues to plow resources into a failing course of action, instead of acting in the interests of the organization and either redirecting or terminating a failing project. One of our measurement items for goal inconguency (GI\_1) was, therefore, designed to tap into this notion by asking the auditor to share his/her perspective on this point. It should be noted that in our operationalization of agency theory, the principal would be someone higher in the organizational hierarchy than the primary decision maker on the project.

In a more direct attempt to tap into the idea that the agent may suffer negative career consequences for reporting ìbadî news, we created two additional items. One item was designed to measure whether, in the auditorís view, the primary decision maker operated in an environment where ìbad news gets you killedî (GI\_2). The third item (GI\_3) was designed to measure the auditorís perception of whether the primary decision maker operated in an organizational climate where association with an unsuccessful project would have an adverse effect on chances for advancement in the organization.

<table><tr><td colspan="4">Table 2. Survey Response Rates for the Two Different Versions of the Survey</td></tr><tr><td>Survey Type</td><td>No. distributed</td><td>No. returned</td><td>Response rate</td></tr><tr><td>Escalation survey</td><td>1,549</td><td>422</td><td>27%</td></tr><tr><td>Non-escalation (control) survey</td><td>682</td><td>157</td><td>23%</td></tr><tr><td>Total</td><td>2,231</td><td>579</td><td>26%</td></tr></table>

## Information Asymmetry Construct

Information asymmetry is the second construct that was derived from agency theory and used in this study. We created three measurement items designed to assess the extent to which the agent(s) could create or exploit a condition of information asymmetry between themselves and the principal(s). The first measurement item (IA\_1) asked the auditor whether the primary decision maker concealed negative information from top management. Recognizing that information asymmetry can result not only from concealment, but also from distortion of information as it is passed up the hierarchy, we created two additional items to capture this notion. The first measured the auditorsí perceptions of whether the primary decision maker distorted negative information when reporting to upper management (IA\_2). The second measured the auditors perceptions of whether the primary decision maker put a positive spin on any negative project information when reporting to upper management (IA\_3).

## Completion Effect Construct

In this research, we wanted to investigate goa proximityóor the completion effect as it is sometimes calledóbecause it is one of the centra constructs associated with approach avoidance theory and because there is some debate regarding the relative impact of sunk cost and completion effects in cases involving escalation.

The completion effect construct was operationalized by creating two measures designed to assess the extent to which goal proximity, and the need for completion, may have influenced the decision to continue. One measure (C\_1) captured the extent to which the key decision maker exhibited the attitude ìwe have come too far to quit nowî as a rationale for continuing the project. The second measure (C\_2) captured the extent to which the key decision-maker(s) exhibited the attitude ìwe are so close to the end of the project, we should keep going.î Such references to the proximity of achieving a certain goal, when offered as a rationale for continuation, can be taken as evidence of the completion effect.

Our operationalization of the completion effect construct is also consistent with previous research that has employed content analysis to detect phrases that people use to express the completion effect as a rationale for continuing a troubled project (Keil et al. 1995b). Keil et al. (1995b) have noted that remarks such as ìonce you start something, finish itî are typical of the way in which people express the completion effect as a rationale for continuation.

## Response Rate and Tests for Non-response Bias

Table 2 summarizes the response rates for the two different versions of the survey. In total, 579 surveys were returned, yielding a 26% overall response rate.

Non-response bias can be a significant hindrance in the interpretation of results from a mail survey. One method of testing for non-response bias is to compare attributes of the survey respondents with attributes of all individuals receiving the survey. In this study, the state of residence was available for every subject. By assigning each state to a region and then comparing the regional frequencies of respondents to regional frequencies of the full mailing list, we were able to test for non-response bias. Observed frequencies of the respondents were compared with expected frequencies based on the full mailing list. As shown in Table 3, the chi-square test indicated there was no significant difference between the respondents and the ful mailing list on region.

<table><tr><td colspan="3">Table 3. Regional Non-Response Bias Results</td></tr><tr><td>Region</td><td>Expected</td><td>Observed</td></tr><tr><td>Northeast</td><td>228</td><td>226</td></tr><tr><td>Southeast</td><td>73</td><td>82</td></tr><tr><td>N. Central</td><td>92</td><td>91</td></tr><tr><td>S. Central</td><td>85</td><td>76</td></tr><tr><td>Mountain</td><td>25</td><td>27</td></tr><tr><td>Pacific</td><td>71</td><td>70</td></tr><tr><td>Total Chi-Square</td><td colspan="2">2.23 (p-value &gt; 0.816)</td></tr></table>

As a further test for non-response bias, the surveys received were grouped into two ìwavesî based on the date returned, with later respondents serving as a surrogate for non-respondents (Babbie 1973). The first wave included those surveys received within two weeks of the initial mailing (i.e., before the follow-up mailing could have been received and acted on) and the second wave included those received after the follow-up mailing. Using this approach, it was possible to determine whether later respondents were significantly different from earlier respondents on such demographic variables as experience, industry category, number of employees, and number of IS employees. Using non-parametric statistical tests (e.g., Mann-Whitney and Kruskal-Wallis), there was no discernible difference between the two waves on any of the above variables. While the above tests cannot guarantee the absence of any non-response bias, they suggest that the respondents are representative of the population surveyed.

## Respondent Demographics

A total of 72% of our respondents indicated that they were either an IS auditor or IS audit manager. The remaining respondents identified themselves either as external auditors (12%) or specified a different audit-related title (16%). Survey respondents had an average of 8.7 years of experience as an information systems audit and control professional.

The respondents represented organizations varying in size from 10,000 or more employees (36%) to fewer than 100 employees (1%). Most respondents represented medium to large organizations with 1,000 or more employees (83%). Of the respondents, 40% worked for organizations in the financial services industry, although a wide variety of other sectors were also represented, including government (15%), manufacturing (13%), utilities (6%), trade (6%), health care (4%), transportation (2%), education (2%), and other (12%).

With respect to the projects they reported on, nearly half of the subjects indicated that they had either served as the project manager (5%), as a member of the development team (11%), or had been responsible for evaluating the project on a regular basis (32%). Approximately half of the respondents indicated that they became associated at a very early stage with the projects they reported on, either during planning (24%) or requirements analysis (24%).

## Reliability Assessment

Constructs derived from the four theories of escalation involved multiple measurement items that were assessed for reliability. Three of the six constructs were measured using scales with two dichotomous measurement items, whereas the other three constructs were measured using scales with three dichotomous measurement items. As all of our measurement items were dichotomous, standard measures of reliability, such as Cronbach's alpha, could not be used. Instead, we assessed the degree to which items associated with a given scale exhibited complete conformity, partial conformity, or no conformity. Complete conformity occurs when coded responses are identical for all items associated with a scale. Partial conformity occurs in threeitem scales when the coded response on one item is different from the coded response on the other two items. Non-conformity occurs in two-item scales when the coded response on one item is different from the coded response on the other item. By definition, two-item scales cannot exhibit partial conformity and three-item scales cannot exhibit non-conformity. Table 4 summarizes the level of conformity associated with each of the measurement scales.

<table><tr><td colspan="5">Table 4. Level of Conformity Associated with Measurement Items</td></tr><tr><td>Construct</td><td># of Items</td><td>Complete Conformity n* = (%)</td><td>Partial Conformity n = (%)</td><td>No Conformity n = (%)</td></tr><tr><td>Completion Effect</td><td>2</td><td>230 (75.4)</td><td>-</td><td>75 (24.6)</td></tr><tr><td>Sunk Cost Effect</td><td>2</td><td>235 (78.6)</td><td>-</td><td>64 (21.4)</td></tr><tr><td>Goal Congruency</td><td>3</td><td>151 (53.5)</td><td>131 (46.5)</td><td>-</td></tr><tr><td>Information Asymmetry</td><td>3</td><td>179 (66.8)</td><td>89 (33.2)</td><td>-</td></tr><tr><td>Social Self-Justification</td><td>2</td><td>189 (63.0)</td><td>-</td><td>111 (37.0)</td></tr><tr><td>Psychological Self-Justification</td><td>3</td><td>110 (37.5)</td><td>183 (62.5)</td><td>-</td></tr></table>

\*Note: The number of cases associated with each scale differs due to missing values.

For five of the six scales, the level of complete conformity is substantially greater than the level of partial conformity or no conformity. Note that psychological self-justification is the only scale where the number of cases with partial conformity is greater than the number of cases with complete conformity. One measurement item, namely PSJ\_3 (emotional attachment) as shown in Appendix B, contributed to a substantial portion of the observed partial conformity for the psychological self-justification construct. Accordingly, we deleted this item and used a two-item measure for the psychological self-justification construct.

## Convergent and Discriminant Validity

The item-to-construct correlations were first computed to examine convergent and discriminant validity (Table 5). All measurement items, with the exception of PSJ\_1 (repeatedly expressed support), had correlation coefficients greater than .73 with the construct they were designed to measure. This item had a moderate correlation of .55 with the self-justification construct. We retained PSJ\_1 as part of the two-item psychological self-justification construct because this correlation was still moderate.

Only one of the items had a very high correlation with a construct other than the one that it was intended to measure. Specifically, SC\_2 ("too much invested to quit"), which is one of the two items designed to measure sunk cost effect, also has a correlation of .74 with completion effect. Accordingly, this item was dropped as a measurement item, and the sunk cost effect construct was assessed using a one-item measure.

To further assess the discriminant validity of our measures, we examined the inter-construct correlation matrix (Table 6).

<table><tr><td colspan="8">Table 5. Item-to-Construct Correlations*</td></tr><tr><td rowspan="2">Constructs</td><td rowspan="2">Item  $Measures^a$ </td><td colspan="6">Constructs</td></tr><tr><td>Completion Effect</td><td>Sunk Cost Effect</td><td>Goal Incongruency</td><td>Information Asymmetry</td><td>Social Self-Justification</td><td>Psychological Self-Justification</td></tr><tr><td rowspan="2">Completion Effect</td><td>C_1</td><td>.87</td><td>.66</td><td>.40</td><td>.31</td><td>.37</td><td>.19</td></tr><tr><td>C_2</td><td>.87</td><td>.55</td><td>.33</td><td>.32</td><td>.25</td><td>.11</td></tr><tr><td rowspan="2">Sunk Cost Effect</td><td>SC_1</td><td>.51</td><td>.88</td><td>.38</td><td>.27</td><td>.28</td><td>.01</td></tr><tr><td>SC_2</td><td>.74</td><td>.88</td><td>.39</td><td>.34</td><td>.39</td><td>.11</td></tr><tr><td rowspan="3">Goal Incongruency</td><td>GI_1</td><td>.40</td><td>.42</td><td>.77</td><td>.58</td><td>.45</td><td>.12</td></tr><tr><td>GI_2</td><td>.30</td><td>.31</td><td>.79</td><td>.59</td><td>.39</td><td>.03</td></tr><tr><td>GI_3</td><td>.26</td><td>.25</td><td>.73</td><td>.35</td><td>.27</td><td>.10</td></tr><tr><td rowspan="3">Information Asymmetry</td><td>IA_1</td><td>.30</td><td>.27</td><td>.57</td><td>.85</td><td>.39</td><td>.03</td></tr><tr><td>IA_2</td><td>.35</td><td>.34</td><td>.62</td><td>.89</td><td>.45</td><td>.17</td></tr><tr><td>IA_3</td><td>.29</td><td>.29</td><td>.48</td><td>.79</td><td>.40</td><td>.12</td></tr><tr><td rowspan="2">Social Self-Justification</td><td>SSJ_1</td><td>.37</td><td>.39</td><td>.45</td><td>.42</td><td>.82</td><td>.22</td></tr><tr><td>SSJ_2</td><td>.20</td><td>.24</td><td>.36</td><td>.39</td><td>.83</td><td>.25</td></tr><tr><td rowspan="2">Psychological Self-Justification</td><td>PSJ_1</td><td>.09</td><td>.05</td><td>.07</td><td>.05</td><td>.18</td><td>.55</td></tr><tr><td>PSJ_2</td><td>.03</td><td>.06</td><td>.12</td><td>.10</td><td>.27</td><td>.84</td></tr></table>

<sup>\*</sup>The actual scal e item s used are s hown i n Append ix 2 . S haded cel ls i n th is tabl e represent i ns ig n ifi cant correl ations (p > . 05) .

<table><tr><td colspan="7">Table 6. Inter-construct Bivariate Correlations*</td></tr><tr><td>Constructs1</td><td>Completion Effect</td><td>Sunk Cost Effect</td><td>Goal Incongruency</td><td>Information Asymmetry</td><td>Social Self-Justification</td><td>Psychological Self-Justification</td></tr><tr><td>Completion Effect</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sunk Cost Effect</td><td>.51</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>Goal Incongruency</td><td>.43</td><td>.38</td><td>1</td><td></td><td></td><td></td></tr><tr><td>Information Asymmetry</td><td>.37</td><td>.27</td><td>.67</td><td>1</td><td></td><td></td></tr><tr><td>Social Self-Justification</td><td>.35</td><td>.28</td><td>.48</td><td>.50</td><td>1</td><td></td></tr><tr><td>Psychological Self-Justification</td><td>.09</td><td>.01</td><td>.09</td><td>.09</td><td>.28</td><td>1</td></tr></table>

<sup>\*</sup><sub>p</sub> > . 05 for the s haded cel ls wh i ch re<sub>p</sub>resent i ns i<sub>g</sub> n ifi cant correl ations .

Ghiselli et al. (1981) suggest that correlations greater than 0.80 suggest extreme cases of multicollinearity. No such cases of extreme multicollinearity were detected. The two constructs derived from agency theory (goal incongruency and information asymmetry) have a high correlation. However, as these constructs tap into two different sets of issues suggested by agency theory, we retained them as two separate variables in our subsequent analysis.

After establishing the reliability and validity of our measurement items, aggregate measures were computed by summing responses to scale items and then dividing by the number of items. Since each item was measured on a dichtomous scale (1 if the item was present in the project and 0 if it was not), the values of each construct represented a continuum that varied from 0 (not present) to 1 (present).

## Results and Discussion

This section presents the major findings from our study organized around the three research questions we sought to address.

## Frequency and Duration of Software Project Escalation

Our first research question was aimed at gaining a better understanding of the frequency and duration of project escalation. In short, we were interested in knowing how frequently escalation occurs and how long it lasts when it does occur. Duration of escalation refers to how long projects are allowed to continue after the point at which an IS auditor believes they should have been terminated or redirected.

The survey results provide convincing indications that project escalation is a common problem. To obtain as accurate an estimate as possible concerning the frequency of escalation, we examined a restricted view of the data set, which included only those respondents who had experience with at least five projects coupled with three or more years of relevant job experience (n = 361). Respondents included in this analysis had an average of 10.5 years of work experience as an IS audit and control professional.

When asked how many of the last five projects they had been associated with were cases of project escalation, 81% of the respondents indicated that one or more of their last five projects involved escalation. The mean response was 1.92, suggesting that escalation occurs (on average) in 38% of all software projects. When asked directly what percentage ìof all the projects with which you have been associated during your years as an information systems control professional...would you classify as cases of project escalation?,î the mean response was 0.304. When asked: ìIn your judgment what percentage of all IS development projects are cases of project escalation?,î the mean response was 0.383. It is interesting to note that all three of the escalation frequency measures yielded similar results. The reliability between these items was extremely high (.92). Taken together, the three measures described above provide a remarkably consistent view of how frequently IT project escalation occurs; the data strongly suggest that 30% to 40% of all IT projects involve some degree of project escalation.

By capturing key dates in the escalation survey (i.e., the month/year when the project began to escalate, and the month/year when the project was either terminated or redirected), it was possible to calculate the duration of escalation (in months). Escalation time among the projects surveyed ranged from one month to 255 months (i.e., 21 years!). Nearly 75% of the projects escalated for two years or less. Among projects that escalated, the average escalation time was 21 months with half of the projects escalating for 15 or more months.

Together, these findings strongly suggest that escalation is a frequently occurring problem and that both researchers and managers should be concerned about it. The findings reported here appear to contrast sharply with the views of some practitioners, who contend that software project runaways are rare events (Glass 1997).

<table><tr><td colspan="3">Table 7. Perceived Implementation Performance</td></tr><tr><td>Category</td><td>Escalated Projects</td><td>Non-Escalated Projects</td></tr><tr><td></td><td>(N=243)</td><td>(N=91)</td></tr><tr><td>Abandoned Before Completion</td><td>44 (18%)</td><td>4 (4%)</td></tr><tr><td>Never Implemented</td><td>13 (5%)</td><td>2 (4%)</td></tr><tr><td>Partially Completed</td><td>56 (23%)</td><td>2 (2%)</td></tr><tr><td>Less than Successful</td><td>44 (18%)</td><td>4 (4%)</td></tr><tr><td>Withdrawn After Implementation</td><td>20 (8%)</td><td>2 (2%)</td></tr><tr><td>Completed and Successful</td><td>55 (23%)</td><td>76 (84%)</td></tr><tr><td>Other</td><td>11 (5%)</td><td>1 (1%)</td></tr></table>

<table><tr><td colspan="3">Table 8. Perceived Budget/Schedule Performance</td></tr><tr><td>Type of Project</td><td>Average % Beyond Budget Target</td><td>Average % Beyond Schedule Target</td></tr><tr><td>Escalated</td><td>156%</td><td>133%</td></tr><tr><td>Non-Escalated</td><td>18%</td><td>22%</td></tr><tr><td>T-Test</td><td>p &lt; .001</td><td>p &lt; .001</td></tr></table>

## Comparison of Escalated vs. Nonescalated Project Performance

Our second research question was aimed at understanding whether projects that escalate differ significantly from projects that do not escalate in terms of project performance. Using measures for perceived implementation performance and perceived budget/schedule performance, we found significant differences between projects that escalated and those that did not.

## Perceived Implementation Performance

For classification purposes, each project was assigned to a single outcome category (i.e., the one that best seemed to fit the respondentís opinion regarding the outcome of the project). The classification scheme used here for perceived implementation performance is categorical in nature and is not meant to represent a smooth continuum from failure to success. The perceived implementation performance categories and the frequency with which projects were assigned to them are shown in Table 7.

As shown in Table 7, only 23% of the escalated projects were considered to be completed and successful, whereas 84% of the non-escalated projects were judged to be completed and successful (Chi-square p < .001). Moreover, all of the negative outcome categories were higher for escalated projects than for non-escalated projects.

## Perceived Budget/Schedule Performance

The survey data indicate that escalated projects were not only more likely to be perceived as late and over budget; but that the amount (i.e., the percentage) by which they were perceived to exceed their schedules and budgets was much greater than that exhibited by non-escalated projects. More than 82% of the projects that escalated were perceived to have exceeded their budgets, whereas only 48% of the non-escalation projects were perceived to have exceeded their budgets. In addition, 91% of the projects that escalated were perceived to have exceeded their original schedule as compared with 58% of the non-escalation projects. Table 8 shows the degree to which escalated and non-escalated projects were perceived to exceed their schedule and budget targets when overruns did occur.

Notice that the differences between escalated and non-escalated projects are significant at the .001 level on both dimensions. Table 8 is also consistent with the notion that budgets and schedules for software projects are frequently underestimated; even the non-escalated projects (which were defined as ones that progressed smoothly enough that continuation was never questioned) showed an 18% overrun on budget and a 22% overrun on schedule.

To summarize, projects that escalate are perceived to be significantly different (from nonescalated projects) in terms of both implementation and budget/schedule performance. This does not mean, however, that all cases of escalation are doomed to perform poorly, nor does it mean that all non-escalated projects perform well. It simply means that escalated projects are significantly more likely to have performance problems. This finding contributes to prior research by showing that escalated projects exhibit significantly worse performance than non-escalated projects.

## Using Theory-Based Models to Distinguish Escalation from Non-Escalation

Our third research question was whether constructs associated with the four theories of escalation could be used to create models capable of distinguishing between projects that escalate and those that do not. Here, we present the results of four separate logistic regression models, one for each theory, designed to test whether the theoretically derived constructs associated could be used to distinguish between projects that escalated and those that did not.

A hierarchical method of analysis was used to develop and then compare models using logistic regression. Logistic regression analysis was chosen over discriminant analysis, because we are dealing with a dichotomous dependent variable, and non-parametric type independent variables with non-normal distributions. The dependent variable was whether the project was escalated (1) or non-escalated (0). Each independent variable was whether a condition was present in the project (1) or not present (0). Logistic regression uses a non-parametric model and, therefore, does not require variables to be normally distributed.

## Controlling for Exogenous Variables.

Demographic variables, such as organization and IS department size, auditor experience, and project size, can potentially impact escalation. The sample was segmented using each of these variables but no significant differences were found across escalated and non-escalated projects, except for project size.

Project size, therefore, was used as an exogenous variable in the analysis. As shown in Appendix B, respondents indicated the relative size of the project on a Likert scale, which ranged from 0 (smaller in size compared to other IS projects undertaken) to 6 (larger in size compared to other IS projects undertaken). Size was included to examine if larger projects were more vulnerable to escalation. A normalized measure of project size was computed by dividing indicated responses by six.

## Logistic Regression Results

Our first step was to take the constructs from each theory and create a model with only those constructs and project size. Each model was then evaluated as to the significance of the model (using 75% of the original sample) and the importance of each construct within the model. Finally, the other 25% of the original sample was used to determine how useful each model was in classifying new projects. In logistic regression, several measures of model significance can be used. Table 9 shows all the measures for each of our models based on different escalation theories and project size. Appendix C provides an explanation of relevant statistics used for interpreting logistic regression results.

According to the Hosmer-Lemeshow goodness-offit test, all the models were significantly better at determining the probability of project escalation than random chance. Two of the models, however, outperformed the others. The two strongest models were those based on constructs derived from agency theory and approach avoidance theory. These models equally reduced the sum of squared error (lower -2 Log Likelihood) and had comparable R<sup>2</sup> values. Of the two, the one derived from approach avoidance theory was marginally better. To continue the assessment of each model, Table 10 presents several measures describing the importance of constructs within each model.

Table 9. Analysis of Project Escalation Behavior Results for Model Fit

<table><tr><td>Logistic Model Derived from Constructs Associated with ...</td><td>-2 Log Likelihood</td><td>Cox &amp; Snell  $R^2$ </td><td>Nagelkerke  $R^2$ </td><td>Hosmer-Lemeshow Goodness-of-fit (chi-square, p &lt;)</td></tr><tr><td>Self Justification Theory</td><td>252.55</td><td>.09</td><td>.13</td><td>(3.20, .92)</td></tr><tr><td>Prospect Theory</td><td>241.52</td><td>.12</td><td>.18</td><td>(3.39, .85)</td></tr><tr><td>Agency Theory</td><td>209.93</td><td>.23</td><td>.32</td><td>(11.29, .19)</td></tr><tr><td>Approach Avoidance Theory</td><td>209.10</td><td>.26</td><td>.37</td><td>(2.03, .98)</td></tr></table>

The significance of a construct was assessed by examining the p-value of the Wald statistic (which measures significance of the construct after accounting for its error) and the 95% Confidence Interval Odds Ratio (if the interval does not contain the number one, then the item is significant). For example: the constructs based on the different theories were all significant except psychological self-justification. Except for psychological selfjustification, all constructs had Wald p-values less than .05 and their Confidence Interval Odds Ratios did not include one.

The degree to which a construct was useful for distinguishing project escalation was determined by examining the standardized Betas (SE Beta) and the Odds Ratios. The odds ratio is the increase in likelihood in project escalation corresponding to an increase in an independent variable. In the model based on self-justification, the project size standardized beta was higher than either psychological or social self-justification. Moreover, the odds ratio for project size was higher than psychological self-justification and similar to social self-justification (approximately three-fold increase in project escalation when social self-justification is present or project size increases).

In the model based on prospect theory, project size was more important than the sunk cost effect in both the standardized betas and the odds ratio (4.96-fold increase and 4.17-fold increase, respectively).

For the model based on constructs derived from agency theory, project size had the strongest standardized beta but the weakest odds ratio. Information asymmetry had the weakest standardized beta and the strongest odds ratio (sevenfold increase in project escalation when information asymmetry is present). Goal congruency was in the middle on both measures of importance.

In the model based on the construct derived from approach avoidance theory, project size had a stronger standardized beta but completion effect had by far the largest odds ratio (21-fold increase in project escalation when completion effect is present!).

<table><tr><td colspan="7">Table 10. Analysis of Project Escalation Behavior Significance Results for Each Construct</td></tr><tr><td>Models</td><td>Beta</td><td>SE (Beta)</td><td>Odds Ratio</td><td>95% CI Odds Ratio</td><td>Wald</td><td>p&lt;</td></tr><tr><td>Model Based on Constructs Related to Self Justification Theory</td><td colspan="6"></td></tr><tr><td>Project Size</td><td>1.21</td><td>.56</td><td>3.36</td><td>(1.11,10 .13)</td><td>4.63</td><td>.032</td></tr><tr><td>Psychological Self-Justification</td><td>.14</td><td>.45</td><td>1.15</td><td>(.48, 2.76)</td><td>.10</td><td>.753</td></tr><tr><td>Social Self-Justification</td><td>1.27</td><td>.44</td><td>3.57</td><td>(1.52, 8.40)</td><td>8.50</td><td>.004</td></tr><tr><td>Model Based on Constructs Related to Prospect Theory</td><td colspan="6"></td></tr><tr><td>Project Size</td><td>1.60</td><td>.57</td><td>4.96</td><td>(1.62, 15.20)</td><td>7.87</td><td>.005</td></tr><tr><td>Sunk Cost Effect</td><td>1.43</td><td>.35</td><td>4.17</td><td>(2.11, 8.21)</td><td>17.00</td><td>.001</td></tr><tr><td>Model Based on Constructs Related to Agency Theory</td><td colspan="6"></td></tr><tr><td>Project Size</td><td>1.22</td><td>.62</td><td>3.39</td><td>(1.00, 11.51)</td><td>3.85</td><td>.05</td></tr><tr><td>Goal Congruency</td><td>1.30</td><td>.59</td><td>3.65</td><td>(1.16, 11.50)</td><td>4.90</td><td>.027</td></tr><tr><td>Information Asymmetry</td><td>1.98</td><td>.54</td><td>7.28</td><td>(2.51, 21.08)</td><td>13.38</td><td>.001</td></tr><tr><td>Model Based on Constructs Related to Approach Avoidance Theory</td><td colspan="6"></td></tr><tr><td>Project Size</td><td>1.77</td><td>.64</td><td>5.88</td><td>(1.67, 20.70)</td><td>7.62</td><td>.006</td></tr><tr><td>Completion Effect</td><td>3.06</td><td>.47</td><td>21.34</td><td>(8.06, 53.81)</td><td>42.05</td><td>.001</td></tr></table>

## Sensitivity Analysis

As discussed earlier, the auditors played different roles in assessing the project and became involved with the project at different phases. We conducted two sets of sensitivity tests to ascertain if the observed pattern of relationships between each set of theoretical constructs and project escalation was stable across auditor role or phase when s/he became involved. In the first set of sensitivity tests, we examined the stability of observed relationships with respect to role played by the auditor. Subjects who participated as a project manager, served as a member of the development team, or audited the project on a regular basis were placed in one group. Subjects who evaluated the project on a less frequent basis or who played some other role in the project were placed in a second group. The pattern of results observed in our logistic regressions for each of the theories was the same across the two groups of auditor roles.

In the second set of sensitivity tests, we examined the stability of observed relationships with respect to the phase when the auditor became involved with the project. Subjects who became involved during planning or requirements analysis were placed in one group; subjects who became involved during later phases of the development process were placed in a second group. The pattern of results observed in our logistic regressions for each of the theories was the same across the two groups, as defined by the phase at which the auditor became involved with the project. The sensitivity analysis provides support for the pooling of our data across roles played by the auditors and the phase in the project when they became involved. Furthermore, these results provide additional evidence for the pattern of relationships identified above using the entire sample.

Predictive Validity: How Well Does Each Model Classify New Projects?

To assess the predictive validity of each model, we examined its classification performance on both the estimation sample and a separate holdout sample. As a base of comparison, we computed the Morrison's (1969) proportional chance criterion given by the model:

$$
C = a l p h a ^ {2} + (1 - a l p h a) ^ {2}
$$

where alpha is the proportion of projects in group 1 and (1-alpha) is the proportion of projects in group 2. In our study, group 1 was escalated projects (approximately 73%) and group 2 was nonescalated projects (27%). For our sample, Morrison's chance criterion (i.e., the overall percentage correct expected by chance) is .59. Accordingly, we used a cutoff estimated probability of 0.59 to determine membership in a given group according to chance.

Table 11 shows the classification results that were obtained for both the estimation sample and the holdout sample. Chi-square tests indicated that all four logistic regression models performed better than chance in terms of their classification ability for both the estimation and holdout samples.

The model derived from approach avoidance theory, however, had the strongest results. Based on the completion effect construct and project size, it correctly classified over 70% of both escalated and non-escalated projects. As this performance level is consistent across the estimation and holdout samples, we have strong evidence of the validity of completion effect predicting project escalation. The model based on constructs derived from agency theory also performs well in classifying both escalated and non-escalated projects, although its predictive performance drops off somewhat in the holdout sample. Interestingly, the models based on constructs derived from selfjustification theory and from prospect theory both perform well in classifying escalated projects (for both the estimation and the holdout samples), but are relatively poor in classifying non-escalated projects. In summary, constructs derived from approach avoidance theory and agency theory perform well in classifying both escalated and nonescalated projects. On the other hand, constructs derived from self-justification theory and prospect theory perform well in classifying escalated projects, but do not perform well in their classification of non-escalated projects.

## Limitations of the Study

Before discussing the implications of our work, it is appropriate to mention its limitations. This study relied on IS audit and control professionals as subjects and involved self-reported information concerning projects that had been completed some time earlier. What is more, the auditors in our study were asked to furnish opinions regarding the motivation and intentions of the key decision maker on a project. These factors raise the prospect of a possible bias or a significant amount of error in our data set and thus our conclusions must be interpreted with some caution.

As an example of possible bias, it is conceivable that auditors are more likely to be assigned to troubled projects and that their estimates of the frequency of project escalation may, therefore, contain an upward biasing. However, this is not necessarily the case. It is conceivable that IS auditors tend to be employed more commonly by organizations that are more cognizant of the need for good software project management. Firms employing IS auditors might, therefore, have a lower incidence of software project escalation. By this logic, it is possible that the choice of IS auditors may have introduced a downward biasing in our estimates of the frequency of project escalation. While the choice of auditors as subjects certainly creates the possibility of an upward or downward bias in our estimates, there were several advantages of relying on IS auditors that outweighed these concerns. These include: (1) IS auditors do not have directly vested interests in project outcomes because their careers are unlikely to be made or broken by a projectís success or failure, (2) IS auditors can be expected to report more objectively than managers and other project participants, (3) IS auditors have access to objective data on project performance, and (4) IS auditors have experience with multiple projects and formal standards for judging projects.

<table><tr><td colspan="7">Table 11. Results of Logistic Regression Models: Classification Analysis</td></tr><tr><td></td><td colspan="3">Estimation Sample (n = 242)</td><td colspan="3">Holdout Sample (n = 80)</td></tr><tr><td>Models</td><td>Escalated (%)</td><td>Non-escalated (%)</td><td>Overall (%)</td><td>Escalated (%)</td><td>Non-escalated (%)</td><td>Overall (%)</td></tr><tr><td>Model Based on Constructs Related to Self Justification Theory</td><td>84.34</td><td>40</td><td>71.86</td><td>87.04</td><td>42.86</td><td>74.56</td></tr><tr><td>Model Based on Constructs Related to Prospect Theory</td><td>85.09</td><td>36.92</td><td>71.24</td><td>82.69</td><td>38.1</td><td>69.86</td></tr><tr><td>Model Based on Constructs Related to Agency Theory</td><td>78.43</td><td>72.31</td><td>76.61</td><td>68.36</td><td>60</td><td>66.20</td></tr><tr><td>Model Based on Constructs Related to Approach Avoidance Theory</td><td>77.25</td><td>71.21</td><td>75.54</td><td>72.22</td><td>80.95</td><td>74.67</td></tr></table>

It is possible that auditors may not have sufficient information to provide knowledgeable responses to questions concerning the motivations and intentions of other actors. Our data, however, suggest that the auditors tended to have an early and relatively high level of involvement in the projects they reported on, suggesting that they were in a position to respond accurately to the questions we posed.

Another limitation is that our research is based on the input of a single respondent for each case studied and is subject to methods bias. Having the same subjects rate both project performance as well as behavioral factors may have led to percept-percept inflation, although the literature suggests that such effects may be smaller and less widespread than previously believed (Crampton and Wagner 1994). By asking respondents to retrospectively characterize troubled vs. less troubled projects, there is also the possibility that respondents ìimputedî the presence of escalation factors onto troubled projects. A one-way ANOVA on all of the escalation-related variables, however, revealed a half-dozen variables where there was no significant mean difference between the escalated and non-escalated projects. The fact that there was some selectivity in the negative factors associated with escalated vs. nonescalated projects suggests that the methods bias threat is minimal in this study.

The reliability of the data might have been improved had we been able to gather data on individual projects from multiple subjects. Such an approach was not feasible, however, in this study. Further, it will be recalled that one of the reasons we chose IS auditors is that we believed they would provide a more unbiased view than other project participants. So, while multiple respondents are generally desirable, it remains unclear whether such an approach would lead to more reliable data in a study context such as this one. Another potential problem involves the issue of recall bias. Since our study relied on selfreported information concerning past events, our data is subject to possible recall bias. Short of conducting a prospective study of escalation, we know of no good mechanism to avoid the problem of subject recall.

Finally, we must note that the operationalization and measurement of escalation-related constructs was challenging and, in some ways, problematic. In the case of prospect theory and the sunk cost effect, we were constrained to the use of a single item measure in our analysis. In addition, our measurement items used to operationalize constructs associated with the four theories of escalation required subjects to make subjective assessments of the attitudes and behaviors exhibited by the key decision maker associated with a project. In some cases, the theories and some of their associated constructs proved difficult to operationalize in the form of one or more questionnaire items. The concept of psychological self-justification serves as an example. Clearly, feelings of personal responsibility, judged to be an essentia element of psychological self-justification, are difficult to assess through a third party. To create measurement items designed to assess the need for psychological self-justification, we, therefore, turned to factors that can give rise to (or be indicative of) a heightened sense of personal responsibility. As an example, repeated expressions of support for a project, extensive involvement or initiation of a project, and emotional attachment to a project may all be suggestive of a heightened sense of personal responsibility. Any of these conditions can thus be expected to induce psychological self-justification in the presence of negative feedback.

Perhaps as a consequence of the operationalization issue just discussed, it should come as no great surprise that psychological self-justification was not a useful discriminator between projects that escalated and those that did not. Because we were unable to measure psychological self-justification directly, our operationalization focused upon attitudes and behaviors that might just as reasonably be displayed in the context of non-escalating projects, as they would be expected to appear in the context of escalating projects. Therefore, the results of our study should certainly not be interpreted to mean that SJT is not a potent theory, but rather that, as operationalized in this study, the concept of psychological self-justification does not allow us to predict which projects will escalate and which ones will not. Further, it should be noted that in drawing upon the four theories of escalation for development of our models, we have selectively chosen to emphasize certain constructs that we believe are central to the theories, while omitting other constructs that may also be important. For example, in the case of approach avoidance, we chose to emphasize the completion effect construct and did not operationalize other constructs associated with the theory. Therefore, it would be misleading to construe our work here as ìprovingî that one theory of escalation is superior to another. This is certainly not our intent. With that being said, we believe that our work does show the value of using theoretically derived constructs to develop and test models capable of discriminating between projects that escalate and those that do not.

## Implications for Research

The results of our study contribute to existing research in several important ways. First, the study provides evidence that escalation is a relatively frequent problem and that escalated projects exhibit markedly worse performance than projects that do not escalate. Second, the study reveals that variables derived from various escalation theories can be used to distinguish between projects that escalate and those that do not. By operationalizing certain constructs associated with self-justification theory (SJT), prospect theory (PT), agency theory (AT), and approach avoidance theory (AAT), and examining their influence on escalation across a large sample of projects, we have shown that elements of all four theories seem to have some predictive validity. This, in itself, represents a contribution to research because it suggests that the theories that have been invoked to explain the escalation phenomenon are not mutually exclusive. Rather than viewing them as alternative theories, as they are frequently portrayed in the escalation literature, they should perhaps be viewed as complementary. Future research should attempt to combine elements of these theories to create a richer theory of this complex phenomenon. Our findings suggest that escalation is a complex phenomenon and that more sophisticated models are needed to explain escalation behavior.

While constructs derived from all four theories were significant in logistic regression models, the completion effect construct derived from approach avoidance theory seemed to be best at discriminating between escalated and non-escalated projects. The model derived from agency theory constructs seemed to also provide good classification, but exhibited a decrease in prediction capability on the holdout sample, as compared to the estimation sample. The sunk cost effect construct provided relatively good classification of escalated projects, but was relatively poor at classifying non-escalated projects. In some measure, this may be seen to corroborate previous research (Conlon and Garland 1993) suggesting that the completion effect dominates the sunk cost effect in terms of explaining escalation behavior. From a measurement standpoint, however, we found it difficult to construct measures of sunk cost and completion that did not correlate highly with one another. This suggests that subjects may be inferring sunk cost information from completion information and vice versa. If the completion effect of approach avoidance theory overlaps with the sunk cost effect of prospect theory (and this would explain the relatively high inter-correlation between the two scales), then further research is needed to fully understand the relationship between the two theories.

## Implications for Practice

Some practitioners may be inclined to believe that project escalation is a rare event (Glass 1997). This study suggests otherwise. Managers should be aware that the incidence of project escalation is relatively high and that the outcomes associated with such projects tend to be markedly worse than projects that do not escalate. The models developed here may help managers to identify and prevent escalation. Since constructs derived from all four theories were significant in logistic regression models, managers should consider their implications for practice. The results obtained using the model derived from agency theory constructs, for example, underscore the importance of good communication and monitoring of projects to avoid the condition of information asymmetry. To minimize the problems associated with escalation, managers would do well to implement early warning systems aimed at detecting escalation as early as possible. One way to minimize budget and schedule escalation is to define the de-escalation trigger points at the outset of the project. In this way, when the cost and schedule begin to approach the predefined trigger points, managers can take steps to deescalate the project and contain the damage. Another related tactic is defining termination conditions at the outset of the project. Finally, managers can embrace one or more of the models presented here and tailor it to their own environment.

The best model developed in this paper classified 77% of the escalated projects and 71% of the non-escalated projects correctly. Practicing managers should consider using and refining this model as an aid in reviewing their software project portfolios. If the goal is to reduce the prevalence of escalated projects, it should be noted that some of the other models we tested provided marginally better classification of escalated projectsó however, they provided significantly poorer classification of non-escalated projects. The problems of incorrectly classifying a non-escalating project as escalating and incorrectly classifying an escalating project as non-escalating may be considered in terms of type 1 and type 2 errors. It is important that managers understand the tradeoff associated with minimizing type 2 errors at the expense of generating type 1 errors and vice versa. To illustrate this, consider the following example.

Suppose an organization has made a policy decision that projects undergoing possible escalation are to be avoided at all costs (i.e., to minimize type 2 errors). If there is any evidence that a project is possibly escalating, the project is terminated and the resources transferred to other uses. Minimizing type 2 errors has important ramifications for the organization that pursues such a strategy. First, it is critical to understand that in making this policy decision, the organization has also (perhaps unknowingly) created an associated policy that it is acceptable to prematurely cancel projects that are non-escalating and which may have eventually yielded benefits to the organization (i.e., a type 1 error). However, this second ìpolicy decisionî is a natural by-product of the decision to minimize type 2 errors. Furthermore, by minimizing type 2 errors, organizations will never experience escalation and will, therefore, never learn how to recognize and manage such problems if and when they do occur.

The alternative situation to consider occurs when an organization makes a policy decision that projects are not canceled until there is sufficient evidence that the project is no longer worthwhile. In doing so, however, the organization has also made a decision (again, possibly without realizing it) that some escalation (type 2 errors) is an acceptable tradeoff in striving to avoid type 1 errors. This tradeoff between type 1 and type 2 errors has strategic implications. Companies gain or maintain competitive advantage for a number of reasons, including their information technology. Thus an organization that chooses to avoid escalation at all costs may also be choosing, perhaps not deliberately, to potentially forego some software projects that could provide competitive advantage. On the other hand, allowing too many cases of escalation to be continued on the grounds that the project may be incorrectly classified will drain valuable resources from the organization that could have been used for other purposes. Managers should therefore consider their organizationís strategy and culture in determining an appropriate balance between type 1 and type 2 errors. By developing and applying tools such as the models presented here, it is hoped that IS management will be able to strike an appropriate balance between obtaining and removing commitment on projects.

## Summary and Conclusions

The IS literature contains several case studies of projects that have undergone escalation and were ultimately judged to be failures (e.g., Drummond 1996; Keil 1995), but the prevalence of this phenomenon and the outcomes generally associated with such projects have not been previously established. This studyóthe first large-scale field survey on software project escalationósuggests that between 30% and 40% of all software projects exhibit some degree of escalation. The results of the study also indicate that escalated projects have significantly more performance problems than projects that do not escalate.

In building models capable of distinguishing escalated from non-escalated projects, we found that the completion effect increased the chances of project escalation by 21 times and that the constructs associated with agency theoryó information asymmetry and goal incongruence) increased the chances of project escalation by seven times and 3.6 times, respectively. The results reported here have significant implications for both research and practice because they suggest that cases of escalation can be identified with a high probability simply by examining the presence of certain behavioral factors. It should be noted that these behavioral factors appear to provide substantially more useful information about the probability of project escalation than traditiona structural variables, such as project size.

To summarize, one of the primary contributions of this study is the evidence that it provides concerning both the prevalence and seriousness of software project escalation. This research also represents an initial step toward providing a theory-based approach for managing the problem.

## Acknowledgements

This research was funded in part by a grant from the Information Systems Audit and Control Foundation. Research funding was also supplied, in part, by a research grant from Georgia State Universityís J. Mack Robinson College of Business. The authors would like to thank the senior editor, Kalle Lyytinen, the associate editor, and the reviewers for their constructive suggestions which helped shape the manuscript.

## References

Abdel-Hamid, T. K. ìUnderstanding the '90% Syndrome' in Software Project Management: A Simulation-Based Case Study,î The Journal of Systems and Software (8:4), 1988, pp. 319- 330.

Abdel-Hamid, T., and Madnick, S. E. Software Project Dynamics: An Integrated Approach, Prentice Hall, Englewood Cliffs, NJ, 1991.

Arkes, H. R., and Blumer, C. ìThe Psychology of Sunk Cost,î Organizational Behavior and Human Decision Processes (35), 1985, pp. 124-140.

Armstrong, J. S., Coviello, N., and Safranek, B. ìEscalation Bias: Does It Extend to Marketing?,î Journal of the Academy of Marketing Science (21:3), 1993, pp. 247-253.

Babbie, E. R. Survey Research Methods, Wadsworth Publishing, Belmont, CA, 1973.

Baiman, S. ìAgency Research in Manageria Accounting: A Second Look,î Accounting, Organizations and Society (15:4), 1990, pp. 341-371.

Brockner, J. ìThe Escalation of Commitment to a Failing Course of Action: Toward Theoretica

Progress,î Academy of Management Review (17:1), 1992, pp. 39-61.

Brockner, J., and Rubin, J. Z. Entrapment in Escalating Conflicts: A Social Psychological Analysis, Springer-Verlag, New York, 1985.

Brockner, J., Shaw, M. C., and Rubin, J. Z. ìFactors Affecting Withdrawal from an Escalating Conflict: Quitting Before It's Too Late,î Journal of Experimental Social Psychology (15), 1979, pp. 492-503.

Brooks, F. P. The Mythical Man-Month: Essays on Software Engineering, Addison-Wesley, Reading, MA, 1975.

Conlon, D. E., and Garland, H. ìThe Role of Project Completion Information in Resource Allocation Decisions,î Academy of Management Journal (36:2), 1993, pp. 402-413.

Crampton, S. M., and Wagner, J. A. ìPercept-Percept Inflation in Microorganizational Research: An Investigation of Prevalence and Effect,î Journal of Applied Psychology (79:1), 1994, pp. 67-76.

DeMarco, T. Controlling Software Projects, Yourdon Press, New York, 1982.

Dillman, D. A. Mail and Telephone Surveys, John Wiley & Sons, New York, 1978.

Drummond, H. Escalation in Decision-Making: The Tragedy of Taurus, Oxford University Press, Oxford, 1996.

Festinger, L. A Theory of Cognitive Dissonance, Row, Peterson and Company, Evanston, IL, 1957.

Flowers, S. Software Failure: Management Failure, John Wiley & Sons, Chichester, 1996.

Garland, H. ìThrowing Good Money After Bad: The Effect of Sunk Costs on the Decision to Escalate Commitment to an Ongoing Project, Journal of Applied Psychology (75:6), 1990, pp. 728-731.

Garland, H., and Conlon, D. E. ìToo Close to Quit: The Role of Project Completion in Maintaining Commitment,î Journal of Applied Social Psychology (28:22), 1998, pp. 2025-2048.

Garland, H., and Newport, S. ìEffects of Absolute and Relative Sunk Costs on the Decision to Persist with a Course of Action,î Organizational Behavior and Human Decision Processes (48), 1991, pp. 55-69.

Ghiselli, E., Campbell, J., and Zedeck, S. Measurement Theory for the Behavioral Sciences, W. H. Freeman, San Francisco, 1981.

Glass, R. L. ìSoftware Runaways--Some Surprising Findings,î The DATA BASE for Advances in Information Systems (28:3), 1997, pp. 16-19.

Glass, R. L. Software Runaways, Prentice-Hall, Inc., Upper Saddle River, NJ, 1998.

Glass, R. L. Computing Calamities, Prentice-Hall, Inc., Upper Saddle River, NJ, 1999.

Harrell, A., and Harrison, P. ìAn Incentive to Shirk, Privately Held Information, and Managers' Project Evaluation Decisions,î Accounting, Organizations and Society (19:7), 1994, pp. 569-577.

Harrison, P. D., and Harrell, A. ìImpact of ëAdverse Selectioní on Managers' Project Evaluation Decisions,î Academy of Management Journal (36:3), 1993, pp. 635-643.

Jensen, M. C., and Meckling, W. H. ìTheory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure,î Journal of Financia Economics (3), 1976, pp. 305-360.

Jensen, M. C., and Meckling, W. H. ìTheory of the Firm: Managerial Behavior, Agency Costs, and Ownership Structure,î In Organizational Economics, J. B. Barney and W. G. Ouch (eds.), Jossey-Bass, San Francisco, 1986, pp. 214-275.

Johnson, J. ìChaos: The Dollar Drain of IT Project Failures,î Application Development Trends (2:1), 1995, pp. 41-47.

Kahneman, D., and Tversky, A. ìProspect Theory: An Analysis of Decisions Under Risk,î Econometrica (47), 1979, pp. 263-291.

Kanodia, C., Bushman, R., and Dickhaut, J. ìEscalation Errors and the Sunk Cost Effect: An Explanation Based on Reputation and Information Asymmetries,î Journal of Accounting Research (27:1), 1989, pp. 59-77.

Katz, D., and Kahn, R. L. The Social Psychology of Organizations, Wiley, New York, 1966.

Keil, M. ìPulling the Plug: Software Project Management and the Problem of Project Escalation,î MIS Quarterly (19:4), 1995, pp. 421-447.

Keil, M., and Flatto, J. ìInformation Systems Project Escalation: A Reinterpretation Based on Options Theory,î Accounting, Management and Information Technologies (9:2), 1999, pp. 115- 139.

Keil, M., and Mann, J. ìThe Nature and Extent of IT Project Escalation: Results from a Survey of

IS Audit and Control Professionals (Part 1),î IS Audit & Control Journal (1), 1997a, pp. 40-48.

Keil, M., and Mann, J. ìThe Nature and Extent of IT Project Escalation: Results from a Survey of IS Audit and Control Professionals (Part 2),î IS Audit & Control Journal (2), 1997b, pp. 66-69.

Keil, M., and Mann, J. ìUnderstanding the Nature and Extent of IS Project Escalation: Results from a Survey of IS Audit and Control Professionals,î in Proceedings of the Thirtieth Annual Hawaii International Conference on System Sciences (HICSS-30), Wailea, Hawaii, 1997c, pp. 139-148.

Keil, M., Mixon, R., Saarinen, T., and Tuunainen, V. ìUnderstanding Runaway Information Technology Projects: Results from an International Research Program Based on Escalation Theory,î Journal of Management Information Systems (11:3), 1995a, pp. 67-87.

Keil, M., and Robey, D. ìTurning Around Troubled Software Projects: An Exploratory Study of the Deescalation of Commitment to Failing Courses of Action,î Journal of Management Information Systems (15:4), 1999, pp. 63-87.

Keil, M., Truex, D. P., and Mixon, R. ìThe Effects of Sunk Cost and Project Completion on Information Technology Project Escalation,î IEEE Transactions on Engineering Management (42:4), 1995b, pp. 372-381.

Mann, J. The Role of Project Escalation in Explaining Runaway Information Systems Development Projects: A Field Study, Unpublished Ph.D. Dissertation, Georgia State University, 1996.

Mehler, M. ìReining in Runaways,î Information Week, December 16, 1991, pp. 20-24.

Morrison, D. G. ìOn the Interpretation of Discriminant Analysis,î Journal of Marketing Research (6), 1969, pp. 156-163.

Newcombe, T. ìBig Project Woes Halt Child Support System,î Government Technology, February 1998, pp. 34-35.

Newman, M., and Sabherwal, R. ìDeterminants of Commitment to Information Systems Development: A Longitudinal Investigation,î MIS Quarterly (20:1), 1996, pp. 23-54.

Rubin, J. Z., and Brockner, J. ìFactors Affecting Entrapment in Waiting Situations: The Rosencrantz and Guildenstern Effect,î Journal of Personality and Social Psychology (31), 1975, pp. 1054-1063.

Scholes, M. S. ìStock and Compensation,î The Journal of Finance (XLVI:3), 1991, pp. 803-823.

Singer, M. S., and Singer, A. E. ìIs There Always Escalation of Commitment,î Psychologica Reports (56:3), 1985, pp. 816-818.

Staw, B. M. ìKnee-Deep in the Big Muddy: A Study of Escalating Commitment to a Chosen Course of Action,î Organizational Behavior and Human Performance (16), 1976, pp. 27-44.

Staw, B. M., and Fox, F. V. ìEscalation: The Determinants of Commitment to a Chosen Course of Action,î Human Relations (30:5), 1977, pp. 431-450.

Staw, B. M., and Ross, J. ìBehavior in Escalation Situations: Antecedents, Prototypes, and Solutions,î in Research in Organizational Behavior, B. M. Staw and L. L. Cummings (eds.), JAI Press Inc., Greenwich, CT, 1987, pp. 39-78.

Tuttle, B., Harrell, A., and Harrison, P. ìMoral Hazard, Ethical Considerations, and the Decision to Implement an Information System,î Journal of Management Information Systems (13:4), 1997, pp. 7-27.

Tversky, A., and Kahneman, D. ìThe Framing of Decisions and the Psychology of Choice,î Science (211), 1981, pp. 453-458.

Whyte, G. ìEscalating Commitment to a Course of Action: A Reinterpretation,î Academy of Management Review (11:2), 1986, pp. 311- 321.

Willbern, J. A. ìRunaway Computer Systems, Best's Review (Life/Health) (89:9), 1989, pp. 90-92.

## About the Authors

Mark Keil is an associate professor in the Department of Computer Information Systems at Georgia State University. His research focuses on software project management, with particular emphasis on understanding and preventing software project escalation. His research is also aimed at providing better tools for assessing software project risk and removing barriers to software use. Professor Keilís research has been published in MIS Quarterly, Sloan Management Review, Communications of the ACM, Journal of Management Information Systems, Information & Management, IEEE Transactions on Engineering Management, Decision Support Systems, and other journals. He has served as an associate editor for the MIS Quarterly and currently serves on the editorial board of IEEE Transactions on Engineering Management and as co-editor of The DATA BASE for Advances in Information Systems.

Joan Mann is an assistant professor at Old Dominion University. She holds a Ph.D. in computer information systems from Georgia State University. Her research focuses on software project management and the management of information systems. Professor Mannís research has been published in the IS Audit & Control Journal, the Proceedings of the Hawaii International Conference on System Sciences, and the Proceedings of the Association for Information Systems.

Arun Rai is a professor in the Electronic Commerce Institute at Georgia State University. His research interests include emergent models of ebusiness and supply chain management, diffusion and impacts of information technology, knowledge management, and management of systems development. Professor Rai's research has been published in Accounting, Management and Information Technologies, Annals of Operations Research, Communications of the ACM, Decision Sciences, Decision Support Systems, Information Systems Journal, Journal of Management Information Systems, MIS Quarterly, Omega, and several other journals. He has served as an associate editor for MIS Quarterly and currently serves as an associate editor for Information Systems Research, Information Resources Management Journal, e-Services Journal, and The DATA BASE for Advances in Information Systems. Leading corporations, including A.T. Kearney, Bozell Worldwide, Daimler-Chrysler, Comdisco, IBM, and Scientific Atlanta, have sponsored his research work.

## Appendix A

# Survey Instructions for Selection of Escalated and Non-Escalated Projects

For the escalation survey, the specific wording used was:

This part of the survey is designed to collect information on your experience with a specific case of project escalation.

## Instructions

Please select a troubled project (abandoned or completed) which continued to receive resources [i.e. time, money] even though the project should have been discontinued or redirected. If you have never seen or been associated with a case of project escalation, please skip to Section 2 on the last page of the survey.

For the non-escalation survey, the specific wording used on the survey was:

This form is designed to collect information on your experience with a project that did not escalate.

## Instructions

Please select a completed project which progressed smoothly enough that you never thought it should be discontinued or redirected. If you have never been associated with a project that did not escalate, please skip to Section 2 on the last page of the survey.

When respondents reached the portion of the survey pertaining to escalation factors they were given the following instructions:

Here we are interested in the degree to which behavioral reasons might influence a decision maker to continue a project.

Subjects were then instructed to ìmark the Yes or No box to indicate whether the behavioral factor was present or notî and to check ìDonít Knowî if ìyou feel you donít have enough knowledge of the situation to respond.î The phrase ìPrimary Decision Maker(s)î which appears in the questionnaire items (see Appendix B) was defined as referring ìto the person(s) responsible for the decision to continue the project.î

## Appendix B

## Scale Items and Descriptive Statistics by Construct

## Which of the following problems were present in this project?

Need for Psychological Self-Justification

<table><tr><td>Variable</td><td>Mean</td><td>Std. Dev.</td><td>Item Wording $^{5}$ </td></tr><tr><td>PSJ_1</td><td>.860</td><td>.347</td><td>The Primary Decision Maker(s) repeatedly expressed support for the project</td></tr><tr><td>PSJ_2</td><td>.712</td><td>.453</td><td>The Primary Decision Maker(s) initiated the project or was extensively involved with it</td></tr><tr><td>PSJ_3</td><td>.387</td><td>.488</td><td>The Primary Decision Maker(s) seemed to be emotionally attached to this project</td></tr></table>

Need for Social Self-Justification

<table><tr><td>Variable</td><td>Mean</td><td>Std. Dev.</td><td>Item Wording</td></tr><tr><td>SSJ_1</td><td>.687</td><td>.464</td><td>Abandonment of the project would make the Primary Decision Maker(s) ‘look bad’ to others</td></tr><tr><td>SSJ_2</td><td>.395</td><td>.489</td><td>People inside or outside the organization viewed this project as the Primary Decision Maker(s)&#x27;s baby</td></tr></table>

Sunk Cost Effect

<table><tr><td>Variable</td><td>Mean</td><td>Std. Dev.</td><td>Item Wording</td></tr><tr><td>SC_1</td><td>.408</td><td>.492</td><td>The Primary Decision Maker(s) referred to past investments in this project as a reason to continue</td></tr><tr><td>SC_2</td><td>.423</td><td>.494</td><td>The Primary Decision Maker(s) used the attitude “there was too much invested to quit” to justify continuing the project</td></tr></table>

Goal Incongruency

<table><tr><td>Variable</td><td>Mean</td><td>Std. Dev.</td><td>Item Wording</td></tr><tr><td>GI_1</td><td>.356</td><td>.479</td><td>The Primary Decision Maker(s) acted out of self-interest rather than the interests of the organization when continuing the project</td></tr><tr><td>GI_2</td><td>.395</td><td>.489</td><td>The Primary Decision Maker(s) operated in an environment where “bad news gets you killed”</td></tr><tr><td>GI_3</td><td>.510</td><td>.501</td><td>Association with an unsuccessful project would have an adverse effect on the Primary Decision Maker(s) chance for advancement in the organization</td></tr></table>

Information Asymmetry

<table><tr><td>Variable</td><td>Mean</td><td>Std. Dev.</td><td>Item Wording</td></tr><tr><td>IA_1</td><td>.392</td><td>.489</td><td>The Primary Decision Maker(s) concealed negative information from top management</td></tr><tr><td>IA_2</td><td>.439</td><td>.496</td><td>The Primary Decision Maker(s) distorted negative information when reporting to upper management</td></tr><tr><td>IA_3</td><td>.542</td><td>.499</td><td>The Primary Decision Maker(s) put a positive spin on any negative project information when reporting to upper management</td></tr></table>

## Completion Effect

<table><tr><td>Variable</td><td>Mean</td><td>Std. Dev.</td><td>Item Wording</td></tr><tr><td>C_1</td><td>.560</td><td>.497</td><td>The Primary Decision Maker(s) exhibited the attitude “we have come too far to quit now” as a rationale for continuing the project</td></tr><tr><td>C_2</td><td>.438</td><td>.497</td><td>The Primary Decision Maker(s) exhibited the attitude “we are so close to the end of the project, we should keep going”</td></tr></table>

## Project Size

Compared to other IS projects undertaken in your organization, was this project...

<table><tr><td>Smaller (in size)</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>Larger (in size)</td></tr></table>

Mean response to project size: 4.124; Standard deviation: 1.656

## Appendix C

## Explanation of Relevant Statistics for Interpreting Logistic Regression Results

<table><tr><td>Statistic</td><td>Explanation</td></tr><tr><td>Cox &amp; Snell  $R^{2}$ </td><td> $R^{2} = 1 - [L(0)/L(b)]^{2/n}$ Where L(0) is the likelihood of the intercepts-only model, L(b) is the likelihood of the specified model, and n is the sample size. This measure achieves a maximum of less than 1 for discrete models, with maximum given by $R^{2}_{max} = 1 - [L(0)]^{2/n}$ </td></tr><tr><td>Nagelkerke  $R^{2}$ </td><td>This adjusted  $R^{2}$  measure differs from the Cox &amp; Snell  $R^{2}$  in that it can achieve a maximum value of 1. $R^{2}_{adj} = R^{2}/R^{2}_{max}$ </td></tr><tr><td>Wald statistic</td><td>The statistic is obtained by dividing the maximum likelihood estimate of the slope parameter by its standard error estimate. The resulting ratio, under the hypothesis that the coefficient of the slope parameter is zero, follows a standard normal distribution.</td></tr><tr><td>Odds ratio</td><td>This is a measure of association between the dependent variable and the independent variable. It represents how much more likely it is for the outcome to be present among those with presence of a certain condition.</td></tr><tr><td>-2 Log Likelihood</td><td>Assesses the significance of independent variables in the model in terms of their ability to reduce the sum of squared errors. The statistic follows a chi-square distribution.</td></tr><tr><td>Hosmer-Lemeshow statistic for goodness-of-fit</td><td>Cases are grouped into g groups based on values of estimated probabilities. Groups contain all subjects with estimated probabilities between adjacent cut-off points. The Hoshmer-Lemeshow goodness-of-fit statistic is obtained by calculating the Pearson chi-square statistic from the 2xg table of observed and estimated expected frequencies.</td></tr></table>

Keil et al./Software Project Escalation
