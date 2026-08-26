---
otero_id: 23458
otero_key: "GAFMBF78"
title: "An application of group decision support technology in collective bargaining"
authors: "Chang-Tseh Hsieh; Michael L Menefee"
year: "1991"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1991.31"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An application of group decision support technology in collective bargaining

CHANG-TSEH HSIEH

Management Information Systems, University of Southern Mississippi, MS, USA

MICHAEL L. MENEFEE

Pembroke State University, Pembroke, North Carolina, USA

Abstract: An enhanced distributive bargaining model is developed to be used as the foundation model of a group-decision support system for facilitating collective bargaining. The proposed system takes into account the multiple objectives decision process and is able to handle qualitative decision variables. The implementation of the proposed system can expedite bargaining and minimize the possibility of a work stoppage.

## Introduction

It has long been the goal of labour relations to expedite the settlement of collective bargaining agreements between unions and managements in order to minimize the probability of work disruptions by means of strikes or lockouts. The study of the collective bargaining process has been the focus of many previous reports, and is highlighted by the early works of Walton and McKersie (1965) and the more recent works of Kessler (1978), Fisher and Ury (1981), Pruitt (1981) and Lewicki and Litterer (1985).

According to Walton and McKersie, the collective bargaining process may be characterized by a behavioural theory of labour negotiations based on four bargaining models. They are

(1) The distributive model based on win-lose outcomes;

(2) The integrative model based on problem-solving outcomes;

(3) The attitudinal structuring model based on attitudinal change;

(4) The intraorganizational model based on selling the contract proposal to one's own side.

With the increased use of computer technology, more complex models have now been developed. Examples are the works of Mumpower and Zumbolo (1988) studying the roles of analytical mediation in negotiation; the works of Sycara (1988) dealing with multi-attribute utility theory in accommodating adversarial problem solving situations involving multiple interacting agents; and the works of

Montgomery and Benedict (1989) dealing with the projection of the probability and duration of strikes based on a set of explanatory factors.

Recent developments in Group Decision Support (GDS) technology may provide a vehicle for integrating all of the techniques addressed in previous studies, and consequently improve the efficiency of conflict resolution. With careful design and development, the GDS technology may eventually eliminate the need for lengthy formal collective bargaining and thus achieve more harmonious labour-management relationships in industry.

Since distributed bargaining (DB) is by far the most common approach to dealing with a conflict situation (Anson and Jelassi, 1989), it will be used as the foundation for this study. The DB model framework suggested by Walton and McKersie will be enhanced to deal with conflict situations involving multi-objectives. The revised distributive bargaining model will then become the basis for developing the Group Decision Support System (GDSS) for collective bargaining presented in this study.

The following section of this paper discusses the characteristics of the collective bargaining process. Next, the DB model suggested by Walton and McKersie will be reviewed, followed by a presentation of the enhanced distributed bargaining model. The feasibility of incorporating the GDS technology in the collective bargaining process will then be explored. A subsequent section describes the framework of the proposed GDSS for collective bargaining process together with a discussion on some special considerations for implementing the proposed system.

The paper ends with a summary of major findings and some suggestions about the direction for future study.

## Characteristics of collective bargaining process

Collective bargaining processes may be characterized by the following (Pruitt, 1981; Sparks, 1982; Jandt and Gillette, 1985; Sycara, 1988):

(1) The process involves several interactive parties. Typically, these include the unions, the company, some types of entity serving as the mediator, members of the union, and sometimes, local, state or even federal governmental agents as well as many other organizations in the private sector;

(2) Each party usually has multiple objectives to be accomplished. Many of the objectives of one party may conflict with the objectives of other parties;

(3) Negotiation is usually conducted on an issue-by-issue, or package-by-package basis. This means that both parties tend to focus on one bargaining issue (package) at a time, attempting to resolve it, then moving to the next issue on the agenda;

(4) Differences between two major parties (i.e. union and company) may be narrowed through the efforts of other involved parties, specifically the mediator;

(5) Settlement usually represents something that is less than the initial goals set by either party, but more than the other party would be willing to give;

(6) Not all decision factors can be quantified. Although monetary factors are the dominant determinants in most bargaining process, other non-numeric factors such as working conditions, safety, job security, etc., may also play important roles in determining outcomes of bargaining;

(7) Union members have the final say about the settlement reached during the bargaining process. Settlements reached in collective bargaining must be ratified by the majority of union members before it can become an official contract;

(8) Final settlement usually has to be reached in a short period of time. This involves the stress of decision making under threat as addressed by Gladstein and Reilly (1985).

The DB model suggested by Walton and McKersie may be used to illustrate some of these special features.

## Review of distributive bargaining process

According to Walton and McKersie, distributive bargaining is central to labour negotiations and is usually regarded as the dominant activity in the union-management relationship. Unions represent employees in the determination of wages, hours, and working conditions. Since these matters involve the allocation of scarce resources, there is assumed to be some conflict of interest between management and unions. The joint decision process for resolving conflicts of interest is distributive bargaining. The term itself refers to the activity of dividing limited resources.

This distributive bargaining process can be viewed in the context of a wage spectrum as illustrated in Figure 1 below.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
where:  $M_{ip}$  = management initial point
 $M_{tp}$  = management target point
 $M_{rp}$  = management resistance point
 $U_{rp}$  = union resistance point
 $U_{tp}$  = union target point
 $U_{ip}$  = union initial point
</div>

## Figure 1 The distributive bargaining model wage spectrum

On the management side an initial offer will be made. This is called the initial point $(M_{\mathrm{ip}})$ . This point is always low and serves as the starting point of the negotiations. Management then moves in negotiations to the target point $(M_{\mathrm{tp}})$ . The target point represents complete success in the negotiations (most optimistic outcome). This is the point where management would most like to see a settlement. As negotiations move upwardly past the target point, management approaches the resistance point $(M_{\mathrm{rp}})$ . When negotiations reach the resistance point, management realizes that only minimum success has been achieved. Thus the bargaining process slows down as the resistance point approaches and stops when the resistance point is reached.

The union process is common to the management experience and differs primarily in direction. The union will start out with a high demand as its initial point $(\mathrm{U}_{\mathrm{ip}})$ . The union will then concentrate on achieving its target point $(\mathrm{U}_{\mathrm{tp}})$ , which defines complete success for them. This is the point where the union gets all it expected to get from management. Then, the union moves slowly to their resistance point $(\mathrm{U}_{\mathrm{rp}})$ where they will not go any further.

The settlement range is defined as the area between the parties' respective resistance points. In the positive settlement range, the resistance points are compatible. In the range bounded by these two points, both parties would settle in preference to sustaining a work stoppage. The negative settlement range depicts the situation in which the resistance points are incompatible. There is no settlement which would be minimally acceptable to both parties. Thus, the probability of a work stoppage is greatly enhanced.

## Enhanced distributive bargaining process

The process described above is obviously oversimplified. In reality, a typical collective bargaining usually involves multiple objectives and a large number of interrelated factors. The objectives faced by both bargaining parties are often mutually exclusive. An appropriate approach to dealing with such a situation may be through the analysis of the utility functions of both parties.

The concept of utility may be defined as a measure of an individual decision-maker's preference for selecting among future alternatives (Knowles, 1989). Each of these alternatives represents a certain combination of the values of the decision variables. For simplicity, consider a conflict situation involving two aggregated factors, Q1 and Q2. Here, Q1 represents the maximum possible value of the aggregated monetary variables and Q2 represents the maximum possible value of the aggregated non-monetary variables.

The utility curve for each party would be a function of the values of Q1 and Q2 that the party expects to obtain. Assuming decision makers in both parties are risk-averters, the initial position for union and management may look like the utility curves, $U_{u}^{0}$ and $U_{m}^{0}$ , as shown in the Edgeworth Box Diagram below.

![](/api/attachments/GAFMBF78/fulltext/images/b6f9915cd4a72b41c47ac618a022313a0a991405df4443ec1d94239f84ae0b0e.jpg)  
Figure 2 Possible initial utility curves

Management's position is to minimize the values of Q1 and Q2, while the union is seeking to maximize them. However, in order to get a higher value on one factor, a decision-maker has to accept a lower value on another.

As indicated by the curve $U_{u}^{0}$ , the union's initial position would be to negotiate a contract to include as much Q1 as possible. However, the union would be willing to trade some Q2 for Q1. But the value on Q1 would not be reduced to lower than $q_{1}^{0}$ . The curve $U_{u}^{0}$ thus represents all possible combinations of the values on Q1 and Q2 which will yield the same degree of satisfaction to the union. This curve is commonly referred to as the indifference curve. Curve $U_{m}^{0}$ thus represents the initial indifference curve for management. The shape of the curve, however, could be concave, convex, or straight depending upon the substitute effect between Q1 and Q2 as perceived by the decision makers.

As stated in the classical distributive bargaining process, both union and management also set a target point. Utility curves for the target points of both parties would be parallel to the initial curves. These are represented by $U_{u}^{*}$ and $U_{m}^{*}$ , respectively for union and management in Figure 2. For union, $U_{u}^{0}$ represents a level of satisfaction higher than that represented by curve $U_{u}^{*}$ . But even $U_{u}^{*}$ is still too high to be arrived at during collective bargaining.

The same is true on the management side. The target point $U_{m}^{*}$ represents complete success in the negotiations. This is where the management would most like to see a settlement. However, the union would like the settlement to be in their favour, and its target is $U_{u}^{*}$ . Therefore, final settlement would be somewhere between $U_{u}^{*}$ and $U_{m}^{*}$ . The area bounded by the curves $U_{u}^{*}$ and $U_{m}^{*}$ thus represents the settlement area. The following diagram (Figure 3) illustrates some possible settlements. Management

![](/api/attachments/GAFMBF78/fulltext/images/edb835277f67daf824e8cf78be50a628415fbd4826b83d19acbdf8e1eb0baf81.jpg)  
Union Figure 3 Examples of settlement

Point E is the tangent of two utility curves $U_{m}^{e}$ and $U_{u}^{e}$ . This point represents the lowest level of satisfaction that both parties would be willing to take. The settlement, as represented by the point E, consists of a value $q_{1}$ for aggregated monetary factors and a value $q_{2}$ for aggregated non-monetary factors. This settlement is the well-known Pareto Optimality.

Clearly, shapes of the utility curves and the bargaining power of each party will affect the position of point E. For example, point $E_{1}$ in Figure 3 represents a Pareto optimal settlement based on another set of utility curves with the union overpowering management. Another point $E_{2}$ represents another possible settlement where union and management both have a perception of the importance of Q1 and Q2 differently from that represented by points E and $E_{1}$ , and management has a better bargaining position than the union.

This enhanced distributive bargaining model is independent of the number of decision variables involved and is a better tool for dealing with the complex collective bargaining process. This enhanced DB model becomes the foundation for setting up the model base of the proposed GDSS.

## Roles of GDSS technology

GDSS may be defined as an information system consisting of software, hardware, and language components and procedures that support a group of people engaged in a decision meeting. It is an interactive, computer-based system which would facilitate the solution of unstructured problems by a group of people engaged in a decision-related meeting. (Huber, 1984, DeSanctis and Gallupe, 1987).

![](/api/attachments/GAFMBF78/fulltext/images/e7ee98525ec7f7f3503498a839f976405bde85d6bd2775fb9d18ead6e63e49a9.jpg)  
Figure 4 A model of GDSS

Typically, a GDSS will include sophisticated hardware, appropriate softwares, people, and procedures. The conceptual structure of a multiple-party GDSS is illustrated in Figure 4 (DeSanctis and Gallupe, 1985).

The group facilitator in Figure 4 plays the role of mediator in the bargaining process. The mediator may be an individual or a group of experts accepted by both parties. Major functions to be performed by the mediator are:

(1) Deriving utilities of both parties. This may be done by surveying negotiators of each party, referencing the records of similar parties from past successful conflict resolution, or applying the appropriate mathematical model using knowledge of domain-specific factors;

(2) Monitoring the shift of utility curves. Upon receiving inputs from either or both parties, the effect of these inputs on the shape and position of utility curves will be quickly estimated and passed on to negotiators.

(3) Assisting the determination of factors weights. The mediator will help decision-makers of either or both parties to reach the agreements on the priority of all involved decision factors through analytic hierarchy process (AHP).

(4) Facilitating the arrival of compromised solution.

When negotiations seem stalled, a compromised solution could be generated and suggested to both parties to initiate next stage negotiations.

The first two functions will be handled by the enhanced distributivebargaining model as described in the previous section. The appropriate software package such as Criterium and Expert Choice will be incorporated into the model base of the proposed system to deal with ranking decision variables and assigning appropriate weights to these factors\*.

Additional models will be developed and included in the model base to handle (1) optimization analysis using goal programming techniques, (2) sensitivity analysis, and (3) simulation. Other models may be added to this component of the system whenever they become necessary.

In addition to models in model base components, the proposed GDSS also needs the appropriate databases and state-of-the-art database management which can handle queries from all participants in a very efficient manner. A separate database will be needed for each party.

On the union side, data should focus on the current economic situation and economic future of the company. The union needs to know about the financial and non-financial aspects of the company. Such information can be obtained in several different sources such as 10K reports, value line data base, stockholder reports and updates, pro forma statements, newspaper articles, press releases, and public record information from open hearings, etc. (Cantrell, 1984).

Data pertaining to general economic trends might include interest rates, gasoline prices, cost of raw materials, or other items affecting the particular company. Economic forecasts as to the unemployment rate and consumer price index would also prove useful in such issues as wage increases and cost of living adjustments, and should also be maintained in the database, and be constantly updated. An example of a union database and its relationships with goal set-up is given in Figure 5.

On the management side, an existing database pertaining to current and future conditions of the company could be linked to the proposed GDSS. Additional data focusing on the union such as financial structure of the union, attitudinal analysis of union members, union leaders' personal profiles, etc. may also be maintained. This would help management to simulate the movement of union negotiators. Its database would have a relationship with the goal set-up similar to that illustrated in Figure 5.

Both databases will be linked to some type of group server (possibly a powerful minicomputer system) which contains appropriate software to enable members of each party to conduct simulation, projection, and sensitivity analysis. The group server may also be used as the front-end processor to handle the communication between negotiators and other individuals who may be affected by the resolution. On the union side, these would be members of each local union. On the management side, these could be the decision makers at all management levels. The proposed GDSS for supporting the collective bargaining process would thus have a framework as illustrated in Figure 6.

The proposed GDSS would be able to increase the efficiency and effectiveness of the collective bargaining process by performing the following functions.

(1) Facilitate the arrival of consensus among union members when determining the weights for all involved decision factors;

(2) Enable the translation of qualitative variables into appropriate quantitative measures through an analytic hierarchical process;

(3) Estimate the initial and target utility functions for both parties;

(4) Conduct hierarchical analysis to rank decision variables based on group input;

(5) Allow multiple objectives and constraints to be analysed simultaneously;

(6) Identify the target settlement area, and direct negotiations toward this area;

(7) Analyse changes in shape (slope) of utility curves instantly upon receiving inputs from negotiations;

(8) Generate alternatives based on changes in utility curves to provide negotiators with up-to-the-minute information on ways to converge at a settlement point;

(9) Assist negotiators of either party to conduct 'what-if' analyses based on a set of assumptions regarding the different issues in the bargaining agenda;

(10) Increase the efficiency of ratifying the final contract.

In addition, typical features of a GDSS will naturally be incorporated into the built-in mechanisms of the proposed system (DeSanctis and Gallupe, 1985). These include

(1) Numerical and graphical summarization of group members, ideas, and votes;

(2) Anonymous recording of ideas, formal selection of a group leader, elimination of redundant input during brainstorming;

(3) Text and data transmission among all individuals involved in decision process.

![](/api/attachments/GAFMBF78/fulltext/images/3cf5c3716678f62f1061283d2c559f1d98c79607e7e0fe417a86d3336d0ba61e.jpg)  
Figure 5 Example of union database and its relationships with goal set-up

## Implementation considerations

Recent advancement in hypermedia technology will greatly enhance the power of the proposed system. The hypermedia technology would allow different types of input/output methods including voice, video, graphics, text, etc. to be integrated in the process of negotiations. It will also increase the efficiency of interfacing with different types of databases (voice, text, numeric, etc.). It will eventually replace the traditional user-interface technology in most sophisticated decision support systems, and is indicated in Figure 6 to handle user interface for the proposed system.

The implementation of the proposed system can mean a major capital investment to any party involved in collective bargaining. In reality, collective bargaining will not be a frequent event between two parties. Judging from the facts that the proposed system is independent of the types of issues, number of objectives, and bargaining parties, a permanent site for maintaining the proposed system would be the ideal solution.

The GDSS facility installed at the University of Arizona may be used as the blueprint to design the facility for multiple-party conflict solution $^{†}$ . Funding may come from government and/or all interested parties. The neutral position of the system, however, must be preserved. With these implementation considerations taken into account, the future of this proposed GDSS for supporting collective bargaining should be very promising.

![](/api/attachments/GAFMBF78/fulltext/images/c285c843b364fd3ea44c52a0b4ff9ee0cbc3dde456cfa3ddd19eb1c5ef68fca4.jpg)  
Figure 6 Framework of the proposed GDSS

## Concluding remarks

In this study, an enhanced distributive bargaining model has been developed, and is proposed to serve as the foundation model for a group decision support system (GDSS) for facilitating collective bargaining.

This enhanced model takes into account the fact that multiple objectives are typically involved in collective bargaining, and that the objectives may be both quantitative and qualitative.

It has been indicated in this study that an appropriately developed GDSS can expedite bargaining and minimize the possibility of a work stoppage. It should be noted that a GDSS is only a tool in the collective bargaining arena. The real decisions and final agreement are made by people. The system, however, is able to enhance the skills and expertise of the negotiators.

As suggested by Cantrell (1984), whenever a negotiation breakdown is inevitable, or when grievance cannot be resolved, the use of computer technology, especially a system such as the one proposed in this study, could be the right tool to melt the ice. In the future, a prototype of the proposed GDSS will be developed to empirically test the limit of the power of the proposed system.

## References

Anson, R. and Jelassi, M.T. (1989) A Development Framework for Computer-Supported Conflict Resolution, INSEAD Working Papers, No. 89/42.

Cantrell, D. (1984) Computers come to the bargaining table. Personnel Journal, 63, 27–30.

DeSanctis, G. and Gallupe, B. (1985) Group decision support systems: a new frontier. DATABASE, 17, 3–10.

DeSanctis, G. and Gallupe, B. (1987) A foundation for the study of group decision support systems. Management Science, 33, 589–609.

Fisher, R. and Ury, W. (1981) Getting to Yes: Negotiating Agreement Without Giving In (Penguin, New York)

Foroughi, A. and Perkins W. (1989) An empirical study of the effects of computer negotiation support systems (NSS) on negotiation outcomes and negotiation attitudes. Proceedings of 1989 Decision Science Institute Conference New Orleans, LA, pp. 648–650.

Fraser, N. and Hipel, K. (1981) Computer assistance in labor-management negotiations. Interfaces, 11, 22–29.

Gladstein, D. and Reilly, N. (1985) Group decision making under threat: the tycoon game. Academy of Management Journal, 28, 613–627.

Golden, B. Wasil, E. and Harker, P. (eds) (1989) The Analytic Hierarchy Process: Applications and Studies (Springer-Verlag, Berlin,)

Gray, P. and Nunamaker, J. (1989) Group decision support systems, in Decision Support Systems, Sprague, R. Jr. and Watson, H. (eds) 2nd edition, (Prentice-Hall, Englewood Cliffs, N.Y.)

Harker, P. (1990) Review of Criterium OR/MS Today, 17,

Huber, G. (1984) Issues in the design of GDSS. MIS Quarterly, 7, 195–204.

Jandt, F. and Gillette, P. (1985) Win-Win Negotiating: Turning Conflict into Agreement (John Wiley & Sons, New York).

Jelasi, M. T. and Jones, B. (1988) Getting to yes with NSS: How computers can support negotiations, in Organizational Decision Support Systems, Lee, R.M., McCosh, A.M. and Migliarese, P. (eds). (North-Holland, Amsterdam).

Kessler, S. (1978) Creative Conflict Resolution: Mediation Leader's Guide (National Institute for Professional Training, Fountain Valley, CA.)

Knowles, T. (1989) Management Science: Building and Using Models (Irwin, Homewood, Illinois).

Lewicki, R. and Litterer, J. (1985) Negotiation (Irwin, Homewood, Illinois).

Montgomery, E. and Benedict, M. (1989) The impact of bargaining experience on teacher strikes. Industrial and Labor Relations Review, 42, 380–392.

Mumpower, J. and Zumbolo, A. (1988) Analytical mediation: an application in collective bargaining, in Organizational Decision Support Systems, Lee, R.M., McCosh, A.M. and Migliarese, P. (eds.) (North-Holland, Amsterdam).

Pruitt, D. (1981) Negotiation Behavior (Academic Press, New York)

Sparks, D. (1982) The Dynamics of Effective Negotiations: A Win-Win Approach to Getting What You Want, (Gulf Publishing) Houston, Texas.

Sycara, K. (1988) Utility theory in conflict resolution. Annals of Operations Research, 12, 65–84.

Walton, R. and McKersie, R. A Behavioral Theory of Labour Negotiations (McGraw-Hill, New York).

## Biographical notes

Chang-tseh Hsieh, PhD, is Associate Professor of Management Information Systems at the University of Southern Mississippi. He received his MBA from the University of Southern Mississippi and his PhD from Purdue University. His current interests are in applications of group decision support technology and database management. He has published papers in Journal of Information Systems Management, Journal of Computer Information Systems, Journal of Financial Research and other journals.

Michael L. Menefee, PhD, is currently the William Henry Belk Distinguished Professor of Business Administration at Pembroke State University. He received his BS from Northern Illinois University and his MS and PhD from Purdue University. His current research interests are in labour relations and personnel and business strategy.

Address for correspondence: Chang T. Hsieh, University of Southern Mississippi, Box 10064, Southern Station, Hattiesburg, MS 39406, USA.
