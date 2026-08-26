---
otero_id: 17428
otero_key: "229HTH2J"
title: "Two-dimensional colour pattern load analysis: A tool supporting demand-side management"
authors: "S. Mitropoulos; V. Assimakopoulos; Y. Charalabidis"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)e0054-h"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Two-dimensional colour pattern load analysis: A tool supporting demand-side management

S. Mitropoulos \*, V. Assimakopoulos, and Y. Charalabidis

Decision Support Laboratory - Energy Policy Unit, National Technical University of Athens, Department of Electrical and Computer Engineering, 42, 28th October Str., GR 10682 Athens, Greece

## Abstract

Load analysis is one of the most important operations that support demand-side management in large electric utilities. Ordinary load analysis techniques stress on statistical processing of hourly load data along predefined time axes, producing numerical results of a standard granularity, such as daily or weekly mean loads. In order to overcome these limitations, a new approach or load analysis was developed, based on applying a two-dimensional formulation of the hourly load data. The tables holding energy consumption values, where columns represent the days of the selected period and lines represent the 24 hours of the day, are then illustrated through the use of colour patterns. In such a way, chronological typical units of variable structure and granularity can be identified and provide the basis for an extensive cross-examination, resulting in optimized decision making and energy policy definition. In order to demonstrate the advantages of the approach, a dedicated DSS implementation and application in the Greek public power corporation was also performed.

Keywords: Decision support systems; Compute graphics; Pattern recognition; Demand-side management; Load analysis

## 1. Introduction

One of the most important problems an electric utility faces is whether it is feasible to know the exact behaviour of the energy consumption that is the general shape of the consumable load during a period. This knowledge is important because it leads to more effective demand side management $[3,6]$ .

The general load behaviour during a period affects significantly utility planning and strategic corporate objectives (improve earnings and cash flow, reduce risks, etc), [6]. To achieve these business objectives, generic load shape changes are often necessary, as for example peak clipping, valley filling, load shifting, energy conservation, load growth and flexible reliability $[1,3]$ . So, the diagnosis of the electric power system behaviour from the point of view of energy consumption, is necessary in conjunction with the general shape of its load and the variations of this shape during the year $[5]$ .

However, the approaches to the problem presume that the granularity in which the behaviour of electricity consumption will be analyzed is standard and irrelevant to the various consumption profiles. The most commonly used typical unit, in statistics-oriented decision support systems used for load analysis, is the typical day?

In the present work, a step forward is attempted. The objective is to find typical units within the examined period, that are relevant to the electricity consumption profile, and therefore obtain more general patterns of load behaviour. These patterns will now be characterized by the specific electric system, without presuming its electric consumption behaviour. The typical units are adapted in time, while the generalization of the typical unit definition leads to more general and accurate patterns spanning across days and weeks [5].

Furthermore, in order to assist the identification of the afore-mentioned patterns, the hourly load data is presented in coloured two-dimensional maps by assignment of different colours to value ranges, thus transforming the problem of typical unit definition to a pattern recognition and matching process.

The following section presents the methodology in detail emphasizing on the two-dimensional tables, the measured parameters and the typical unit definition. Sections 3 and 4 describe the implementation and application of a computer-based decision support system dedicated to load analysis by this methodology, while section 5 concludes the work done.

## 2. A novel methodology for supporting decisions in demand-side management

## 2.1. Table construction and colouring

For each selected period, a two-dimensional table is created from the hourly load data.

The first dimension is the twenty four hours of a day. The general load shape with regard to the time of the day is influenced by the fluctuations of the temperature, the policy of invoice, the selected day type (holiday or working day), etc. [5].

The second dimension is the selected period, i.e. from 1 January to 31 December. The load shape in this dimension follows some general figure per hour, which obviously depends on the season or the temperature, among other factors. In this way, on the two-dimensional table of the selected period, the days of the period are its lines, while the 24 hours of the day are its columns. In other words, an energy demand calendar map is created.

Through applying fundamental image processing concepts, each range of values of the indicators corresponds to a different colour, resulting in a coloured map. In this two-dimensional coloured board typical units and more general patterns of energy consumption behaviour are searched for. The colour choice must fulfill two prerequisites. Firstly, the basic colours, which express the levels of the indicator values, must follow the same sequence with those of the colour spectrum [4]. Secondly, apart from the basic colours there should also exist various colour grades corresponding to the continuous nature of the underlying values.

## 2.2. Typical units

In the homogeneous areas of the two-dimensional coloured table, the loads have a common behaviour. In this way, there are defined a posteriori some areas in the energy consumption calendar map, that generally show a kind of homogeneous behaviour, depicted by a colour with its shades. Such an area represents a typical unit for a specific electric power system and defines the pattern of energy consumption. For the sets of loads which belong in the typical unit limits, there is no clear pattern of their behaviour.

![](/api/attachments/229HTH2J/fulltext/images/fb2a2d95f14a819f6a84fe34e69dc03e4c1c08aa581c1d1bb7ddf77a04124892.jpg)  
Fig. 1. Ordinary and two-dimensional colour pattern load analysis.

![](/api/attachments/229HTH2J/fulltext/images/0e23298482e54918559758e6e5cb0d54c9622aa8a4ac1afa43eac5113ffaac48.jpg)  
Fig. 2. Two-dimensional table of indicator 1 for all days of 1985.

Beyond that, comparingly to a one-dimensional presentation, the information obtained from the two-dimensional presentation is richer in data (hourly load values) and therefore constitutes a more realistic picture of the energy consumption [2]. So, someone may fit policies for generic load shape changes, for example, peak clipping or valley filling. Finally, it is examined how these typical units or the whole shape of a period, behave during a number of years. In other words, two periods for the stability of the typical units of the examined energy system are compared the fact that the colour shades (level of values) of these units (areas) alter in time is also examined. This analysis can contribute to a more effective demand side management (Figure 1).

## 3. The design and implementation of the system

## 3.1. The colours

Within the framework described above, a software package was developed. The implementation of the two-dimensional coloured analysis for the two-hourly load indicators of a year or a certain subperiod, is performed on the basis of a colour scale comprised of lightgreen, yellow, red, and blue, representing values in an ascending order. Intermediate values between yellow and red are brown while those between red and blue are magenta. The shades were formed by the mixture of coloured pixel patterns with one of the basic colours. A legend is placed on the graphics screen informing the user of the level of values represented by each colour.

![](/api/attachments/229HTH2J/fulltext/images/3d63f48566be1b20d35f689fbe77d12cb13b3eff532d2ceb987e953661bdc88b.jpg)  
Fig. 3. Two-dimensional table of indicator 1 for all days of 1989.

## 3.2. The subperiod types

Because of the limited graphic analysis of a computer screen, details of the colour analysis of the period are missing. On the other hand, it is desirable to point attention to a subperiod of the year or to a subset of some of its days which are appropriately chosen. For overcoming such problems two-dimensional tables, rectangular subareas or selected lines of the year board are drawn, thus enhancing the resolution of the displayed table. This results in a detailed colour analysis of the hourly load indicator values and allows the independent examination of sub-areas. Those periods which have their hourly load values processed in the way mentioned above are:

Years. It is noted that, before the values of two years are processed, a kind of lining-up is done so that the two years start with the same day of the week, (for instance Tuesday) while the remaining days are ignored. This lining-up is used so that days of the same type are processed, something very important when the percentage change maps are produced.

Months. Two-dimensional maps of two months of the same or a different year, are produced. A lining-up of the days of the week is performed here as well.

![](/api/attachments/229HTH2J/fulltext/images/b93ab58afae4d38f45ee50504a741f89130b9bf822ea0ccba418fa1d8219ac97.jpg)  
Fig. 4. Two-dimensional table of indicator 2 for all days of 1989 and 1985.

![](/api/attachments/229HTH2J/fulltext/images/f8c89d780a164ba6153289c7515e41a793939580df8588b0d0f8fbcfc951a187.jpg)  
Fig. 5. Load factors comparison.

Selected days. From the hourly load data of a year, a season, a month, or a week, the user can choose: the working days either separately (all Mondays, ..., all Fridays) or all together, all Saturdays, all Sundays, all steady holidays (in case of yearly processing).

## 3.3. Processing the subperiods

The analyst usually obtains the knowledge of energy demand, load peak and load factor for each period (year or month) and also how much these have changed. As a particularly useful tool, the analyst utilizes the two-dimensional coloured analysis in order to localize in which subperiods of a year or a month load shape changes were presented, or to evaluate their contributions to the load factor change, or to generally observe the behaviour pattern (typical units) of the examined period (year or month).

From the isolation of a specific type of hourly load data (e.g. all Mondays or working days) very significant information can be obtained. For example, the contribution of the chosen days to the formation of the pattern that the corresponding year presents, and their impact on changes of the load shape and the load factor.

![](/api/attachments/229HTH2J/fulltext/images/6aad77c1c89fa4258c071ce1d8a140668024e321ceb3ed0f32ab8fc5569ba6c8.jpg)  
Fig. 6. Energy demand comparison.

![](/api/attachments/229HTH2J/fulltext/images/0981261a68d9b3252931ba9d1947cd384bd6ccc5c665094d8b8c72a4d277e49b.jpg)  
Fig. 7. Peak values comparison.

## 3.4. The energy demand indicators

In the developed system, the processing is performed on the basis of two-hourly load indicators.

The first indicator is defined as the ratio of the hourly load value that corresponds to a position in the two-dimensional coloured maps, to the peak load of the whole period. Values are normalized to unity, so that the behaviour pattern of a period can be compared with the pattern of another period. This indicator is appropriate for the definition of the typical units in the calendar load map, the specification of behaviour patterns, the performance of comparisons between patterns, the localization of load shape and load factor changes.

The second indicator is defined from the percentage difference between two corresponding hourly loads of two selected periods. Based on this indicator a two-dimensional coloured calendar map is produced, which expresses the levels of the percentage differences between the subperiods of the two selected periods. The observation of the first and second indicator maps provides a more accurate knowledge of the load shape and load factor changes.

![](/api/attachments/229HTH2J/fulltext/images/a698cff83068f3502150e9e6ef79c355d2c069bd2948fa02f3f8dd5cc97152b5.jpg)  
Fig. 8. 2-dimensional table of indicator 1 for all Wednesdays of 1985.

![](/api/attachments/229HTH2J/fulltext/images/4e66356a9a1715de2ee29eca28cdf80d999e0a4a10482b0eddbb841c3a18acc2.jpg)  
Fig. 9. 2-dimensional table of indicator 1 for all Wednesdays of 1989.

## 3.5. Usage example

The software package developed operates in high-end IBM-compatible personal computers equipped with an S-VGA graphics card, under MS-DOS operating system. It presents an attractive user/computer interface which is based on windowing menus, editor facilities, error messages, and computer graphics. Full control of interfacing devices (keyboard, mouse) and presentation facilities (laser and inkjet colour printers) is also supported. For supporting the portability of the system in other platforms (UNIX, WINDOWS) the programming language was standard C, supported with user interface building libraries.

## 4. Application in the Greek public power corporation

A full analysis took place for the hourly loads of the Greek interconnected system for the years 1985 to 1989. Comparing the two calendar coloured maps (Figures 2 and 3) of the years 1985 and 1989, similar colour patterns are displayed. In these figures, some coloured homogeneous regions are observed. These regions express the typical units of the Greek interconnected power system.

![](/api/attachments/229HTH2J/fulltext/images/653aac1d29067ff02dce3df9219336513c00b770ac62b7a8da5f131ebb1e58d0.jpg)  
Fig. 10. 2-dimensional table of indicator 2 for all Wednesdays of 1989 and 1985.

![](/api/attachments/229HTH2J/fulltext/images/e6158fb1851a04f952c5d0adaef2ea9af8b1df7ed1520839ed681d64df3abbb0.jpg)  
Fig. 11. Typical Wednesday for 1985 and 1989.  
Fig. 13. Memorandum for 2-dimensional table of indicator 2.

The load factor of 1985 and 1989 was 68.607% and 70.639%, respectively which means that a 2.032% change or 2.96% percentage difference was presented (Figure 5). So, a change in the colours of the two maps is expected, from colours corresponding to low values as well as to high. This change is actually shown in Figures 2 and 3 and is greater for the midnight and early morning hours during the year, and particularly for the spring and summer days. The knowledge of the behaviour of energy consumption (Figure 6) in conjunction with the knowledge of peak demand (Figure 7) and the two-dimensional tables (Figures 2 and 3) provide a better picture of the load factor behaviour.

Between 1985 and 1989 there was a 17.13% increase in energy consumption (Figure 6). Figure 4 shows the maps of indicator 2 which expresses the percentage difference between two corresponding hourly loads of those years. As each colour expresses a level of value change, it can be observed in Figure 4 that energy consumption was increased. The early morning and after midnight hours presented a great amount of change, similarly to all hours during the winter and summer days.

Any selected period (year, month, typical day) can be presented by the system, as is mentioned in the previous paragraphs. It is remarkable, that the normalization base of the hourly load values is the peak of either the examined subperiod or of the selected days. This is important because someone can examine these days independently from the other ones. For example Figures 8 and 9 depict the behaviour patterns which correspond to all the Wednesdays of the years 1985 and 1989. So, typical units for this particular day can be defined. Independent load factor analysis can also be performed, as well as examination of the energy change distribution based on the map of indicator 2 of these days (Figure 10). Comparisons with Figure 11, which shows the one-dimensional typical Wednesday load pattern of the two years; give identifications and deviations from this pattern.

The system was installed in the power corporation and used by its executives and analysts, in parallel with their existing systems. Their remarks were very encouraging on the whole, identifying important decision support features and leading to very interesting conclusions.

## 5. Conclusions

The application of the two-dimensional colour pattern load analysis system for supporting decisions in the demand-side management operations of the Greek public power corporation showed that both the methodology and the implementation were effective and useful. The main conclusions are presented below.

\- Two-dimensional load analysis provides well-structured sets of correlated results that can serve as the basis for estimating all the important indicators of energy demand.

\- Colour patterns greatly assist in the instant comprehension of complex result structures leading to successful establishment of the proper typical units for further analyses.

\- The variable granularity of the system, that allows closer examination of selected years, periods, months or days, according to the established typical unit or pattern is a powerful characteristic.

\- The approach and the system have to be further enhanced, in the directions of pattern recognition and matching, multi-dimensional analysis and connectivity with existing systems for demand-side management.

## Acknowledgement

The authors wish to acknowledge the public power corporation of Greece for providing the data.

## References

[1] I. Benbasat and B. Nault, An Evaluation of empirical Research in Managerial Support Systems, Decision Support systems 6 (3) (1990).

[2] S.H.C. du Toiot, A.G.W. Steyn and R.H. Stumpf, Graphical Exploratory Data Analysis (Springer-Verlag, 1986).

[3] C. Gellings, Demand-Side Management, EPRI selected papers on Demand-Side Management, June 1985.

[4] Illuminating Engineering Society of North America, IES Lighting Handbook, Reference Volume, 1984.

[5] S. Mitropoulos, V. Assimakopoulos and J.-E. Samouilidis, GLAS: A PC based software tool for load analysis, accepted for publication to Athens Power Tech 1993, NTUA-IEEE/PES.

[6] J. Schaefer, Cost-benefit analysis of energy management research, EPRI selected papers on Demand-Side Management, June 1985.

Sarandis Mitropoulos is a doctoral candidate in the Department of Electrical and Computer Engineering at the National Technical University of Athens (NTUA), funded by the Greek Government Institute of Scholarship. He received his diploma in electrical engineering from the NTUA in 1990. His current research interests include distributed system, network management, multimedia technology and decision support systems.

Vassilis Assimakopoulos is Assistant Professor in the Department of Electrical and Computer Engineering at National Technical University of Athens (NTUA). He received his Ph.D. in energy forecasting from the NTUA in 1988. His research interests include forecasting, artificial intelligence, decision support systems and optimization techniques.

Yannis Charalabidis is an Electrical and Computer Engineer of National Technical University of Athens, aiming at a Ph.D. in object-oriented software engineering. His current research interests include object-oriented data and knowledge bases, multimedia databases, knowledge-based systems and artificial intelligence.
