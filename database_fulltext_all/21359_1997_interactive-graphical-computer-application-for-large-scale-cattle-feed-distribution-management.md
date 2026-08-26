---
otero_id: 21359
otero_key: "53HFRC3N"
title: "Interactive graphical computer application for large-scale cattle feed distribution management"
authors: "Marianna Tracey; Moshe Dror"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00046-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Interactive graphical computer application for large-scale cattle feed distribution management

Marianna Tracey $^{a}$ , Moshe Dror $^{b,*}$

$^{a}$ SAP America, Inc., Waltham, MA 02154, USA

$^{b}$ MIS Department, College of Business and Public Administration, University of Arizona, Tucson, AZ 85712, USA

## Abstract

In this paper we describe the development of a visual computer-based interactive management tool for feed distribution at a cattle ranch. In Operations Research terminology, the underlying problem is that of a split-delivery capacitated rural postman problem with time windows on arc. In terms of decision support, the scope of the paper is the description of a computer-based tool used to graphically present the feed distribution solution, and to facilitate the management of cattle feed related input and update operations. This system was site tested in a real cattle feed environment and received very high praise from the cattle professionals.

Keywords: Decision support system; Arc routing; Cattle feed distribution

## 1. Introduction

This paper describes the development of a visual computer-based interactive management tool for feed distribution at a cattle feed ranch. The feed distribution methodology is described in $[1]$ , while this paper focuses on the development of a computer-based tool used to graphically present the solution and manage the cattle feed related input and update operations.

## 1.1. Background

The ranch that motivated this research produces cattle for the general meat market, and holds about 100,000 head of cattle of various ages and sizes at any given time. The cattle are penned throughout a large area in approximately 600 pens connected by a network of paved dirt roads (see Fig. 1). The feed is dispensed along a designated side of each pen (where a trough is located), and must be delivered within a designated time window each day. As the cattle mature, their diet requirements change. Therefore, the feed type, volume, and feeding time for each pen may vary from day to day, and several different types of feed are required each day. The feed is manufactured in one location on the ranch, and a fleet of vehicles deliver the feed to the pens. Since the feed types vary in density, the vehicle capacities also differ by feed type.

## 1.2. Project description

At the time of the study's initiation, the feed distribution management of such large cattle ranches is based primarily on the experience and intuition of the operating crew. No attempt has been made to introduce computer-based management tools for feed distribution. However, during numerous preliminary visits to one ranch, it became apparent that using such tools would raise the operational efficiency by generating shorter, more precise distribution routes to meet the specific feeding time windows of each pen.

![](/api/attachments/53HFRC3N/fulltext/images/347b18285f3c9e6eda92bfb0e54c019d90d10595376fe8434ff1d3eb7b54e8a2.jpg)  
Fig. 1. Cattle ranch pen layout.

Beyond the problem of generating a solution to the feed delivery problem lies the question of managerial display and interaction. In a real life context, the distribution solution needs to be presented as a sequence of vehicle routes which pick up the appropriate feed at the feed producing facility and route the feed through the prespecified cattle pens in the correct order. The solution should be clearly understood and provide all the necessary graphical manipulation required for the best presentation of the solutions.

## 1.3. Objectives

The objective of this paper is to present the development of the display tools for the feed distribution at the cattle ranch. The following steps are required in order to develop such display tools:

\- Determine specific system requirements with requirement analysis.

\- Select a development platform and software application package if appropriate.

• Prepare the graphical outline of the ranch.

\- Design the underlying graphical and data structure.

\- Design the application.

## 2. System requirements

## 2.1. Graphic display

The complete graphics system must be able to display the feed delivery routes, and the pens to which the feed is delivered. In addition, the system must show the pen troughs in order to identify clearly the feed alleys. Other physical features on the ranch, such as the rail line and the mill, must be available for display if desired.

The delivery routes must be shown in different colors or line types, to make them distinguishable from one another. The user must be able to add or remove routes from the display. Because there may be up to 70 different deliveries made per day, many of which have overlapping deadhead paths, it is not possible to clearly display all the delivery route simultaneously.

Thematic shading is used to display different quantitative ranges of data, discrete data values, lot number, ration type, cattle type, or cattle age.

## 2.2. Application development environment

The cattle ranch management team will be the end-users of this type of system. Therefore, it is necessary to develop a user-friendly system, preferably one which is menu-driven and operates in a graphical environment. This requires an application development environment which could consist of either a programming language, macro language, or batch commands which can be used to create applications.

## 2.3. Attribute binding and feature querying

The system should have the data storage capacity to store and manipulate additional attributes. There are many attributes for both the pens and the routes; this data must somehow be bound to the graphical elements by defined relationships. Examples of such attributes include lot number and feed type. Although these are not necessary for the graphical representation of the feed deliveries, this data is important from the information management perspective.

The system must also have querying capabilities, based on graphical (mouse) selection of a feature (either a pen or a route). The query function must allow displaying not only the inherent feature attributes, but also bound attributes.

## 2.4. Insert / update / delete

Many of the additional attributes associated with the cattle change over time, requiring insert, update, and delete capabilities as well. Examples of this type of data manipulation include:

\- adding cattle to an empty pen;

\- removing cattle from a pen;

\- moving cattle from one pen to another;

\- changing the feed delivery time window to a pen;

\- updating the average cattle weight.

## 2.5. Data duration

This system presently considers only current (single feeding) requirements; diachronic information (e.g., historical routing data) cannot be stored. If the end-users needed to track the history of the feed delivery routing, an archiving module could be added to store part of all the routing data in separate time-tempted subdirectories and files. Additional programming would also be required to analyze the collected data.

## 3. Platform and software selection

## 3.1. Selection criteria

In addition to the system requirements outlined in the preceding section, we considered the following factors in selecting a platform and software package:

\- cost;

\- availability of software package;

\- hardware resources required;

• system administration required;

\- software learning curve;

\- availability of expertise;

\- expandability;

\- feature richness;

• market position of software manufactures;

• end-user resources;

\- portability;

\- graphic import compatibility.

The alternatives considered are described below.

## 3.2. Description of alternatives

## 3.2.1. PC Arc / Info

The Arc/Info family of products is considered by many the world leader in geographic information systems technology (GIS). Although it is usually expensive, the University of Arizona has a site license with ESRI, maker of Arc/Info, for campus-wide use of their products, requiring only the price of an additional set of manuals if we chose PC Arc/Info.

PC Arc/Info meets all of the system requirements outlined in Section 2, and has particularly strong database capabilities. This is a feature-rich application with capabilities which far exceed our current requirements. It is a DOS application with Windows extensions added-on. Though a pure Windows application environment would be preferable, our end-users have both DOS and Windows available to them. PC Arc/info accepts DXF format drawings (programable with AutoCAD), and the import facility is clean and flexible.

On the negative side, PC Arc/Info has a steep learning curve relative to other PC desktop mapping applications, the command line interface is not user-friendly, and assistance would be minimal since most of the local users of the site license operate in the UNIX environment, and have minimal experience with PC Arc/Info application.

## 3.2.2. UNIX Arc / Info

There would be several advantages to using the UNIX version of Arc/Info. This is the native environment for Arc/Info, and therefore contains the richest set of features, and a more advanced macro programming language. Also, the UNIX Workstations that we have would make the most impressive visual presentation, and we would have access to local experts at the University.

However, the UNIX version of Arc/Info requires a large investment of time in initial configuration and system administration, in addition to consuming valuable system resources. Another negative aspect of this alternative is that the end-user is more likely to have PC and Windows machines available than UNIX workstations.

## 3.2.3. MapInfo

MapInfo is a Windows map-drawing and map-querying package which is relatively inexpensive and easy to learn. Like PC Arc/Info, MapInfo builds images as a series of layers, analyzes the layers, and provides access to data beneath the layers. MapInfo also has a full programming language (MapBasic) for creating turnkey applications, see $[2]$ .

MapInfo is targeting this software primarily as a query package for sales management. Although maps may be digitized or imported from other formats, its strength is in analyzing data from MapInfo national, state, county, or city maps. This presented a possible problem with our application, specifically with the representation of the delivery routes. Another concern was the limited portability and expandability, and the ability to call external programs.

## 3.2.4. Borland or semantic $C + +$

We considered both Borland and semantic C + +: The positive aspects of programming in C + + are portability (PC to UNIX and vice versa), availability, cost, and access to people with expertise. These C + + compilers, however, do not have built-in graphical mapping features, and though there may be libraries, the project would require extensive programming in order to meet the system requirements outlined in Section 2. In addition, the learning curve for Windows programming in C + + is steeper than that of the mapping software packages' macro languages.

## 3.2.5. Reasons for selecting PC Arc / Info

Ultimately, we selected PC Arc/Info because it best met the criteria outlined in Section 2, without imposing any obvious limitations: It is affordable, flexible, and provides the required functionality, albeit with some lack of user-friendly interface.

## 3.3. Description of PC Arc / Info

We used the following PC Arc/Info modules for our application:

StarterKit and Data Conversion. All of the initial graphic and character-based data conversion and editing was performed using the Starter Kit and Data Conversion commands. Although there is a shell program through which the user can perform many functions, to access the full range of PC Arc/Info capabilities the user must operate in the command-line mode which is not at all intuitive, and in the early stages requires constant referral to the manuals.

PC ArcPlot. The ArcPlot module provides full graphic output capabilities for PC Arc/Info, including screen displays, and can use maps as graphic windows to the database for interactive query and update of attribute information, see $[3]$ . The application which we developed runs in the PC ArcPlot module.

SML (Simple Macro Language). SML is a set of commands which constitute a simple programming language for building macros with some of the features of a high-level language such as expression evaluation, handling of input and output, and directing program flow-of-control, see [4]. SML can also be used to create menus and dialog boxes which prompt for input, and take action based on the response given. We used SML to develop the window-based menu-driven application.

## 4. Graphical representation

## 4.1. Graphics file formats

We created and refined a CAD representation of the cattle ranch layout in parallel with the software selection and procurement process. We used a combination of hand drawn sketches and rough dimensional data provided in the computer listing to create the original CAD drawing, and subsequently refined them.

We elected to use AutoCAD release 12 for the following reasons:

\- availability of the software;

\- expertise;

![](/api/attachments/53HFRC3N/fulltext/images/69b88fdfeb759e704a6c37632e8741f6c46778e8cfc285b109a98ac7fa3b5b29.jpg)  
Fig. 2. Drawing conversion.

\- functionality;

\- DXF export capability. (AutoCAD exports to DXF format, which is a widely recognized transferable format.)

Our contacts at the cattle ranch provided us with an accurate CAD layout, created with TurboCAD for DOS and saved in TCD format. Unfortunately, TCD files cannot be imported to CAD Windows. However, the DXF format TurboCAD DOS application file was read into AutoCAD and modified as necessary.

The required changes were made, the drawing was again exported to a DXF file, and imported into PC Arc/Info. Another benefit of the DXF format is that the layers saved in a DXF file are distinguishable when imported into Arc/Info (i.e., individual DXF layers can be saved to different Arc/Info layers). Fig. 2 shows these file conversion sequences.

All of the operations required for this graphical conversion were performed manually, at the command line level. Because this is considered an infrequent operation, required only when the pen layout is modified, it was not included as part of the application. If modifications are required in the future, the original DXF files can be modified using one of the many CAD software packages which recognize DXF or PC Arc/Info, and the conversion to Arc/Info format can be repeated.

## 4.2. Graphical manipulation required

We made several graphical changes to the original pen layout drawing prior to exporting the file to be used by the Arc/Info application. These changes, which are described below, involved error corrections, feature additions, and modifications to add clarity and meaning to the features.

## 4.2.1. Corrected intersections

Fig. 3 shows a row of pens formed by intersecting arcs. The circled area identifies an “undershoot”, where two arcs intended to form an intersection do not actually meet. This may occur when a drawing is manually digitized from an existing layout, or when the proper snapping techniques are not used during the digital creation. Although these problems can be corrected by specifying a snapping tolerance and running a cleaning program, this process often creates additional errors by extending arcs to form intersections where they do not actually exist, so the cleaning program was used for detection purposes only, and errors were corrected manually. Correction of such errors is critical because the generation of polygons to represent the pens requires a closed perimeter.

## 4.2.2. Added features

The original drawing file included only the layout of the pens. We added the following features:

\- Feed Mill: The location where all deliveries start and finish;

\- Routing Arcs: A directed arc offset 10 feet from each pen to show the truck delivery routes;

\- Feed Trough: A double line near the edge of the pen indicating the trough side;

<table><tr><td>3304</td><td>3302</td><td>3300</td></tr></table>

Fig. 3. Intersection undershoot.

![](/api/attachments/53HFRC3N/fulltext/images/2321cb7ffc5e3d87fa28cc55a4cee9a8e26e7403058db6d4f5156bb83ac53c5c.jpg)  
Fig. 4. Added features.

• Rail: The rail line which crosses the yard;

\- Other Roads: Used for dead-heading.

Fig. 4 shows an example of these additional features.

## 4.2.3. Edit pend edges

The delivery roads are relatively narrow (15 to 20 feet) compared to the width of the pens (50 to 100 feet), and when the layout is drawn to scale the arcs, the indicated delivery routes are difficult to distinguish from the pen edges. In order to enhance visibility of the route arcs, we moved the edges of the pens back 10 feet from the road (making the roads appear 20 feet wider).

## 4.2.4. Change curved routing arcs

All curved routing arcs were changed to piecewise linear arcs, to facilitate storing and drawing the arcs using $(x_{1},y_{1})$ , $(x_{2},y_{2})$ coordinates. This results in two or more arcs being associated with one pen. The first arc maintains the original arc identification (e.g., 417); the additional segments have letters appended (e.g., 417A,417B, etc.). Section 5.2 explains the implications of this strategy.

## 5. Specific design considerations and solutions

## 5.1. Data conversion

In order to display the delivery routes, the results of the route generation analysis must be converted to a format which PC Arc/Info can interpret. The results of the analysis are stored in a file that includes the route number, pen number, split flag, and a start and finish location for the split delivery (between 0 and 1) if required (see Table 1).

This data must be converted to $(x,y)$ coordinates in a file formatted in accordance with PC Arc/Info requirements. This conversion is performed by a C program. The program uses a cross reference table that stores the $(x,y)$ coordinates for all arcs (see Table 2). The “Next Arc” columns apply to those pens which have multiple arc segments, and the entry in this column is the arc number of the next segment. The entry NULL indicates that no additional segments exist.

Table 1  
Results of route generation analysis

<table><tr><td>Route number</td><td>Arc number</td><td>Split (0/1)</td><td>Start</td><td>Finish</td></tr><tr><td>1</td><td>301</td><td>0</td><td></td><td></td></tr><tr><td>1</td><td>302</td><td>0</td><td></td><td></td></tr><tr><td>1</td><td>303</td><td>0</td><td></td><td></td></tr><tr><td>1</td><td>304</td><td>1</td><td>0</td><td>0.3</td></tr><tr><td>2</td><td>304</td><td>1</td><td>0.3</td><td>1</td></tr><tr><td>2</td><td>305</td><td>0</td><td></td><td></td></tr><tr><td>2</td><td>306</td><td>0</td><td></td><td></td></tr><tr><td>.</td><td>.</td><td>.</td><td></td><td></td></tr></table>

The cross-reference in Table 2 was created by importing the layer of the DXF graphic file which contains all arcs, and creating a Arc/Info coverage. Next, the “ungen” command was used to create a file listing of “from” ( $x_{1}, y_{1}$ ) and “to” ( $x_{2}, y_{2}$ ) coordinates for each arc. We then imported this text file into an Excel spreadsheet, and used a macro to rearrange the data format shown in Table 2. We then inserted the “Next Arc” column and manually added the required data. (Section 4.2.4 describes the numbering convention used for pens with multiple arc segments.)

The conversion program writes the $(x,y)$ coordinates of the arcs contained in each route to a file in the required Arc/Info format (see Fig. 5), which does not include any reference to the arc number. Each delivery route is stored as a separate layer, or "coverage" in Arc/Info terminology. Therefore, the conversion program creates a separate file for each route, with file name route n.out, where n is the route number. In addition, the program creates a separate deadh n.out file for the deadheading segments of the route. This requires an input file of the same format that is shown in Table 1, which lists only the numbers of the arcs required for deadheading.

Table 2  
Arc number/coordinate cross-reference

<table><tr><td>Arc number</td><td>Next Arc</td><td>X1</td><td>Y1</td><td>X2</td><td>Y2</td></tr><tr><td>301</td><td>NULL</td><td>5334.377</td><td>6016.451</td><td>5397.100</td><td>6039.280</td></tr><tr><td>302</td><td>NULL</td><td>5361.704</td><td>6058.322</td><td>5220.750</td><td>6007.020</td></tr><tr><td>303</td><td>NULL</td><td>5231.011</td><td>5978.829</td><td>5334.377</td><td>6016.451</td></tr><tr><td>304</td><td>NULL</td><td>5220.750</td><td>6007.020</td><td>5079.796</td><td>5955.716</td></tr><tr><td>305</td><td>NULL</td><td>5090.057</td><td>5927.525</td><td>5231.011</td><td>5978.829</td></tr><tr><td>306</td><td>NULL</td><td>5079.796</td><td>5955.716</td><td>4938.842</td><td>5904.414</td></tr><tr><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td></tr></table>

![](/api/attachments/53HFRC3N/fulltext/images/c968271c53f1a4e3bf8fe802acdbc120b9dddc11cdebf640f7170cb566087cbb.jpg)  
Fig. 5. Arc/Info input format.

Within the Arc/Info application, we created a routine which will read each route n.out and deadh n.out file individually and generate a coverage for each. The route coverages created by this routine are stored in subdirectory and the deadheading coverages are stored in its subdirectory. This program searches for route n.out files, creates the coverages, increments the n value, and repeats this process until route n.out is not found. Therefore, it is important that the routes are numbered sequentially. If they are not, route numbers after any gap will not be found and converted.

## 5.2. Converting multiple segment arcs and split deliveries

For those pens which have only one arc segment and which do not require a split delivery, the $(x_{1},y_{1})$ , $(x_{2},y_{2})$ coordinates can simply be read from the cross-reference table and written to the Arc/Info input file in the format shown in Fig. 5. The following sections describe the calculations required for those pens which contain either split deliveries, multiple arc segments, or both.

## 5.2.1. Split deliveries

For split deliveries to pens which are represented by only one arc segment, the $(x_{1s}, y_{1s})$ , $(x_{2s}, y_{2s})$ coordinates are calculated as follows:

$$
\begin{array}{l} x _ {1 s} = x _ {1} + (x _ {2} - x _ {1}) \times s, \\ y _ {1 s} = y _ {1} + (y _ {2} - y _ {1}) \times s, \\ x _ {2 s} = x _ {1} + (x _ {2} - x _ {1}) \times f, \\ y _ {2 s} = y _ {1} + (y _ {2} - y _ {1}) \times f, \end{array}
$$

where $(x_{1},y_{1})$ and $(x_{2},y_{2})$ are the coordinates from the conversion table, s is the start location for the delivery $(0\leq s<1)$ , and f is the finish location for the delivery $(s<f\leq1)$ .

The program then writes these calculated $(x_{1s}, y_{1s})$ , $(x_{2s}, y_{2s})$ coordinates to the Arc/Info input file in the format shown in Fig. 5.

## 5.2.2. Multiple segment arcs

For pens which have multiple arc segments, but do not involve a split delivery, the conversion program writes multiple $(x_{1},y_{1}),(x_{2},y_{2})$ entries to the Arc/Info input file. First, the coordinates for the initial segment are written to the file, and if the “Next Arc” is not equal to NULL, a look-up is performed to retrieve the coordinates of the next arc segment. These coordinates are then written as a separate entry to the file, and the process is continued until the “Next Arc” segment is equal to NULL.

## 5.2.3. Split delivery for multiple arc segment pen

The most complex situation occurs when a split delivery is required to a pen which consists of multiple arc segments. In this case, the computations shown in Fig. 6 are required to determine the coordinates for the entry (or entries) to the input file. The basic strategy is as follows:

\- Find all segments and compute total trough length for pen.

\- Determine in which segment the split delivery should start and the starting position within that segment ( $s^{*}$ – relative to the beginning).

\- Determine the same (segment and position $-f^{*}$ ) for the finishing point.

\- If the delivery starts and finishes in the same segment, treat the delivery as an ordinary split delivery with revised $s$ and $f$ values (see Section 5.2.1).

```c
i arc number (segment for one pen)
d length of segment i
D = Σd, sum of length of all segments for the pen

s start location (0 <= s <= f)
f finish location (0 < f <= 1)

m segment where delivery starts
n segment where delivery finishes

s* start location for segment m
f* finish location for segment n

t_sum0 = 0
t_sum1 = t_sum_{i-1} + d_i / D

find min m such that st < t_sum_m
s* = 1 - (((t_sum_m - st) * D) / d_m)
find n such that fin >= t_sum_n
f* = 1 - (((t_sum_n - fin) * D) / d_n);
if m = n
    print (m, s*, f*)
else
    print (m, s*, 1)
    print (i, 0, 1) for all i between m and n
    print (n, 0, f*)
```  
Fig. 6. Split delivery to multiple arc segment pens.

If the delivery starts and finishes in different segments, write one entry to the file for the start segment with start value = s\* and finish value = 1. Write one entry to the file for the finish segment with the start value = 0 and finish value = f\*. Write one non-split entry to the file for each segment which lies between the start segment and the finish segment.

## 5.3. Pen display

The pen display was created with a CAD file and modified as described in Section 4.2. Section 5.3.1, 5.3.2, 5.3.3, 5.3.4, 5.3.5 describe the method used to adopt this CAD file into an Arc/Info coverage. Note that the steps included in this section establish the foundation on which the application will be built. They are required only for the initial development stages and are not part of the final working application.

## 5.3.1. Import the DXF file

The dxfarc command imports DXF files to create Arc/Info coverages. The user must specify the DXF file to be imported, and name the coverage to be created. The coverage name for the pen layout is pens. The user must also identify which layers (arcs, points, text, etc.) should be included. The DXF file usually consists of many different layers, and normally these should be organized onto separate Arc/Info coverages. To see a list and description of the DXF file layers, the user may enter the dxfinfo command. In this case, the pens layer from the mc-mod.dxf file was imported with arc features only.

Given that in addition to the features relevant to the application, all coverages must have a minimum of four points called tics, which are used to align the different layers as they are added to a display output. To accomplish this, we added four points to the DXF graphic file on a layer named tics, and imported it into every coverage created.

## 5.3.2. Use ADS to check for layout errors

ADS (Arc Digitizing System) is an Arc/Info command used to create or edit graphical data. We used a feature of ADS to identify any dangling nodes (arc endpoints which are not shared with any other arc - see Section 4.2.1). After identifying these problem intersections, we corrected them in the original graphics format - the AutoCAD file. The file could have been changed from within Arc/Info (using the ArcEdit module) but for this prototype we wanted to keep the original graphics files consistent with the Arc/Info coverages. After correcting the errors, we repeated the import process, and re-checked the nodes until all of the problems were corrected, see [5].

ADS can also be used to add labels to polygons, however the naming formats are limited to integer values. We did not use this feature since the pen numbers consist of alphanumeric characters, and there is not a meaningful integer identifier which corresponds to the pen identifier.

## 5.3.3. Build the polygon coverage

Once the pen coverage was created, we built the polygon attribute table (PAT) using the build command. The PAT is a database file in DBF format, and contains the fields shown below:

<table><tr><td>AREA</td><td>Area of each polygon.</td></tr><tr><td>PERIMETER</td><td>Length of each polygon boundary.</td></tr><tr><td>Pens-</td><td>Internal polygon number(assigned by Arc/Info).</td></tr><tr><td>Pens-ID</td><td>User-ID for the polygon(if assigned by the user).</td></tr></table>

## 5.3.4. Cross-reference pen numbers and add attribute fields

Since we did not apply polygon labels using the ADS command, the Pens-ID was not meaningful. We therefore had to cross reference the system-generated Pens-field to the actual pen numbers manually. This involved creating a separate Microsoft Excel spreadsheet which listed the system-generated Pens-number and the corresponding alphanumeric pen identification used by the ranch managers.

We also included the additional attribute fields in the spreadsheet. Table 3 shows a portion of this cross-reference table and describes the additional attributes. Although not all of the attributes included are essential to the route generation process, they all contribute to the ability of this tool to support management decisions.

## 5.3.5. Join PAT file to additional attribute file

Once this cross-reference table was created, we saved the file in DBF format and permanently joined it to the PAT file using the joinitem command. The join was based on the shared item Pens. It is possible to temporarily connect two tables using the relate command, but in this case a permanent join was more appropriate since the shared item is a static value and there would be no benefit to dynamically joining the tables. The data values in the attribute fields will change, but the relationship between the Pens and Pen-num fields is fixed, therefore a permanent join was used.

After this join was performed, the underlying structure for the pen display was complete and all the required application functions could be performed from the ArcPlot module.

## 5.4. Route layer display

After the pen display was completed, a similar series of operations was required to create the foundation for the routing display which contains every delivery arc, and it will be used to query for delivery route information. The route layer differs from the pen display in: (i) the relationship between a pen number and the route number which will deliver to the pen (which is not a fixed assignment), and (ii) the CAD file did not display arcs to identify pen deliveries. (Section 4.2.2 described the process for adding the delivery route arcs to the CAD file, and following sections will describe how the coverage was generated from the modified file.)

Table 3  
Pen number cross-reference and additional attributes

<table><tr><td>Pens</td><td>pen_num</td><td>group</td><td>cattle_type</td><td>cattle_qty</td><td>lot</td><td>rtn_typ</td><td>rtn_qty</td><td>s_req</td><td>f_req</td><td>s_act</td><td>f_act</td></tr><tr><td>1</td><td>2700</td><td>Calf</td><td>c-type</td><td>100</td><td>122</td><td>100</td><td>10.01</td><td>0.29</td><td>0.31</td><td>0.30</td><td>0.31</td></tr><tr><td>2</td><td>2702</td><td>Calf</td><td>c-type</td><td>100</td><td>122</td><td>100</td><td>10.02</td><td>0.30</td><td>0.32</td><td>0.31</td><td>0.31</td></tr><tr><td>3</td><td>2704</td><td>Calf</td><td>c-type</td><td>100</td><td>122</td><td>100</td><td>10.03</td><td>0.30</td><td>0.32</td><td>0.31</td><td>0.31</td></tr><tr><td>4</td><td>2706</td><td>Calf</td><td>c-type</td><td>100</td><td>123</td><td>400</td><td>10.04</td><td>0.30</td><td>0.32</td><td>0.31</td><td>0.32</td></tr><tr><td>5</td><td>2708</td><td>Calf</td><td>c-type</td><td>100</td><td>123</td><td>400</td><td>10.05</td><td>0.31</td><td>0.33</td><td>0.32</td><td>0.32</td></tr><tr><td>6</td><td>2710</td><td>Calf</td><td>c-type</td><td>100</td><td>123</td><td>400</td><td>10.06</td><td>0.31</td><td>0.33</td><td>0.32</td><td>0.32</td></tr><tr><td>7</td><td>2712</td><td>Calf</td><td>c-type</td><td>100</td><td>112</td><td>800</td><td>10.07</td><td>0.31</td><td>0.33</td><td>0.32</td><td>0.33</td></tr><tr><td>8</td><td>2714</td><td>Calf</td><td>c-type</td><td>100</td><td>112</td><td>800</td><td>10.08</td><td>0.32</td><td>0.34</td><td>0.33</td><td>0.33</td></tr><tr><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td></tr></table>

<table><tr><td>Pens_</td><td>System-generated pen identifier.</td></tr><tr><td>pen_num</td><td>Pen number used by ranch management.</td></tr><tr><td>group</td><td>Name of pen group where pen is located (eight total groups).</td></tr><tr><td>cattle_type</td><td>Type of cattle in pen.</td></tr><tr><td>cattle_qty</td><td>Quantity of cattle currently in pen.</td></tr><tr><td>lot</td><td>Lot number of cattle.</td></tr><tr><td>rtn_typ</td><td>Ration type fed to the cattle.</td></tr><tr><td>rtn_qty</td><td>Ration quantity required for the pen.</td></tr><tr><td>s_req</td><td>Required start time for feed delivery.</td></tr><tr><td>f_req</td><td>Required finish time for feed delivery.</td></tr><tr><td>s_act</td><td>Actual scheduled start time for feed delivery.</td></tr><tr><td>f_act</td><td>Actual scheduled finish time for feed delivery.</td></tr></table>

The dxfarc command was used again to import the graphics to create coverage. In this case, the R4 and tics layers were imported to create a coverage named all-rt.

## 5.4.1. Build the arc coverage

For the pens coverage, we created a polygon attribute table (PAT) to store the required data for the pens. The all-rt coverage consisted of arcs (not polygons), so this time we built the arc attribute table (AAT) using the built command. The AAT, like PAT, is a database file in DBF format, and is initialized with a similar set of system attributes.

## 5.4.2. Cross-reference pen numbers

Similar to the pen layout display, the pen numbers had to be manually cross-referenced to the system-generated arc identification numbers. Since the AAT will be used only to look up a pen number or route number (which changes), the routes did not have any additional attributes (other than the pen number) permanently joined to the AAT. The pen number was joined to the AAT file using the joinitem command.

## 6. Application development

The previous section focused on the conversion processes that take place outside of Arc/Info and on the operations required to prepare the underlying graphical and data structure of the system. This section will outline the functions which are included in the application.

## 6.1. Development environment

The operations described in all of the previous sections are performed in the Arc/Info module. In order to take advantage of the PC Arc/Info's full range of presentation functionality, we developed the application for the ArcPlot module. As stated previously, this program is native to DOS but has Windows extensions which we used to create the graphical user interface.

SML (Simple Macro Language) is a powerful development tool which we used to program the application. The following section will highlight the interesting components of the system.

## 6.2. Initial display

After starting the application, the user selects the “Draw Pens”. This menu choice launches the routines which display the pens and all route coverages. The route coverage is necessary for selection operations which will be explained in Section 6.7, but is plotted in the same color as the background to be invisible to the user. The user may also select “Draw Trough” which identifies the feed alleys by drawing a double line on the trough side of each pen.

In addition to these operations which are specific to our application, the menu choices provide standard graphics presentation options such as zooming, panning, and inverting the background. Other utilities provided on the menus include printing the current display, or saving it to a bitmap file.

## 6.3. Display routes

To display the routes, the user selects “Show Routes” from the “Display” pull-down menu which brings up the dialog box shown in Fig. 7. The user must then individually identify each route which is to be displayed. The user must select from 100 different colors to identify and to plot the route; selecting “Line Color” will display a color palette to be shown, and the user can select from the palette using the mouse.

![](/api/attachments/53HFRC3N/fulltext/images/5913ac632fc588cc2ccf3651e87d57b6177dfe17c8e04431ff1a9f72d1a06da1.jpg)  
Fig. 7. Route display dialog box.

## 6.4. Display coverages

The “Show Coverages” menu choice is very similar to “Show Routes”, except the coverages listed are not routes but other physical features which the user may wish to display. These features include the feed mill, the rail which crosses the yard, and other items which were included in the original ranch file.

## 6.5. Pen shading

Once the pen coverage is created and additional attributes are joined to the graphical representation of the pen, the analysis and display features of Arc/Info can be used to represent the data. Thematic shading, or in this case, pen shading, is a simple but powerful tool which displays different attribute values by varying colors. Pen shading does not require any initial definition in Arc/Info, but a look-up table in DBF format is required to assign color numbers to different discrete data values. Table 4 shows a sample look-up table for a feed ration type. The heading of the first column must exactly match the attribute file name (in this case rtn-type). The second column specifies the color, or shade symbol, with which all of the pens for a specific ration type will be shaded. Polygonshades is the ArcPlot command used to create this effect. Legends are created using the ArcPlot keyshade command with size and location parameters set by the keybox, keyposition commands. In this prototype system, legend creation is integrated in the shading operations.

Table 4  
Look-up table for ration type

<table><tr><td>rtn_typ</td><td>Symbol</td></tr><tr><td>0</td><td>0</td></tr><tr><td>100</td><td>93</td></tr><tr><td>400</td><td>73</td></tr><tr><td>500</td><td>89</td></tr><tr><td>700</td><td>70</td></tr><tr><td>800</td><td>67</td></tr></table>

![](/api/attachments/53HFRC3N/fulltext/images/31911d351eb158746698fdd21e53ffb5eed4b8f8cab469394af181c4c8e5c050.jpg)  
Fig. 8. Pen query dialog box.

## 6.6. Pen identification from mouse

A user may use the mouse to select any pen, and the dialog in Fig. 8 will display the attributes of that pen. Once this information is displayed, the user may select another pen, update the data in the current pen, or move the cattle group displayed to another pen.

## 6.7. Route identification from mouse

Similarly, a user may select the route arc adjacent to any pen which will display the route information shown in Fig. 9. The identify command recognizes the mouse input and performs to look-up on the PAT or AAT for the specific coverage. The coverage must be displayed to the current plot when the identity command is called, which is why we created a coverage which contains all arcs. Although the all-rt coverage is not visible (it is plotted in the same color as the background), it is required for this look-up.

![](/api/attachments/53HFRC3N/fulltext/images/3114b087ef940ad2067e064257fb48eb594df15dfb8d45684f650b61227e6431.jpg)  
Fig. 9. Route query dialog box.

## 7. Conclusion

In this paper we describe the development of a visual computer-based graphic interactive management tool for feed distribution at a cattle ranch, the first computer-based management tool for feed distribution ever implemented. In Operations Research terminology, the underlying problem is that of a split-delivery capacitated rural postman problem with time windows on arc. In terms of decision support, the scope of the paper is the description of the computer-based tool chosen to graphically present the feed distribution solution and to facilitate the management of cattle feed related input and update operations. We chose to implement the decision support system for cattle feed using the PC Arc/Info. This software best met our criteria without imposing any obvious limitations. PC Arc/Info meets all the system requirements; it is affordable, flexible, and provides the functionality required for our application. The system has been tested in a real cattle feed environment for a large ranch (of 100,000 head of cattle) and received very high praise from cattle professionals.

## References

[1] M. Dror, J. Leung and P.A. Mullaseril, Routing and Scheduling for Livestock Feed Distribution, Working Paper, MIS Department, University of Arizona (1985).

[2] B. Smith and H. Eglowstein, Putting Your Data on the Map, BYTE (1993) 188–200.

[3] Environmental Systems Research Institute, Inc., PC ARC-PLOT User's Guide (1994).

[4] Environmental Systems Research Institute, Inc., SML User's Guide (1994).

[5] Environmental Systems Research Institute, Inc., Understanding GIS The ARC/INFO Method (1990).

Marianne Tracey is an Applications Consultant at SAP America, Inc. in Waltham, Massachusetts. She received a B.S.M.E. degree in Mechanical Engineering from Tufts University and an M.Sc. degree in Management Information Systems from the University of Arizona. This paper has been written as a part of a Masters Thesis project under the supervision of Professor Dror.

![](/api/attachments/53HFRC3N/fulltext/images/80bcb1fc99d6820c8cae1232714aa2cf5f2ec375907613f12355a5ec79764cbb.jpg)

Moshe Dror is a Professor in the MIS Department at the College of Business and Public Administration, University of Arizona. He received his Ph.D. in Management Science from the University of Maryland at College Park with minors in Transportation and Computer Science, and I.E. (Industrial Engineering) and M.Sc. (Mathematical Methods in Engineering) degrees from Columbia University. He serves on editorial boards of IIE Transactions, Computers and

Operations Research, Foundations of Computing and Decision Sciences. His current research ranges from combinatorial problems such as routing and machine scheduling to problems of cost allocation in logistics, interactive multiobjective Linear Programming systems, and decision support systems. He is actively working on arc routing and inventory distribution related research in industry.
