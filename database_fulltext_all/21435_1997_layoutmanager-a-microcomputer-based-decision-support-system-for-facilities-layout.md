---
otero_id: 21435
otero_key: "95J5Q8VZ"
title: "LayoutManager: A microcomputer-based decision support system for facilities layout"
authors: "L.R Foulds"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00003-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# LayoutManager: A microcomputer-based decision support system for facilities layout

L.R. Foulds $^{1}$

Department of Management Systems, University of Waikato, Private Bag 3105, Hamilton 2020, New Zealand

## Abstract

A user-friendly, menu-driven decision support system (DSS) for facilities layout design is described. It provides for the choice between a variety of productivity criteria. The system is written in Pascal, within the Microsoft Windows environment, for an MS-DOS personal computer. A case study, involving the successful use of the system which motivated its development, is also mentioned.

The system provides a useful addition to the facilities planner's toolkit and an interesting application of the DSS approach in a new area. © 1997 Elsevier Science B.V.

Keywords: Facilities layout; Decision support system; Microcomputer applications; Case study

## 1. Introduction

Facilities layout, an important research topic in physical systems design, has received much recent attention from production engineers and others. This is due, in part, to increased global competition in manufacturing, which has spurred renewed efforts to reduce manufacturing costs. Efficient and effective physical layout is critical in the ability to achieve and maintain manufacturing competitiveness. Indeed, Tompkins and White [1] reinforced this point by observing that up to half of the operating costs in a manufacturing system are related to materials handling and layout. These concepts are interrelated, as improved layout design often brings about reductions in the costs of materials handling, transportation, congestion, and work-in-process. The resulting benefits in productivity have been summarized by Sule [2].

Recent advances in the field of facilities layout have been reported by Heragu [3] who surveyed recent models and techniques in a special issue of the European Journal of Operational Research, which was dedicated to facilities layout. It also contains the following articles: Chajed et al. [4] concentrated on the flow network component, Askin and Mitwasi [5] integrated layout with process selection and capacity planning, van Camp et al. [6] presented a nonlinear optimization approach, Heragu and Alfa [7] and Kouvelis et al. [8] experimented with simulated annealing algorithms, Ram and Viswanandham [9] considered the layout of flexible manufacturing systems, Sarin et al. [10] presented a multi-attribute decision-theoretic approach, Leung [11] described a graph-theoretic heuristic for designing loop-layout manufacturing systems, Rosenblatt and Golany [12] devised a distance assignment approach, and Urban [13] and Balakrishnan et al. [14] considered dynamic problems.

![](/api/attachments/95J5Q8VZ/fulltext/images/68413fe014661d40d703854b3a289f3378f1bfc3853bebb7dbf82706e6e91f41.jpg)  
Fig. 1. A typical block plan.

We concentrate on layout design with the aim of producing a scale plan (called a block plan, of the type illustrated in Fig. 1) of the physical system to be designed. This is a specialized, but important, concern within the more general endeavour of manufacturing systems design. We are concerned with the physical arrangement of a given number of facilities, of known area but of arbitrary shape, within a given configuration. Classical approaches to this endeavour, as described by Foulds [15], have adopted a single optimality criterion, based on either qualitative relationships between facilities or quantitative transportation costs, without the possibility of user interaction or experimentation. In contrast, Harmonosky and Tothero [16] developed a multi-factor plant layout methodology. The theme of multi-criteria decision-making (MCDM) techniques in layout has been discussed at length by Malakooti et al. [17–20] and by Jacobs [21]. The approach taken by these authors differs from that of the present paper in that they tackle an objective, which is a weighted combination of adjacency scores and transportation costs, by MCDM methods.

Here we present a decision support system (DSS) for facilities layout which is user friendly and menu driven. It is based on various models, which are described elsewhere by Hassan and Hogg [22], Foulds et al. [23], Foulds and Giffin [24,25], and Watson et al. [26]. The basic elements of the facilities layout design environment that give rise to this research are given in Section 2. A rationale for using a DSS approach is given in Section 3. In Section 4 we discuss why we decided to develop a DSS for our clients and how we came to understand their needs. The DSS, called LayoutManager, is detailed in Section 5. We present a summary and our conclusions in Section 6.

## 2. A facilities layout design environment

## 2.1. Background

Computer Automation (Ireland) Ltd. (CAIL) is a manufacturer of printed circuit boards and commercial and industrial computers located on an industrial estate in Dublin, in the Republic of Ireland. Recently the company began experiencing difficulty in matching the productivity of its rivals in the highly competitive microcomputer manufacturing market.

After considerable examination, it became increasingly clear to the management that part of the cause of the decline in productivity was due to inefficiencies in the mechanical assembly (MA) area, where the computer parts are actually put together to create the final products. It became obvious that a significant problem in MA was caused by the travel of workers, parts, and equipment necessitated by the assembly sequences. The total distances travelled by each of the categories just mentioned were grossly excessive, due to poor spatial allocation of the MA operations and facilities. We now explain the relevant details of the assembly process.

## 2.2. The assembly process

A typical layout of the MA area is shown in Fig. 2. Basically, three main activities take place in the area: the processing of incoming kits of parts, the assembly of the final products, and some testing of these products. The MA area comprises twelve facilities (either activities or physical resources), one of which is the region exterior to MA. This “exterior” facility is included because it is important that certain MA facilities are located adjacent to the perimeter of the MA area so that they are relatively close to certain facilities beyond the MA area. These external facilities (shown as columns) and their relationships with the MA facilities (shown as rows) are listed in Fig. 3.

There are two distinctive features of the MA

![](/api/attachments/95J5Q8VZ/fulltext/images/2f6ed0013fa231471d7d7fc7682c9567be2f8f4bfd68f68e004a654cb419cd41.jpg)  
Fig. 2. A typical layout of the MA area.

process that have important implications for the layout design exercise at hand. First, there is a high variance in the numbers and types of products that must be assembled over quite brief time intervals. A typical product mix is shown in Fig. 4. Second, this variance necessitates the use of a variety of markedly different criteria (discussed later) by which the productivity of the MA area is judged.

![](/api/attachments/95J5Q8VZ/fulltext/images/9f1e9c198ea060fea2ba1897d88509955debfe201dc73ee298b7bafa6e4bdf59.jpg)  
Fig. 3. The relationship between the MA area and the rest of the factory.

![](/api/attachments/95J5Q8VZ/fulltext/images/0238947ea5e409df757c5d73d1e73812f032d219e5960cf5f2ed387ba5f9c589.jpg)  
Fig. 4. A typical product mix.

Also, the use of the facilities, and the numbers of trips between them, required by product assembly, varies drastically between products. Of course, these numbers have a direct bearing on the effectiveness of any layout. These factors demand a high level of fluidity and flexibility in MA layout if the productivity of the area is to be consistently high.

This can be achieved if MA facilities can be relocated relative to each other quite easily via facility wheels and trolleys. This is crucial to maintaining high productivity when the product mix, or levels within it, change significantly.

The most effective (temporary) layout for the current production schedule was traditionally found by shuffling templates. However, rapidly increasing changes in the schedule rendered this approach less and less effective. It was then that the management invited the author to study the MA operation in order to recommend areas for improvement in its physical layout.

Recognizing the importance of judgemental considerations and the need for rapid layout design decisions in a volatile environment, we felt that current layout computer programs offered little benefit. Instead, we decided to develop a DSS to address the MA layout design issue.

## 2.3. Productivity criteria

One of the first tasks in this development was to establish appropriate criteria by which the productivity of layouts can be judged. Different product mixes and levels require different criteria, involving factors of facility adjacency and transportation times.

## 2.4. Criterion Cl

One common set of mixes involve both few facilities and a multitude of qualitative considerations. The criterion (denoted by C1) selected for this set was the maximization of the total adjacency score of potential layouts. Here, an adjacency score is defined for each pair of facilities; the higher the score the more desirable it is that the pair be located adjacently in the layout. An adjacency score for any potential layout is calculated by summing the scores of all pairs of facilities that are adjacent in the layout.

## 2.5. Criterion C2

The previous criterion measures the utilization of a potential layout based only on its physically adjacent facilities. This is an inadequate measure for product mixes whose production requires the use of most, or all, facilities. In this case it is better to consider the effect of nearly adjacent facilities as well. In this case the criterion that was selected (denoted by C2) is an extension of the last, in the sense that the layout score is the sum of the adjacency scores of all pairs of facilities. The adjacency score of any pair of facilities is based on the least number of facility boundaries that must be crossed in the potential layout in order to travel between them.

## 2.6. Criterion C3

Although the previous criterion takes into consideration how close facilities are to each other in terms of adjacency, it does not consider the time taken to travel between them. This is the most important factor in the remaining set of mixes, where quantitative rather than qualitative factors are more important. Thus the final criterion (denoted by C3) considers the cost of transportation between all pairs of facilities, in terms of travel time. The objective is to minimize the total time of all travel.

CAIL staff felt that the above criteria are sufficiently broad to measure effectively the utility of potential layout designs. They did not believe it was necessary to incorporate other considerations, such as initial set-up costs, plan complexity, or detailed relationships with the region outside MA. There was little incentive to include set-up costs as the MA workers are a close-knit, experienced team who are well versed in the efficient relocation of their facilities within the MA area. These facilities had long since been fitted with wheels, or placed permanently on trolleys so that capital and set-up costs are minimal. Because MA is relatively small in area, does not contain many facilities, and involves only a very limited number of layouts that reoccur on a routine basis, layout complexity was not an issue.

To cope with the different facilities in the external region (depicted as columns in Fig. 3) having various relationships with the MA facilities, it is sometimes desirable to subdivide the external region into a number of facilities, which are treated separately in the layout design process.

There is the possibility to combine, in the form of a weighted sum, the criteria just identified, as espoused by Malakooti et al. [17-20] and Jacobs [21]. We, however, resisted this temptation on both theoretical and practical grounds. Hall [27] has identified a number of as yet unresolved, theoretical objections to this approach, including the devising of suitable common scales and units of measurement which satisfactorily reflect the aggregation of criteria. An example of this dilemma can be seen in the design of an emergency ward in a hospital. Aggregating say, adjacency criterion for care of critically ill patients and a criterion for cleaners' travel may be not only meaningless but irresponsible.

Fortunately, in MA at CAIL, natural, single criteria are evident for each product mix category and there is no need to enter the treacherous waters of “adding apples and oranges”.

On another matter, the deployment of the MA facilities is quite flexible in the sense that there are no fixed areas or corridors. Rather, the facilities are all mobile. Thus, the question of good layout design comes down to identifying temporary floor positions so that efficient clusters of adjacent facilities promote effective manufacture of the product mix at hand. For this reason it was decided not to adopt the approach of Jacobs [21] which allows for fixed areas or areas of definite shape (e.g. corridors); in MA they do not exist.

We now go on to discuss the basic concepts and use of DSSs in order to motivate their use as a solution approach to the problem in hand.

## 3. The DSS approach

The DSS has emerged as a computer-based approach to assisting decision makers (including manufacturing engineers) to address semistructured problems by allowing them to access and use data and analytic models (Turban [28] and Young [29]). Such systems have the following characteristics: they are interactive computer-based systems, they are aimed at semistructured problems, they utilize models with internal and external databases, and they emphasize flexibility, effectiveness, and adaptability. These characteristics have guided much of the research in the DSS area, but the potential benefits of the DSS in the business environment have not yet been fully realized. Nevertheless, many successful DSS applications have been reported in the literature (see for example, Arinze et al. [30] and Couillard [31]). Most of these applications are either large-scale systems built to facilitate well-defined and repetitive decision tasks, or else they are small PC-based systems offer ing quick and economic routines to support one-time decision making (Islei et al. [32]). This paper describes a PC-based DSS which addresses a non-routine and ill-defined decision environment, i.e. facilities layout design.

Although the definition of the DSS concept has been elusive (see for example, Bonczek et al. [33] and Er [34]) the field has flourished with the development of computer technology. Keen [35] reviewed a decade of DSS development and concluded that there is a need for a balance between each of the three DSS elements: decision, support, and systems. He felt that more research effort on the decision component was required to restore this balance, as the technology for the system component was no longer the bottleneck. To achieve the “mission of DSS—helping people make better decisions”, Keen stressed the need for an active supporting role for “decisions that really matter”. This paper focuses on the decision component of the DSS.

PC technologies are becoming accepted and incorporated into organizations and our personal lives. PC-based systems have the potential to improve both individual and organizational performance. As decision makers recognize the potential benefits, many companies are investing in information technology. PC-based systems have been generally hailed as a revolution that will change the nature of professional work and transform the way most professional people function in their jobs. It is expected that almost all knowledgeable workers are likely to have their own PC to perform both stand-alone tasks and network services in the near future. Despite the proliferation of microprocessor-based systems, the potential benefits of these systems as aids to decision making have not been fully realized, due to poor design and low acceptance by users. It is recognized that individuals are sometimes unwilling to use these systems, even if they may increase their productivity. While some DSSs may have an impact on individuals and organizations, the adoption and acceptance of these systems among decision makers has been limited. This may be due to the inflexibility in the systems as well as their narrow design. Therefore, it is important to understand the environment of the decision makers and the type of support they need in order to make effective decisions, and to examine the models appropriate for addressing their problems.

We shall now discuss the DSS that was designed to aid the layout planners in the MA area at CAIL.

## 4. The development of the DSS

As has been stated, the MA layout planners have traditionally shuffled templates in order to identify a suitable layout for the next product mix to be manufactured. Therefore, in order to gain acceptance, it was imperative that the DSS displayed colour-coded blocks, drawn to scale, representing the facilities. The relevant data and information were represented by using a colour graphics-display system with windows and pull-down menus. This allows a complementary combination of skills. The planners have the skill, superior to that of the computer, to recognize patterns in the potential layouts that the DSS creates. Based on these patterns, the planners can modify the layouts. The use of a computerized layout display permits the computer to present immediately to the planner the consequences of these options. The planner then chooses an option, and the computer updates the layout. Such a planner-computer combination marries the pattern recognition skills, specialized knowledge, and inspiration of the experienced planner, along with the numerical, graphical, and recall ability of the computer.

To develop the DSS, we held a series of discussions with the layout planners and other individuals involved, over a significant period of time. This helped us to understand their needs and requirements. In order to meet the planners' needs and requirements and follow their decision-making processes, desirable main-menu functions of a DSS were developed. The following functions are needed by the planners to identify the requirements of a new product mix and to create a satisfactory new layout to meet its demands.

(1) File open/close. In order to begin the process of new layout generation, based on a previous layout, the planners must first be able to access the previous layout. Planners should be able to open and manipulate all the data files, including facilities, areas, traffic, and criteria.

(2) Layout checking. There should be some means whereby the planner can ascertain how well a layout will meet the requirements of the planners. A layout may be checked for facility shape, convenience, safety, and productivity criteria (including manufacturing time and distance travelled).

(3) Layout modification. Having pinpointed where an existing layout is deficient, the planners must then devise modifications to it which produce a satisfactory new layout. The system must allow for modification of existing layouts by such means as altering:

\- MA area shape,

\- facility shape,

\- adjacency structure,

\- which facilities are adjacent to the area perimeter,

• minimum facility width,

\- minimum pair-wise facility boundary overlap for useful adjacency of each pair of facilities.

These functions should be guided by the provision of relevant criteria, including the productivity criteria. Naturally, there must be a mechanism whereby the new layout can be recorded.

It is also desirable that the DSS can be used to respond to enquiries and to address questions concerning changes: the facilities used, the product mix, the product levels, adjacency desirability ratings, and transportation times. Often these changes trigger not merely a modification of an existing layout, but rather the construction of a complete new layout from scratch. This is appropriate in a start-up situation, or when there are significant changes in the conditions or data which make a rationalization of resources desirable. This task can often be aided by carrying out systematically the clustering of facilities into “super” combined or nested facilities.

We now introduce the system structure of the DSS named LayoutManager, which was developed for use by the layout planners at CAIL.

## 5. LayoutManager

LayoutManager is a user-friendly menu-driven DSS for facilities layout design which can accommodate the criteria and models previously referred to and implements routines to output a colour-coded, labelled block plan. LayoutManager has three components: the user interface, the modelling base, and the database. The structure that integrates these three components is shown in Fig. 5. The system outputs a colour-coded block plan. It comprises pull-down menus, windows which display the input data, and is user friendly and mouse driven. It can be used to create new or to improve existing block plans. The menu options available are shown in Fig. 6. The pull-down menus give access to the modules. Each module includes a secondary menu of procedures. All procedures are independent and can be used in any order. All data can easily be stored for further processing.

## 5.1. The database component

The system maintains a database of the names, shapes, areas, minimum width, and colour references of facilities; adjacency scores, transportation times, production flows, and productivity criteria. This database can be interactively entered and updated. It can be easily accessed and manipulated through a File module, which is described later.

The user provides LayoutManager with a particular scenario to analyse by loading a standard ASCII text file that must provide all the necessary information. Input files may be created and edited with any suitable text editor or they can be created and edited with the built-in editor. The input file must specify the productivity criterion to be adopted and the number of facilities to be considered, including the exterior facility. There is a soft limit imposed by the program of 40 facilities. This limit may be increased through recompilation if necessary, provided the additional computer memory requirement is available.

![](/api/attachments/95J5Q8VZ/fulltext/images/8446034ce318ddeae645bbd83910350c037366d94fa00977b504cef8155fcf4e.jpg)  
Fig. 5. The component structure.

<table><tr><td>File</td><td>Apply</td><td>Improve</td><td>View</td><td>Options</td></tr><tr><td>Load...Save as...Save Plan...Load Plan...PrintClear</td><td>HeuristicEdit</td><td>Improve AllImprove OnceReplace EdgeRelocate Vertex</td><td>ScoreEditKeyRedraw</td><td>Shape...Set AEIOUX...</td></tr><tr><td>ExitAbout...</td><td></td><td></td><td></td><td></td></tr></table>

Fig. 6. The menu options.

For productivity criteria C1, for each pair of facilities, an adjacency rating is required. For criteria C2, relationship charts are required for each distance (facility boundaries to be crossed in travelling between facilities) from 1 to $((n-2)/3)+1$ where n is the number of facilities. For any given pair of facilities the adjacency rating can be specified as a floating point number, allowing the user to define exactly the input parameters. When the measure is less precise and only a rough estimate of closeness is available, the user can specify the adjacency rating using a restricted set of values represented by the letters A, E, I, O, U and X, which represent actual floating point values in decreasing order. Here A represents the highest value and most desirable closeness and X represents the lowest. The user may specify, in the input file or interactively, the equivalent floating point value for each letter. Default values of 64.0, 32.0, 16.0, 4.0, 1.0, 0.0, and -1024.0 will be assigned to A, E, I, O, U, and X respectively if no values are specified. The large default negative value of the letter X is designed to be used for facility pairs whose adjacency is infeasible. The representations are loaded in by LayoutManager and are internally converted to the equivalent floating point value, but are still viewed as letter values.

For criteria C3, a from-to chart specifying the traffic between each pair of facilities is required.

To generate a block plan, we require the area of each facility. Areas are expressed as positive floating point values. A unique name must be assigned to each facility so that it can be identified.

An optional property of facility colour can also be assigned to each facility. The facility colour is used to distinguish the facilities in the block plan and as a key to the facility names. Each facility colour is specified as a background colour code, a foreground colour code and a pattern index. The values for the background and foreground colour are limited to the capability of the output display device. The pattern index specifies one of the following patterns: no pattern (background colour only), horizontal lines, vertical lines, left and right diagonal lines, cross-hatching and diagonal cross-hatching. If no facility colour is specified LayoutManager will assign a unique colour combination. A display of typical input data for LayoutManager is shown in Fig. 7.

To aid the planners in defining a valid problem in the format required, the built-in editor can be used to create a new problem data set or to edit any of the details of an existing problem.

The editor allows

• facilities to be added and deleted,

\- facility names, areas and colours to be altered,

\- relationship weights (adjacency scores or transportation times) between any two facilities to be changed.

The editor thus allows planners to change interactively various problem parameters. The effect of editing on the outputed layout block plan can be observed by reapplying the relevant criterion. Corrections and experimental changes can be quickly made and their effect noted immediately. Any changes to the input data set can then be saved as a file so that they may be recalled as required. A typical display occurring during the use of the editor is shown in Fig. 8.

<table><tr><td>1</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>1</td><td>-</td><td>I</td><td>O</td><td>A</td><td>A</td><td>A</td><td>E</td><td>A</td><td>A</td><td>O</td><td>A</td><td>I</td></tr><tr><td>2</td><td>I</td><td>-</td><td>E</td><td>I</td><td>I</td><td>I</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>O</td></tr><tr><td>3</td><td>O</td><td>E</td><td>-</td><td>A</td><td>A</td><td>A</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td></tr><tr><td>4</td><td>A</td><td>I</td><td>A</td><td>-</td><td>U</td><td>U</td><td>I</td><td>U</td><td>A</td><td>O</td><td>I</td><td>O</td></tr><tr><td>5</td><td>A</td><td>I</td><td>A</td><td>U</td><td>-</td><td>U</td><td>U</td><td>A</td><td>U</td><td>U</td><td>I</td><td>O</td></tr><tr><td>6</td><td>A</td><td>I</td><td>A</td><td>U</td><td>U</td><td>-</td><td>U</td><td>U</td><td>U</td><td>U</td><td>I</td><td>U</td></tr><tr><td>7</td><td>E</td><td>U</td><td>U</td><td>I</td><td>U</td><td>U</td><td>-</td><td>U</td><td>U</td><td>U</td><td>U</td><td>X</td></tr><tr><td>8</td><td>A</td><td>U</td><td>U</td><td>U</td><td>A</td><td>U</td><td>U</td><td>-</td><td>U</td><td>U</td><td>U</td><td>U</td></tr><tr><td>9</td><td>A</td><td>U</td><td>U</td><td>A</td><td>U</td><td>U</td><td>U</td><td>U</td><td>-</td><td>I</td><td>U</td><td>X</td></tr><tr><td>10</td><td>O</td><td>U</td><td>U</td><td>O</td><td>U</td><td>U</td><td>U</td><td>U</td><td>I</td><td>-</td><td>U</td><td>U</td></tr><tr><td>11</td><td>A</td><td>U</td><td>U</td><td>I</td><td>I</td><td>I</td><td>U</td><td>U</td><td>U</td><td>U</td><td>-</td><td>O</td></tr><tr><td>12</td><td>I</td><td>O</td><td>U</td><td>O</td><td>O</td><td>U</td><td>X</td><td>U</td><td>X</td><td>U</td><td>O</td><td>-</td></tr></table>

Fig. 7. Typical input data.

## 5.2. The model base component

Models are used by LayoutManager to suggest layouts to the planners based on the productivity selected. The deltahedron heuristic of Foulds et al. [36,23] is used to accommodate C1. The n-boundary heuristic of Giffin and Foulds [25] is used to accommodate C2. The super deltahedron heuristic of Foulds and Giffin [24] is used to accommodate C3. The edge replacement and vertex relocation routines of Foulds and Robinson [37] are used to attempt layout improvement. This is discussed further in the description of the IMPROVE module.

Once a problem has been specified, the appropriate criterion can then be applied to the input data to produce a block plan and its score. The score is displayed and, in the case of criterion C1, the score is also displayed as a percentage of a calculated upper bound to provide some indication of how close to an idealized best possible layout the solution is. Relevant displays are shown in Fig. 9.

The facility adjacency structure produced by the DSS is internally represented as a tree structure and is not directly accessible to the user. Instead, Layout-Manager generates and displays a block plan based on it.

The block plan is constructed by inserting facilities in much the same order as was used to construct the adjacency structure. Each facility is inserted adjacent to exactly three already inserted facilities. Let us call these three facilities the parent facilities of the child facility to be inserted.

When inserting a child facility into the chosen parent facility the area encompassed by the parent facility is increased to match the size of both facilities. The area is then divided so that each facility is of the correct size. If facilities are inserted into the parent facility that was the last of the parents to be inserted, the mechanics of the DSS ensures that no unwanted adjacencies are created and that existing adjacencies are retained. Inserting in this manner implies that at each iteration, at most three child facilities may be inserted into any given parent facility. It is important to note here that the underlying deltahedron heuristic of the DSS is deterministic, i.e. its application will always produce a block plan which is the dual of the adjacency graph. (See Foulds [36] for an explanation of these graph theoretic terms.)

![](/api/attachments/95J5Q8VZ/fulltext/images/3fed1042572178ce616dcea64fa43d59dd6bfa14d2684212b54aef0af25d1a1b.jpg)  
Fig. 8. Typical editor display.

![](/api/attachments/95J5Q8VZ/fulltext/images/9d47d4c11e621faf65d187bc954e0598f0d1d9db4d7a4d4cc7e4f41cd6763319.jpg)  
Fig. 9. Key, block plan, and score display.

For the initial four facilities, the exterior facility is assumed to be inserted first. The remaining three initial facilities are then ordered based on their areas, starting with the facility with the smallest area. Assigning insertions in this order implies that no facilities will be inserted into the exterior facility, as both the other two parents of a child facility must have been inserted later than the exterior. Similarly, no facility will be inserted into the smallest initial facility as at least one other parent must have been inserted later. The third initial facility inserted can only have the child facility inserted whose parents are exactly the first, second, and third initial facilities. The other facilities that can be inserted at this stage must be inserted into the fourth initial facility which has been arranged to be the largest. Choosing insertions to be made into the larger facility is important in producing a useful block to avoid facility shapes that have been elongated by large insertions to the extent that their shape has become unusable.

Once the facilities in the initial layout of the first four facilities have been constructed, there are three points in each facility where other facilities can be inserted; these correspond to three corners of the facility. Each of these corners intersect with exactly two other facilities. The remaining corner of the rectangular facility does not intersect with other facilities and is redundant in terms of the insertion process.

The presence of the redundant corner means a facility can be inserted in one of two ways. Facilities can be inserted by boxing—creating a box at the appropriate corner of the enlarged parent facility. Boxing in this fashion does not remove any existing adjacency and ensures that the inserted facility is adjacent to only its three parents. The second insertion method, known as carving, extends an inserted facility from its insertion corner to the redundant corner, carving a complete slice out of the parent facility. The redundant corner can be used in this fashion because it does not represent any specific adjacency in the deltahedron.

The advantage of carving over boxing is seen by the effect of insertion on the parent facility. With boxing, the originally rectangular parent facility assumes an L-shape, and if two child facilities are inserted into the same parent by boxing, the parent has a T-shape. If all three possible insertions into a parent facility are boxed the parent facility's shape becomes even more irregular. An irregularly shaped facility may be unusable for its intended purpose and should be avoided. When carving however, the shape of the parent facility remains rectangular, and for this reason is preferred.

As there is only one redundant corner in each facility, only one child facility can be inserted by carving into each parent facility, and this child facility cannot be carved if its insertion corner is diagonally opposite the redundant corner. If there is a choice between facilities to carve, LayoutManager will choose the larger of the facilities as the one to carve. It is preferable to carve larger facilities, as carved facilities have a dimension in common with their parent which will tend to be larger than the child because of the insertion order used in the heuristic. If carving is used where possible, all facilities in the final plan will either be rectangular, L-shaped or T-shaped.

The final block plan shape is assumed to be rectangular and the ratio of width to height can be specified by the user. The shape can be adjusted dynamically although the total area must always equal the sum of the facility areas. By default, the final block plan shape is assumed to be square.

The shape of an individual facility is controlled by the shape of its parent facility and the insertion method used. For carved facilities, one dimension matches the dimension of the parent and the other is determined by the area of the child facility. For boxed facilities, there is a degree of freedom in their shape. The width and height of a boxed facility may be chosen, provided the dimensions of the facility correspond to the required area, the facility remains completely inside the parent, and an adequate length of boundary is retained by the parent and its adjacent facilities. When more than one box is added to a facility, care is taken that the child facilities do not overlap.

LayoutManager uses the ratio of parent facility dimensions to fix the shape of the box. Using this ratio gives some similarity to the shapes used in the block plan, and the length of the adjacencies between the parent and its parent are maintained as a ratio of their original lengths. The box ratio is moderated so that the box does not become too elongated, as square facilities are assumed to be the most desirable shape. Provided the box remains inside its parent, the ratio of its dimension is adjusted to be in the range between 1:1 and 1:2.

A minimum width of facility and of adjacent boundary is also used to adjust the shape of facilities. LayoutManager initially calculates the minimum width to be $(\sqrt{A/n})/2$ , where A is the total area to be laid out and n is the number of facilities. LayoutManager attempts to shape facilities so that this minimum is maintained. There are, however, situations where this minimum cannot be satisfied using the insertion methods available. For example, if a sufficiently small facility is carved into a large facility, one dimension of the small facility is forced to be large causing the other dimension to be smaller than its minimum width. Similarly, boxing a sufficiently large facility into a small facility will cause the adjacencies of the small facility to be less than any minimum width chosen. If the minimum width criteria cannot be satisfied, LayoutManager reduces the minimum width until a solution can be found and the block plan drawn. If the minimum width was reduced, the user is informed of the required minimum width and of the facility which forced the reduction.

The block plan is drawn to scale within a window using the final block plan shape specified and the appropriate colours and patterns. A key to the colour patterns is also displayed, so the user can relate the shapes back to the names provided. Having produced a block plan, the user can evaluate the results and return to the input data to make any necessary modifications using the built-in editor. The changes can then be reapplied and a new block plan will be drawn.

When the user is satisfied with the results or wishes to save a particular block plan for further study, the block plan can be printed out or saved as a file. Saved block plans, when reloaded, are displayed in separate windows so that several instances of a scenario with minor modifications applied can be viewed at once. One intended use for this option is to observe the changes that are produced when procedures are successively applied to the problem.

## 5.3. The window-based user-interface component

As previously stated, LayoutManager is composed of five modules: FILE, APPLY, IMPROVE, VIEW, and OPTIONS. The pull-down menus give access to the modules. Each module comprises a secondary menu of procedures. All procedures are independent and can be used in any order. All data can easily be stored for further processing. A short description of the modules and their procedures follows.

The FILE module provides file manipulations, exit, and DOS-shell functions. LayoutManager automatically loads the input data files, which are used in the criteria implementation process, and can be edited using the File Open menu command.

The APPLY module actually implements the appropriate procedure to automatically generate a block plan according to the criteria selected.

The IMPROVE module can be used to attempt to improve any block plan that is displayed. For maximum flexibility, these improvement procedures can be applied in several ways. The available procedures are (1) simultaneously making two adjacent facilities no longer adjacent and making two non-adjacent facilities adjacent, and (2) relocating a facility that is adjacent to exactly three other facilities in a new part of the block plan. One instance of either of the procedures can be applied and the block plan will be automatically redrawn to display the change, along with its score. LayoutManager also provides the option of applying a single instance of the improvement procedure which will yield the best improvement in the total score. There is also the option of repeatedly applying the procedure which gives the best improvement in the score until no further improvement is possible.

## 5.4. General discussion

LayoutManager can automatically generate a block plan using information from the planners or a database, and thus provide a block plan with the intervention of the planners. It can then display or print the plan. Because users are often reluctant to use the solution of a model they do not understand, Turban [28] and Sprague and Carlson [38] listed “understandable model-base” as a desirable DSS characteristic. Thus LayoutManager has been designed to provide block plans that can be modified by the user. This option is also a useful planning tool, where the effects of “what if” queries can be analysed.

We should stress that our approach does not generate layouts that satisfy all the various constraints and complicating factors. Rather, the purpose of the DSS is to suggest an initial layout. This layout may then be modified by the planners in the light of those complicating factors. Automatic block-plan generation may also be used as a strategic planning tool in which various options can be tested and the costs of those can be compared.

LayoutManager includes all of the characteristics of an effective DSS from the generic DSS framework of Sprague and Carlson [38] and Turban [28].

\- It supports but does not replace the decision maker. It should therefore neither try to provide the “answers” nor impose a predefined sequence of analysis.

\- It supports a semistructured decision, where parts of the analysis can be systematized for the computer, but where the decision maker's insight and judgment are needed to control the process.

\- It combines modelling techniques with database and presentation techniques.

\- It emphasizes ease of use, user friendliness, user control, and flexibility and adaptability.

\- It supports all phases of decision making.

\- It interacts with other computer-based systems, mainly with the company mainframe system, to download and upload information.

## 5.5. Implementation of the DSS

LayoutManager has been implemented on an MS-DOS personal computer with a high-resolution monitor. It was developed using a prototyping approach. The iterative (prototyping) approach is most common in DSS development since the information requirements are not known precisely (Turban [28]). The core of the DSS was written in a general-purpose programming language—a set of Borland Pascal Version 7.0 subroutines and library functions. Systematic testing assured that each process was error-free before the next layer of complexity was added. Implementation enabled the development team to work on both the model building and the interface between other components of the systems, allowing for periodic testing of their enhancements and progress and checks on performance of the whole system. The need for involvement and participation of the potential users was recognized right from the beginning.

Version 1.0 was first developed and following users' feedback and reaction, the system was refined, expanded, and modified. The changes have largely occurred in the implementation of the graphical interface. Minor changes have also been made to other areas. The layout of the files that make up the LayoutManager system has also been improved. The display with colour aims to simplify the system and emphasize the ease of use, flexibility, and adaptability of the system.

Initially, teething problems were encountered and some bugs were discovered. There were gaps in our perception of the functions of the DSS and the desires of the planners. There were also gaps in communicating the instructions to be followed. The time spent by the planners in preparing the block plans has been cut significantly and the boredom of the task has been reduced, thus freeing the planners for more creative tasks. However, it is too early to gather evidence of actual savings of production costs. Full details of the implementation of the DSS at CAIL is given by Foulds [39].

## 6. Summary and conclusions

We introduced a DSS, called LayoutManager, which is designed to address issues concerning block plan design that commonly occur within a particular computer hardware manufacturing plant. A conceptual model for providing a DSS for facilities layout has been presented. LayoutManager was designed to assist planners in every step of the layout design process. It does not automate the decision-making process, but helps planners by providing powerful tools to create layout plans, choose between plans, generate alternative plans, and to assess alternative plans with respect to productivity criteria of their choice. The system allows the planner to create block plans automatically, minimize the total distance travelled, and to improve existing plans.

In general, DSS benefits are often uncertain and are difficult to assess. In our case, with the prototyping approach, where development is evolutionary, this is especially the case. The ongoing layout changes and changing environments make it even more so. The true value of a DSS is whether it improves a manager's decision-making capability, which is not easily measured. Therefore, the traditional cost-benefit analysis will not be able to capture all of the DSS benefits. Actually in some cases, it may not be well suited to the DSS. However, some of the benefits in our case can be measured, such as production costs. The use of LayoutManager as a DSS may also result in a reduction in labour costs. The system also has tangible and intangible benefits. It can benefit planners in: fine tuning existing layouts, creating entirely new layouts, strategic planning for new production plans, efficient facility utilization, and the flexibility to plan for and cope with unexpected situations. The DSS also allows the planners to carry out ad hoc analysis through “what if” queries. It also provides the planners with a better understanding of the business, where the system can alert users concerning illogical outcomes, brought about by poor production sequences, processes, and procedures. In summary, this paper shows that facilities planning is a complex management process involving subjective and objective information and judgements. LayoutManager is designed to deal with such complex situations. As a result of numerical experimentation and practical implementation of the system, we are confident that it represents a useful addition to the facilities planner's toolkit.

## References

[1] J.A. Tompkins, J.A. White, Facilities Planning, Wiley, New York, 1984.

[2] D.R. Sule, Manufacturing Facilities—Location, Planning and Design, PWS-KENT, Boston, 1988.

[3] S.S. Heragu, Recent models and techniques for solving the layout problem, European Journal of Operational Research 57 (1992) 136–144.

[4] D. Chajed, B. Montreuil, T.J. Lowe, Flow network design for manufacturing systems layout, European Journal of Operational Research 57 (1992) 145–161.

[5] R.G. Askin, M.G. Mitwasi, Integrating facility layout with process selection and capacity planning, European Journal of Operational Research 57 (1992) 162–173.

[6] D.J. van Camp, M.W. Carter, A. Vannelli, A nonlinear optimization approach for solving facility layout problems, European Journal of Operational Research 57 (1992) 174–189.

[7] S.S. Heragu, A.S. Alfa, Experimental analysis of simulated annealing based algorithms for the layout problem, European Journal of Operational Research 57 (1992) 190–202.

[8] P.W.C. Kouvelis, W.-C. Chiang, J. Fitzsimmons, Simulated annealing for machine layout problems in the presence of zoning constraints, European Journal of Operational Research 57 (1992) 203–223.

[9] R. Ram, N. Viswanandham, Performance evaluation of cellular flexible manufacturing systems: A decomposition approach, European Journal of Operational Research 57 (1992) 287–295.

[10] S.C. Sarin, P. Loharjun, C.J. Malmborg, B. Krishnakumar, A multiattribute decision-theoretic approach for the layout design problem, European Journal of Operational Research 57 (1992) 231–242.

[11] J. Leung, A graph-theoretic heuristic for designing loop-layout manufacturing systems, European Journal of Operational Research 57 (1992) 243–252.

[12] M.J. Rosenblatt, B. Golany, A distance assignment approach to the facility layout problem, European Journal of Operational Research 57 (1992) 253–270.

[13] T.L. Urban, Computational performance and efficiency of lower-bound procedures for the dynamic facility layout problem, European Journal of Operational Research 57 (1992) 271–279.

[14] J. Balakrishnan, F.R. Jacobs, M.A. Ventakaramanan, Solutions for the constrained dynamic facility layout problem, European Journal of Operational Research 57 (1992) 280–286.

[15] L.R. Foulds, Techniques for facilities layout: Deciding which pairs of facilities should be adjacent, Management Science 28 (1983) 1414–1426.

[16] C.M. Harmonosky, G.K. Tothero, A multi-factor plant layout methodology, International Journal of Operational Research 30 (1992) 1773–1790.

[17] B. Malakooti, G. D'Souzi, Multiple objective programming for the quadratic assignment problem, International Journal of Production Research 25 (1987) 285–300.

[18] B. Malakooti, A. Tsirisjo, An expert system using priorities for solving multiple criteria facility layout problems, International Journal of Production Research 27 (1989) 793–808.

[19] B. Malakooti, J. Deviprasad, An interactive multiple criteria

approach for parameter selection in metal cutting, Operations Research 37 (1989) 805–818.

[20] B. Malakooti, Assembly line balancing with buffers by multiple criteria optimization, International Journal of Production Research 32 (1994) 2159–2178.

[21] F.R. Jacobs, A layout planning system with multiple criteria and a variable domain representation, Management Science 33 (1987) 1020–1034.

[22] K.M.D. Hassan, G.L. Hogg, A review of graph theory application to the facilities layout problem, Omega 15 (1987) 291–300.

[23] L.R. Foulds, P.B. Gibbons, J.W. Giffin, Graph theoretic heuristics for the facilities layout problem: An experimental comparison, Operations Research 33 (1985) 1091–1106.

[24] L.R. Foulds, J.W. Giffin, A graph theoretic heuristic for minimizing total transportation cost in facilities layout, International Journal of Operational Research 23 (1985) 1247-1257.

[25] J.W. Giffin, L.R. Foulds, Facilities layout generalized model solved by n-boundary shortest path heuristics, European Journal of Operational Research 28 (1987) 382–391.

[26] K. Watson, J.W. Giffin, L.R. Foulds, Orthogonal layouts using the deltahedron heuristic, Journal of the Australasian Combinatorics Society 12 (1995) 127–144.

[27] A.D. Hall, A Methodology for Systems Engineering, Van Nostrand Reinhold, New York, 1962.

[28] E. Turban, Decision Support and Expert Systems: Management Support Systems, 3rd edition, Macmillan, New York, 1993.

[29] L.F. Young, Decision Support and Idea Processing Systems, W.C. Brown, Dubugue, IA, 1989.

[30] B. Arinze, M. Igbaria, L.F. Young, A knowledge based decision support system for computer performance management, Decision Support Systems 8 (6) (1992) 501–515.

[31] J. Couillard, A decision support system for vehicle fleet planning, Decision Support Systems 9 (2) (1993) 149–159.

[32] G. Islei, G. Lockett, B. Cox, S. Gisbourne, M. Stratford, Modeling strategic decision-making and performance measurement at ICI Pharmaceuticals, Interfaces 21 (6) (1991) 4–22.

[33] R.H. Bonczek, C.W. Holsapple, A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York, 1981.

[34] M.C. Er, Decision support systems: A summary, problems, and future trends, Decision Support Systems 4 (3) (1988) 355–363.

[35] P.G.W. Keen, Decision support systems: The next decade, Decision Support Systems B 3 (3) (1988) 253–265.

[36] L.R. Foulds, Graph Theory Applications, Springer-Verlag, New York, 1994.

[37] L.R. Foulds, D.F. Robinson, Graph theoretic heuristics for the plant layout problem, International Journal of Operational Research 16 (1978) 27–37.

[38] R.H. Sprague, E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

[39] L.R. Foulds, LayoutManager: A new DSS—a case study, (1997) Submitted to Interfaces.

![](/api/attachments/95J5Q8VZ/fulltext/images/f60acba110e86e7c7e33604a3924a0e33012ba9e3f8a5a594b5e6d30d5607264.jpg)

Les Foulds was born in New Zealand and received an MSc with honours in mathematics from the University of Auckland in 1972 and a PhD in operations research from Virginia Polytechnic Institute in 1974. Later he became a full processor of industrial and systems engineering at the University of Florida. In 1986 he moved back to New Zealand permanently to become Dean of the School of Management Studies at the University of Waikato. He is now Pro-

fessor of Management Systems there.

He teaches quality management, world class manufacturing, and facilities planning. He has published books and papers on scheduling, facilities planning, combinatorial optimization, and applied graph theory. His research interests are currently in developing decision support systems for vehicle and facilities layout.
