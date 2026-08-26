---
otero_id: 11834
otero_key: "FTHCEB6H"
title: "A spatio-temporal geometry-based model for digital documentation of historical living systems"
authors: "Athanasios D. Styliadis; Michael Gr. Vassilakopoulos"
year: "2005"
journal: "Information & Management"
doi: "10.1016/j.im.2004.01.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A spatio-temporal geometry-based model for digital documentation of historical living systems

Athanasios D. Styliadis<sup>\*</sup>, Michael Gr. Vassilakopoulos<sup>1</sup>

<sup>a</sup>Department of Information Technology, The ATEI of Thessaloniki, P.O. Box 14561, Thessaloniki 541 01, Greece

Received 10 November 2002; accepted 6 January 2004 Available online 1 April 2004

## Abstract

Representations used in digital documentation applications today usually assume a world that only exists in the present. Information contained within a database may be added-to or modified over time, but change through time is seldom maintained. This limitation of current IT has recently received attention, given the increasingly urgent need to understand geographical processes and cause-and-effect inter-relationships between human activities and the environment. Models proposed for the representation of spatio-temporal data are extensions of traditional raster and vector representations that can be seen as locationor feature-based, respectively, and are therefore best organized for performing, either location- or feature-based queries. In this paper, a new spatio-temporal data model suitable for digital documentation of historical living systems (artefacts, monuments and sites) is defined: it is based on 3D geometry and intended to facilitate analysis of temporal relationships and patterns of 3D modeling changes through time. This is particularly useful to both IT and IS managers, researchers and practitioners. It is shown that time-based queries related to 3D models of objects can be processed in an efficient and straightforward manner using the model. Finally, analytical time efficiency estimations are given, showing that the model is also an efficient and compact representation of spatio-temporal information. <sup>#</sup> 2004 Elsevier B.V. All rights reserved

Keywords: Visualization and management of historical living systems; Spatial and temporal analysis; Digital documentation; Morphogenesis temporal modeling; 3D geometry

## 1. Introduction

The need to understand the effects of man’s creations on the natural environment (historical living systems [15] involving artefacts, monuments, archaeological sites, etc.) or on a number of management and business applications [16] (such as tracking the accuracy of predictions, evolution of markets, etc.) at geographic scales as far as details are concerned, has received increasing attention in both the IT and IS communities. For instance, in cultural resource management within the developed world, the emphasis has shifted from inventory and manual documentation to implementation and maintenance of a DSS with spatial and modeling capabilities (i.e. digital documentation). This has required integrated and broad-scale process analysis in order to understand historical, natural and human processes and how they are interrelated in historical living systems.

The availability of remotely sensed satellite and high altitude photogrammetry data of archaeological sites, in addition to other spatio-temporal observational data like close-range photogrammetry images of historical artefacts or monuments, has made the empirical study of large-scale, complex spatio-temporal processes possible and further increased the demand for integrated computer-based tools for this task [31]. As a result, enhancement of the spatio-temporal capabilities of GIS towards a DSS with spatio-temporal functionality (4D GIS/DSS) is now an issue [17]. A key element in this work is how to represent detailed and accurate 3D structured morphogenesis-based deformable models (i.e. groups of basic shape elements [9]) of monuments and sites in time, as well as space, so that spatio-temporal data can be effectively stored and analyzed. Therefore, for rapid GIS applications development [14] a DSS for digital documentation and management of monuments and archaeological sites can be designed and implemented, if all the data types are spatially compatible, in that they all can be recorded under the same attribute (e.g. a line-segment type) describing and formulating the 3D geometry of the monument or geographic region (archaeological site).

In engineering (e.g. architecture) and historical living systems management (e.g. archaeology), a time-based representation is needed to allow empirical analysis of space and time dynamics, and ultimately to allow temporal 3D modeling, simulation and management of geographical processes as an integrated GIS capability [21]. Several approaches to spatio-temporal modeling have appeared in the database literature, however, none of them is based on CAD systems and 3D geometry but on specialized (traditional) database approaches. For example, in [28] a quantum-based spatial data model has been formalized: it supports directly point, line and surface types as used daily.

Traditional raster and vector model representations are organized for performing location- and featurebased queries respectively. Neither form is well-suited for analyzing overall temporal historical relationships of objects, events and quality management issues throughout a geographical area as is a timebased representation [3]. Even more, classical morphogenesis-based modeling has a lack of spatial (GIS) functionality and, therefore, new agent-based morphogenesis models using 3D geometry of pattern formation are needed [2].

In our paper, a new type of spatio-temporal data model is defined, based on 3D modeling and time as its organizational basis; it is intended to facilitate spatial analysis of temporal historical relationships. The model is called GST-DigiDoc (geometry-based spatio-temporal digital documentation). This represents an extension of the NAOS object-oriented modeling scheme for Byzantine churches [24]. Time-based queries related to 3D models of objects, having a regular can be represented in an efficient and conceptually straightforward manner using the model by describing algorithms for three fundamental procedures used in architecture and archaeology [1].

## 2. Existing representations

Any representational scheme is inextricably linked to a set of specific uses. This was demonstrated within the spatial realm during the lengthy raster versus vector debate that began in the 1970s [18]. Functional trade-offs that have been recognized between these two approaches and other approaches, relational DBMS (RDBMS) in particular, have resulted in modern GISs being implemented increasingly using a multi-representational database design. If digital documentation of historical living systems is to provide sophisticated temporal analysis capabilities, as well as being able to answer specific types of time-based queries [25], it is necessary to utilize a type of representation that is suited to that application.

The only data model available within existing CAD/GIS/Modeling software (a spatio-temporal data model in a digital documentation system) is a series of layer-based 2D models. This representation, known as the snapshot model, simply employs the grid data model using a sequence (i.e. a geometric database) of spatially registered 2D models [5]. Instead of a single grid-based file representing a complete thematic map layer, each grid-based 2D model $S _ { i } ,$ represents a monument historical state relative to a given thematic domain, storing an accurate and complete layer-based 2D model, at a known point in time, $t _ { i } .$ Actually, each cell within a separate snapshot contains a pointer to the corresponding 2D model.

This approach is conceptually straightforward, and the historical state for any given object within the recorded time interval can be retrieved either directly or by interpolation. Nevertheless, the actual changes that occurred at the component elements between given times are not stored and can only be derived by comparing, either the pixel value differences in pictorial representation or the element information between successive layers of graphical information.

Another approach with management and strategic functionality [30] is based on the so-called grid model, proposed within a GIS/SIS context in [23]. The basic idea is to represent each pixel in a grid-based array of discretized objects as a list. With this representation, any change of a given component element of the monument is added to the beginning of its list. The result is a set of variable-length lists referenced to grid cells. The present (i.e. most recently recorded) state for the entire monument is easily retrieved as the first value stored in all of the location related lists. This has the advantage of storing only the changes related to specific monuments and has the related additional advantage of avoiding storing redundant information, in contrast to a layer-based representation.

Several spatio-temporal models [6,22] and spatiotemporal access methods [26,27] have been described to record spatial changes in time as they relate to specific entities. These approaches are not suitable for real-world 3D complex objects in historical living systems. At a broad conceptual level, all of these models represent extensions of the classical vector representation. They rely on amendments, where any change after some initial time in the configuration of polygonal or liner entities are incrementally recorded as additions to the original entities. The first of these models was proposed in [12] and relied on amendment vectors. The time of any change was recorded as an attribute. This organization allowed the integrity of individual features (e.g. 3D models), components of those features (e.g. arches), elements (e.g. bricks), and their spatial interrelationships to be explicitly retained over time. This basic idea was utilized in [7] within a 4D space–time Cartesian space, where an extended hierarchy consisted of nodes, lines, polygons, polyhedra, polytopes and polytope families. This research was based on a 2D design session, with the addition of an extra dimension: to 2D polygons to become polyhedra (3D enclosed areas), or for 3D polyhedra to become polytopes (4D enclosed areas), etc.

All of these extended vector and grid models incorporated the temporal dimension in some indirect way while retaining their fundamental organizational basis. They also retained their relative functional advantages and disadvantages. All vector models were feature-based, in the sense that all locational and temporal information, as well as other types of attribute information (metric or qualitative), was stored relative to specific geographic/spatial features, and/or the topologically defined lines and nodes that make up those features in a 3D modeling scheme. In other words, geographic/spatial entities and 3D models serve as the basic conceptual element and organizational basis of the vector. Conversely, the grid model, or any tessellation model, can be characterized as location-based, since all other information is stored relative to specific locations.

Because of these two fundamentally different ways of storing information, a vector model, based on the 3D representation of its components, can be used more effectively to store information and perform tasks relative to spatial features, including the discovery of topological relationships between them. This model is suitable for a 3D model-based spatial documentation. On the other hand, the vector model is not really so good for storing information and performing tasks related to a specific location or set of locations. Conversely, a grid model can perform tasks relative to locations and overlays. Neither model can be used directly for temporal support.

The spatial data types and operations in [4] were similar to these, except that an infinite spatial representation was considered. A point data type was also supported. A classification of the set of operations for the management of natural resources was proposed in [13], but formalism for data types and operations was missing. Finally, the model defined in [29] considered only one spatial data type whose elements were collections of points, non-overlapping straight-line segments and non-overlapping triangles. In this paper, the set operations union, difference and intersection were well documented and can be applied to spatial objects, but the basic GIS operation boundary was presented informally.

In the vector and grid models, associating additional temporal information with individual features can be provided only using software extensions in the environment. In using a spatio-temporal GIS to analyze processes, it is also essential to be able to examine changes in the data due to time, retrieving locations, objects and features for a specified monument and to examine overall patterns of time-based relationships. Change can be converging or diverging. Individual objects (e.g. monuments) and events (e.g. fire) can be characterized as clustered, forming time episodes that can be further grouped into time cycles. Cyclical variations is an important steady-state behavior over longer time periods: e.g. a series of church constructions between 1300 and 1400 can be grouped as an episode. This may, in turn, be part of a global Byzantine cycle.

Specific examples of queries which relate spatial and non-spatial changes that occur in specific spatiotemporal relationships include:

\- When did the last monument renovation occur in a particular city?

\- Which monuments are known to have suffered from a specific fire?

\- Which monuments are known to have suffered from major fire events in the 1960s?

\- Which monuments changed in appearance in the 10 years after a particular event?

In addition to extending traditional raster-based and vector-based approaches to incorporate changes with time, they also need to be explicitly modeled. This was described in [11] but no example was given.

## 3. The time-based approach

In this approach, time becomes the primary organizational basis for recording change. The sequence of events, representing a spatio-temporal process, is noted via a time-line (see Fig. 1). This represents an ordered progression of known changes from some starting date to another subsequent point in time. Each time along the line $( t _ { 0 } , t _ { 1 } , . . . . , t _ { n } )$ can have a particular set of 3D models of monuments and component elements that have changed at that time and the value to which they changed.

![](/api/attachments/FTHCEB6H/fulltext/images/c19e2027be497592a79fb1eedd2143402865ce0a33a384ea8a82400ee9baf38a.jpg)  
Fig. 1. Representation of a monument’s changes organized as a function of time.

Recording only episodes when changes occur as opposed to a complete time-line that contains an entry for every tick of the clock, can also be viewed as temporal run-length encoding. This is analogous to raster run-length encoding for recording spatial variation. In this, a value is recorded only when it is different from the last one along the scan-line. The length of the run of contiguous dates (locations) on the scan-line can also be recorded as either starting/ ending locations or as an increment value $D _ { \mathrm { y } } .$ . Thus, for run-length encoding, only meaningful dates in time or locations in space are recorded. In the spatial domain, this usually coincides with some change over space. This can be an edge, such as a dome’s boundary or a change in construction materials from stones to bricks.

The top-level of information is the object list since an object, through its 3D model, usually represents a change in state (i.e. geometry, some property, attribute values, etc.) that can be described for some feature, location, set of features and locations. Besides sudden changes that might be caused by some catastrophic event (like fire or war), change can also be gradual such as the number of bricks or the type (form) of a dome’s architecture for a particular x, y location. For gradual change, a change object (3D model) would be recorded when the amount of accumulated change is considered to be significant, or according to some domain-specific rule.

In the objects-based approach, the time associated with each change is stored in increasing order from the initial state at $t _ { 0 }$ (e.g. 10 January 1902) to the latest recorded change $t _ { n }$ (e.g. 31 October 1998). These may be recorded at any desired resolution (e.g. year, month, day). For most phenomena, the length of any temporal interval will vary. Associated with each $t _ { i }$ are the changes, which occurred between $t _ { i - 1 }$ and $t _ { i } .$ The only exception to this is that the starting state must be stored with the first time $t _ { 0 } .$ . The changes associated with any $t _ { i }$ may also be extensive, affecting a large historical/archaeological area and many monuments.

## 4. The spatio-temporal data model

A specific data model is now defined. It is called the GST-DigiDoc data model and represents a specific example of the time-based approach that temporally orders changes to 3D modeling within a pre-specified monument. An initial generalized form of GST will first be described before presenting formulation and implementation details.

The GST-DigiDoc in its simplest form stores specific changes associated with each time $t _ { i } ,$ in the timeline (see Fig. 2). The specific stored time $t _ { i }$ is called a time-stamp, using the convention of the temporal database management systems (TDBMS) terminology [10]. It is assumed that each time-line and associated 3D modeling changes are related to a single thematic domain (e.g. Byzantine monuments). The set of 3D monument models, recorded for any $t _ { i } ,$ consists of the x, y starting co-ordinates of the monument component element which has changed since its previous values at $t _ { i - }$ <sub>1</sub>, and a pointer to the corresponding 3D component model.

One obvious potential disadvantage of storing modeling change is that the number of x, y, attribute values, pointer records is related directly to the total number of discrete component elements which changed between $t _ { i }$ and $t _ { i - 1 }$ . The representation of changes for a specific time-stamp consists of grouping together individual cell locations (i.e. x, y pairs) that share a common new attribute value. Then, the tabular/graphical display is acquired by using the pointer ptr. Such a pointer-to-model specific mapping is stored within a single structure, called a display file.

![](/api/attachments/FTHCEB6H/fulltext/images/d462e27c205851a8a07a8f26a47b6eedb23471de012e958a2ceacfb22e88fd79.jpg)  
Fig. 2. The display file structure of the GST-DigiDoc.

In GST, all component elements that have changed within a single thematic layer, regardless of their location or previous value, are stored together as members of the same dummy component. This means that any given value is stored only once per monument instead of once for every x, y component’s location (space optimization). A separate component structure, called a segment table, is stored for each value for which at least one locational cell has changed. By storing locations in this manner, it is also possible to apply raster run-length encoding within each component in order to reduce the volume of storage space for locations of component elements. Grouping locations, which changed to a common value also greatly aids certain search tasks.

The display file and segment table structures are defined as having two primary elements: the new value, termed a component descriptor, and an array of space-defined elements termed tokens (records). A single token represents a set of consecutive cells along a row in a grid-based map utilizing run-length encoding. It consists of five entries: the row number $x _ { i } ,$ the column number $y _ { i } ,$ the name of the component element, the ‘same’ value and a pointer to the 3D model.

Utilizing the neutral terms of components and tokens, the object-based model can be defined as being composed of a series of temporal locations, each corresponding to a single point in a 1D time-line, and one or more components associated with each of the points containing the new values and the elements to which they apply.

## 4.1. The GST-DigiDoc data structure

The GST structure as implemented, consists of a header, a base-map that defines the initial state of the entire monument at $t _ { 0 } ,$ , and a time-line with set of monument’s component elements attached to individual time-stamp entries in the time-line (see Fig. 3). A single GST-formatted file that represents the spatiotemporal dynamics of a single thematic domain for a specific archaeological area, equivalent to a single thematic map layer, is called a GST series.

![](/api/attachments/FTHCEB6H/fulltext/images/83c52736abcf4c43996e732da00b52a481de14789609008c00d0ee3a2a3c6e0f.jpg)  
Fig. 3. The GST-DigiDoc showing all primary elements and the pointer structure.

The header contains the name of the thematic domain, a pointer to the base map, the name of the base map, the time-stamp of the initial time value associated with the base map, and pointers to the first and last elements of the time-line. The base-map consists of a complete raster run-length encoded snapshot image of the entire monument.

Each object entry in the time-line contains a timestamp, a list of pointers to each component element (3D model), and a pair of pointers, prev and next, that point to the elements in the modeling list. The pointer prev of the first element points back to the header and the pointer next of the last element in the list is assigned the value NULL.

The use of pointers to connect adjacent entries allows new 3D models that emerge to be easily added. This conceptually entails new models to be added at the end of the modeling list. At the implementation level, the use of pointers allows GST-formatted files to expand in order to accommodate the additional data while avoiding the need to recopy the file. Adding a new 3D model (which has occurred more recently than the last model in the modeling list) onto the end of the modeling list.

The separation of the base-map in a GST series, as a separate element and not as an event component, is done for both representational and efficiency reasons. Obviously, t must be considered as the beginning of time as far as the data are concerned. This means that the nature of the values for all locations at that time is unique: it would not be valid to view these initial locational values as a change.

On a practical level, this initial world state is the only necessary exhaustive inventory of values for all locations, and it is used as the base from which any later world state can be derived and reformatted into a complete snapshot, if desired, by accumulating subsequent changes for the entire area to the desired time. For data representing temporally transient phenomena and management issues associated with specific types of monuments or/and archaeological sites, the basemap may not be relevant, since there is no temporal continuity for this form (type) of architecture relative to a specific geographical area.

## 5. Functional evaluation of the GST-DigiDoc

The most significant and unique capabilities of GST-DigiDoc, in a GIS/DSS context, arise from its ability to aid temporal reasoning, e.g. temporal scale change, and time-based comparisons. The primary ordering of information, on the basis of time, facilitates search and retrieval of change to specific living system values within those temporal intervals.

Such an ordering also makes comparison of different temporal sequences for the same or differing thematic domains for historical living systems, a straightforward task of comparing two or more GST series by comparing the time-stamps in their respective time-line.

The hierarchical organization of data offers additional functional advantages. For comparing only the times at which events occur, the times alone are retrieved directly from the time-line without a need for retrieving the associated attribute values or 3D models. Also, since changes associated with each event are organized on the basis of each unique value occurring during that event, the frequency and variability of occurrences of specific values, regardless of their spatial location, can be examined as changes through time. Using the third level in the storage organization, questions relating to locational changes (e.g. which 3D models of artefacts, monuments or archaeological sites were changed to a specific value or set of values at a given time?) can be easily answered.

## 5.1. Time-based queries

Specific algorithms are now derived to serve as examples of how implementing time-based queries can be straightforward and efficient using the GST-DigiDoc. These also serve as some of the elementary building blocks for implementing more complex and application-specific tasks.

1. Retrieve and Display in tabular or graphics form all component element objects, in artefacts, monuments, and archaeological sites, which:

(a) were changed to, or

(b) had a given attribute value at a given time.

The retrieval of all 3D component element models which changed to a particular given attribute value gav at time $t _ { i } ,$ is the most fundamental retrieval task for which GST was designed. The basic procedure for accomplishing this task is a two-stage search. The first is to find the event with the desired time-stamp within the time-line. The second is to find the component c, associated with this event whose descriptor matches the given value gav, the component co-ordinates are returned.

Since the time-line is arranged in increasing temporal order, the first stage relies on a comparison of whether the given time $g _ { t } ,$ is greater than the time-stamp in the event list. If $t _ { \mathrm { f i r s t } } > g _ { t } .$ then the event was later than the search requested and it returns FAIL. Otherwise, the search continues until $t _ { e } > g _ { t }$ , where $t _ { e }$ is the time associated with the event $e .$ Here, it is assumed that the value of $g _ { t }$ does not necessarily match any time-stamp stored in the time-line. If $t _ { e } < > g _ { t } ,$ the simple rule of closest temporal distance is applied, i.e. whether $t _ { e }$ or $t _ { e - 1 }$ is selected, although this depends on the application. As GST is defined as a complex structure, then the general logic of the algorithm can be described more formally (in Pascal-like coding) as

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Procedure Get&amp;Display_3-DModels_Value_Time(GST,  $g_{t}$ , gav)
Begin
    if ( $t_{first} &gt; g_{t}$ )
    return FAIL;
    for each Monument (3-D Object) in GST
    if ( $t_{e} &gt;= g_{t}$ )
    begin
    if ( $g_{t} &lt;= ((t_{e} + t_{e-1})/2)$ )
    3-D Model = previous (3-D Model);
    for each component c of the 3-D Model
    if (c(value) = gav)
    return c(xy-coordinates);
    end;
    return NULL;
End; {Procedure Get&amp;Display_3-Dmodels_Value_Time}
</div>

Since both the search of the time-line and of component descriptors within the desired event are exhaustive, linear searches have, as worst-case efficiency:

$$
\mathbf {O} (n _ {e} + n _ {c})
$$

where $n _ { e }$ is the total number of events in the timeline and $n _ { c }$ is the maximum number of components for any given event.

This can be improved to

$$
\mathrm{O} ((\log n _ {e}) + n _ {c})
$$

by using any O(log n) search, where n denotes the total number of elements to be searched.

In the case of closed-geometry historical living systems, an array of fixed size can be used and a binary search can be applied. This leads to O(log n) as the worst-case. For open-geometry historical living systems (artefacts of an archaeological excavation), a dynamic data structure (e.g. a balanced binary tree) can be used, where the searching time is, in the worst-case, O(log n).

Performing the same task by using the classical snapshot model, the following three steps would be required:

 Find the 3D model with the right time-stamp in the monument 3D models sequence.

 Create a difference monument 3D model between that model and the preceding model. This would then contain the new values in all 3D cells whose values had changed from the preceding model and zero or NULL in all cells whose values had not changed.

 Find those cells whose contents match the required changes.

The first and third steps are generally equivalent to the two-phase search as in the GST-based algorithm. The primary difference, however, is the addition of the second step to create a difference 3D. This is necessarily exhaustive; always requiring $( n _ { x } n _ { y } )$ cell-by-cell comparisons between two adjacent snapshots, where n is the total number of cells. This means that the entire task is performed in ${ \mathrm { O } } ( n ^ { 2 } )$ time for a complete snapshot image.

2. Retrieve and display in tabular/graphics form all component element objects, in monuments and sites, which:

(a) were changed to, or

(b) had a given attribute value over a given time interval.

This procedure utilizes a range of temporal values at the first level of search, retrieving element components for all monuments from a starting time gts to an ending/finishing time gtf. For the sake of simplicity, it is assumed that the temporal distance between gts and gtf is wide enough so that at least one 3D artefact/monument model will be found.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Procedure Get&amp;Display_3-DModels_Value_Interval(GST, gts, gtf, gav)
Begin
    if ( $t_{first} &gt; g_t$ )
    return FAIL;
    for each Monument (3-D Object) in GST
    if (gts &lt;=  $t_e$  &lt;= gtf)
    for each component c of the 3-D Model
    if (c(value) == gav)
    return c(xy-coordinates);
    return NULL;
</div>

End; {Procedure Get&Display\_3-DModels\_ Value\_Interval}

It can be seen that this task has the same logical structure involving the same two-level search. Given retrieval of 3D models with a temporal range of $g t f , . . . , g t s$ instead of a single model from a temporally ordered list, the time spent would be

$$
\mathrm{O} ((\log n _ {e}) + (n _ {f} \times n _ {c}))
$$

where log $n _ { e }$ is the amount of time needed to search the time-line for the starting event.

Since all object models after the start to the finish, are retrieved sequentially, this results in $n _ { f }$ additional steps. Also, for each 3D model, $n _ { c }$ additional steps are required to examine each component for each model. Thus $( n _ { f } \times n _ { c } )$ more steps are required.

The worst-case in terms of efficiency would be when the start time coincided with the first event in the time-line and the finish time coincided with the last event in the time-line. This would require all components in the time-line to be examined. The resulting efficiency thus would be

$$
\mathrm{O} (n _ {e} \times n _ {c})
$$

3. Calculate and display in tabular/graphics form total changes in an archaeological site area to a given value over a given temporal interval.

Finding the amount of morphogenesis (geometry dynamic modeling) change is another basic query, both for finding the degree of change taking place over a specific time and for calculating the rate of change.

Within the GST-DigiDoc, the amount of morphogenesis change is represented by the total number of units represented within a component or within the c(xy-coordinates) returned by either of the algorithms. Since run-length coding is used for both, counting the total number of morphogenesis units requires a very simple procedure that accounts for the cells not explicitly stored in the structure. If the input xy-coordinates are represented by a run-length encoded list of georeferenced (x, y) or (x, y, z) cell locations returned from either of the algorithms, a GST morphogenesis change algorithm reduces to a simple counting procedure:

Procedure Morphogenesis\_Area (xy-list)

return area;

```txt
Begin
    area = 0;
    for each cell component with xy-coordinates
    area = area + c(xy-coordinates);
```

End; {Procedure Morphogenesis\_Area}

Obviously, the time efficiency of this procedure is a direct linear function of the number of compacted records in the xy-list.

## 6. Discussion

The general problem of the modeling process is a morphogenesis problem and it is still under design. It is a problem of all living systems, including human construction with historical interest. The historical living systems are defined as spatial-based artefacts, monuments and archaeological sites that involve time, morphogenesis 3D elements and events that have or will occur. These systems are associated with locations and time periods over which the entities and events occur. We need to investigate this important area of the, so-called sciences of complexity of the historical living systems.

In the past, many methods of spatial analysis were developed. However, there is still a need for exploration of new analytical techniques. In general, space syntax models the spatial configuration of the objects involved by using a 2D connectivity graph representation [8]. Such a representation identifies patterns that cannot be used to study objects through time, because such living systems are too complicated, with significant 3D geometry-based complexity.

This paper has presented methodological and practical evaluations of incorporating 3D functionality within traditional spatio-temporal GIS approaches. Even more, nowadays, using Internet and incorporated technologies (like collaborative Web engineering) the 3D modeling reduces the complexity of studying and managing remote systems.

## 7. Conclusions

In many real world applications a time-based representation model is needed to allow empirical analysis of space and time dynamics and thus allow temporal 3D modeling, simulation and management of geographical processes as an integrated GIS capability. Several approaches have appeared in the literature, however, none of them is based on CAD systems functionality and 3D geometry, but on a specialized (traditional) spatial database approach.

This paper introduced a new type of a spatiotemporal model for the digital documentation of historical living systems. The model has been described and evaluated. Unlike existing approaches used in GIS/SIS, it was designed to represent 3D modeling change relative to time. Its main contribution includes two aspects. First, GST is based on 3D geometry allowing morphogenesis functionality [19,20]. Second, because GST stores change relative to time in a controlled environment, procedures for answering queries related to temporal relationships, the management, and analytical tasks for comparing different sequences of change are aided by the system.

## Acknowledgements

The authors thank the editor and the three anonymous referees for their helpful comments on the earlier version of the paper and Ms. Marissa Bargouli for her assistance during working out at a preliminary version. The research work was supported by the joint Greece/EU’s Arximedes research project [action: 2.2.3.z].

## References

[1] A.D. Bell, On the astogeny of six-cornered clones: an aspect of modular construction, in: J. White (Ed.), Studies on Plan Demography: A Festschrift for John L. Harper, Academic Press, London, pp. 187–207.

[2] E. Bonabeau, From classical models of morphogenesis to agent-based models of pattern formation, Artificial Life 3 (3), 1997, pp. 191–211.

[3] S. Fotheringham, M. Wegener (Eds.), Spatial Models and GIS: New Potential and New Models, Taylor & Francis, London, 2000.

[4] R.H. Guting, M.H. Bohlen, M. Erwig, C.S. Jensen, N.A. Lorentzos, M. Schneider, M. Vazirgiannis, A foundation for representing and querying moving objects, ACM Transactions on Database Systems 25 (1), 2000, pp. 1–42.

[5] R.H. Guting, Geo-relational algebra: a model and query language for geometric database systems, in: International Conference on Extending Database Technology (EDBT’88), 1988, pp. 506–527.

[6] T. Hadzilacos, N. Tryfona, Logical data modeling for geographical applications, International Journal in Geographical Information Systems 10 (2), 1996, pp. 179–203.

[7] N.W.J. Hazelton, Integrating time, dynamic modelling and geographical information systems: development of fourdimensional GIS, Ph.D. Dissertation, Department of Surveying and Land Information, The University of Melbourne, Australia, 1991.

[8] K. Hornsby, Deriving summaries through an identity-based approach, in: Proceedings of the FLAIRS’2000, Orlando, FL, 2000, AAAI Press, pp. 271–275.

[9] L. Ibanez, C. Hamitouche, M. Boniou, C. Roux, Morphogenesis-based deformable models application to 3-D medical image segmentation and analysis, in: Proceedings of the MICCAI, 2001, pp. 1369–1370.

[10] C.S. Jensen, J. Clifford, S.K. Gadia, A. Segen, R.T. Snodgrass, A glossary of temporal database concepts, in: Proceedings of the ACM International Workshop on an Infrastructure for Temporal Databases, 1993, pp. A25–A29.

[11] G. Langran, Time in Geographic Information Systems, Taylor & Francis, London, 1997.

[12] G. Langran, Ternporal GIS design trade-offs, Journal of URISA 2, 1990, pp. 16–25.

[13] S. Madon, S. Sahay, Managing natural resources using GIS: experiences in India, Information & Management 32 (1), 1997, pp. 45–53.

[14] E. Malcolm, Requirements acquisition for rapid applications development, Information & Management 39 (2), 2001, pp. 101–107.

[15] J.-L. Le Moigne, Formalisms of systemic modelling, in: Some Physicochemical and Mathematical Tool for Under standing of Living Systems, University of Geneva, 1993, pp. 3–22.

[16] J.-L. Le Moigne, Natural and artificial computing and reasoning in economics affairs, Theory and Decision 27 (1/ 2), 1989, pp. 107–117.

[17] S. Nasirin, D.F. Birks, DSS implementation in the UK retail organisations: a GIS perspective, Information & Management 40 (4), 2003, pp. 325–336.

[18] D.J. Peuquet, Raster Data Handling in Geographic Information Systems, Harvard Papers on Geographic Information Systems, 1978, pp. 68–76.

[19] P. Prusinkiewicz, M. Hammel, R. Mech, Visual models of morphogenesis: a guided tour, 1997. www.cpsc.ucalgary.ca/ Research/bmv/vmm-deluxe/TitlePage.html.

[20] P. Prusinkiewicz, Visual models of morphogenesis, Artificial Life 1 (1/2), 1994, pp. 67–74.

[21] Y. Spanos, G.P. Prastacos, A. Poulymenakou, The relationship between information and communication technologies adoption and management, Information & Management 39 (8), 2002, pp. 659–675.

[22] A.D. Styliadis, P.G. Patias, N.C. Zestas, 3-D computer modeling with intra-component, geometric, quality and

topological constraints, Informatica 14 (3), 2003, pp. 375– 392.

[23] A.D. Styliadis, I.G. Paraschakis, M. Zhou, Spatio-temporal analysis and digital documentation, Journal Monument & Environment 7, 2001, pp. 169–181.

[24] A.D. Styliadis, GUI and monument manipulation, Journal Monument & Environment 3, 1997, pp. 113–134.

[25] C.D. Tarantilis, C.T. Kiranoudis, Using a spatial decision support system for solving the vehicle routing problem, Information & Management 39 (5), 2002, pp. 359–375.

[26] T. Tzouramanis, M. Vassilakopoulos, Y. Manolopoulos, Overlapping linear quadtrees: a spatio-temporal access method, in: Proceedings of the Sixth ACM GIS, Bethesda, MD, 1998, pp. 1–7.

[27] T. Tzouramanis, M. Vassilakopoulos, Y. Manolopoulos, Benchmarking access methods for time-evolving regional data, Data & Knowledge Engineering, in press.

[28] J.R.R. Viqueira, Formal extension of the relational model for the management of spatial and spatio-temporal data, Ph.D. Dissertation, Department of Computer Science, The University of A. Corunia, Spain, 2003.

[29] M.F. Worboys, A unified model for spatial and temporal information, The Computer Journal 37 (1), 1994, pp. 34– 36.

[30] I.-L. Wu, A model for implementing BPR based on strategic perspectives: an empirical study, Information & Management 39 (4), 2002, pp. 313–324.

[31] H. Zhuge, J. Chen, Y. Feng, X. Shi, A federation-agentworkflow simulation framework for virtual organisation development, Information & Management 39 (4), 2002, pp. 325–336.

![](/api/attachments/FTHCEB6H/fulltext/images/b6f2f3dccb70f87ee577f605885415f9a82fd898936f63b3a876cc7e1b5ec8de.jpg)

Athanasios D. Styliadis is an Associate Professor at the Department of Information Technology at the Alexander Institute of Technology (ATEI), Thessaloniki, Greece. He was born in 1956 in Florina, Greece. He received a Diploma in surveying engineering (Aristotle University of Thessaloniki, Greece; 1980), an M.Sc. in computer science (Dundee University, Scotland, 1987), and a Ph.D. in CAD/

GIS/computer modeling (Aristotle University of Thessaloniki, Greece, 1997). He was a Fellow Research Scholar at the Department of Geomatics, University of Melbourne and at the Center for GIS and Modeling (CGISM), Australia. He has over 60 publications in refereed scientific journals and conference proceedings and is the author of three books (‘‘Computer Graphics—Algorithms and Programming’’, ‘‘Programming the User Interface in Human–Computer Interaction—A Computing GIS Perspective’’, ‘‘GIS—Spatial Reasoning and Geomatics Engineering’’). He has been worked at the Hellenic Army Geographical Service (HAGS, Athens) for 3 years as GIS system analyst and programmer. His research interests include: computer modeling, web-based CAD, temporal GIS systems, concurrent engineering and 3D geometry, and digital documentation of monuments and sites. http://www.it.teithe.gr/	styl.

![](/api/attachments/FTHCEB6H/fulltext/images/a152083b54613ce59c15c37fea5e6d80bdd7439437b65eff1d9eb074101cbdff.jpg)

Michael Gr. Vassilakopoulos is an Associate Professor at the Department of Information Technology at the Alexander Institute of Technology (ATEI), Thessaloniki, Greece. He was born in 1967 in Thessaloniki, Greece. He received a Diploma in computer engineering and informatics (University of Patras, Greece, 1990), and a Ph.D. in computer science (Aristotle University of Thessaloniki, Greece, 1995). He followed post-doctoral studies at the Laboratory of Data Engineering/Department of Informatics at the Aristotle University of Thessaloniki. He has published over 40 papers/chapters in refereed scientific journals, conference proceedings and books. He has been with the Department of Applied Informatics of the University of Macedonia and the Department of Informatics of the Aristotle University of Thessaloniki. For 3 years he also served the Greek Public Administration as an Informatics Engineer. His research interests include: spatial and spatio-temporal databases, GIS, WWW, multimedia, and information systems integration. http://www.it.teithe.gr/ vasilako.
