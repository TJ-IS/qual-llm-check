---
otero_id: 20903
otero_key: "EF8RNEQZ"
title: "Solving power flow problems with a Matlab implementation of the Power System Applications Data Dictionary"
authors: "Fernando L. Alvarado"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00102-0"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Solving power flow problems with a Matlab implementation of the Power System Applications Data Dictionary

Fernando L. Alvarado

ECE Department, The UniÕersity of Wisconsin, Madison, WI 53705 USA

## Abstract

This paper implements a power flow application and variations using the IEEE Power System Application Data Dictionary PSADD within a Matlab environment. It describes a number of useful data and implementation techniques for a Ž . variety of applications. The techniques include the use of very compact and efficient code for the computation of Power Transfer Distribution Factors PTDF . PTDF are an important element of present and proposed congestion managementŽ . strategies for power systems, particularly when these systems must operate in a deregulated environment. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Power system databases; Data exchange; Applications interfaces; Common information model; CIM; IEEE common format

## 1. Introduction

This paper provides a brief overview of the major elements of the IEEE Power System Application Data Dictionary PSADD . It utilizes PSADD ele-Ž . ments toward the creation of flexible general-purpose power flow environments that have great expandability and flexibility. The PSADD is intended primarily as a means for exchanging application data among power system analytical applications of various types. The paper then uses an environment closely based on PSADD concepts toward the creation of sample applications in Matlab. The two main applications considered are: a simple vanilla power flow and a rapid and efficient computation of Power Transfer Distribution Factors PTDF . TheŽ .

paper is intended as a means of documenting efforts conducted by PSerc<sup>1</sup> toward the creation of a unified environment for power flow analysis, as a means for illustrating and popularizing the data dictionary itself, and as a means for illustrating Matlab vectorized computation techniques and methods. The paper contains much actual code because it is intended for use in its electronic form, where users are expected to be able to cut and paste examples to a Matlab environment directly from the text of the paper.

## 2. The data dictionary

The PSADD is an attempt by IEEE to extend and renovate the old standby of the power industry, the

Table 1  
Miscellaneous data subsetŽ .

<table><tr><td>Name</td><td>Description</td><td></td></tr><tr><td>Misc.Title</td><td>User defined case title</td><td>T</td></tr><tr><td>Misc.BaseMVA</td><td>MVA base</td><td>R</td></tr><tr><td rowspan="3">Misc.ModelConnectivityType</td><td>BM or Bus.Model</td><td>T</td></tr><tr><td>BS or BusSection*</td><td></td></tr><tr><td>BO or Both*</td><td></td></tr><tr><td rowspan="3">Misc.ContingencyGenMWResponse</td><td>RF = Use response factors</td><td>T</td></tr><tr><td>PC = Proportional to capacity</td><td></td></tr><tr><td>PO = Proportional to output</td><td></td></tr><tr><td>Misc.DeviceRefMethod</td><td>Method (i.e. Number or Name) used as for referencing a device.</td><td>T</td></tr></table>

IEEE common format 1 , which served the industry <sup>w</sup> <sup>x</sup> well for many years. The data dictionary is meant primarily as a definition of terms used for analytical applications within power system models. It is organized around the notion of objects. Within this paper, we consider objects to be structures within the Matlab environment. Each object contains a number of attributes or fields. As such, each object constitutes a relational database. The following is a list of all data types defined in the dictionary. Boldface indicates data types that are used in the present paper. Some of the data types are defined but declared obsolescent:

v Company data

v Connectivity node data

v Data exchange data

v Equivalent AC series device data

v Equivalent injection<sup>r</sup>shunt device data

v Generator data: obsolete, see machine data

v Interchange control data

v Line data

v Load data

v Machine synchronous data( )

v Miscellaneous application data

v Ownership data

v Rating data

v Reactor data: obsolete, see shunt device data

v Bus data

v Analog data

v Capacitor data: obsolete, see shunt device data

v Area

v Set data

v Shunt nonsynchronous device data( )

v Station data

v Status data

Table 2  
Subset of Analog data table

<table><tr><td>Name</td><td>Description</td><td></td></tr><tr><td>Analog.Number</td><td>Unique number</td><td>I</td></tr><tr><td rowspan="6">Analog.Type</td><td>VOLT = voltage magnitude</td><td>T</td></tr><tr><td>FLOW = Power or current</td><td></td></tr><tr><td>MW = Active Power</td><td></td></tr><tr><td>MVAR = Reactive Power</td><td></td></tr><tr><td>TAP = Transformer Tap</td><td></td></tr><tr><td>ANGL = Voltage Angle</td><td></td></tr><tr><td rowspan="2">Analog.AssignDevice</td><td>Device type associated with value (complete spelling or abbreviation of one of the root entities). Some possibilities are: BS = Bus LN = Line TR = Xformer SW = Switch</td><td>T</td></tr><tr><td>MA = Machine LD = Load SH = Shunt</td><td></td></tr><tr><td>Analog.DeviceRef</td><td>Device assignment (Bus.Number, Line.Number) of value on device for device type.</td><td>I</td></tr><tr><td>Analog.Value</td><td>Numeric value</td><td>R</td></tr></table>

Table 3  
Subset of Bus data table

<table><tr><td>Name</td><td>Definition</td><td></td></tr><tr><td>Bus.Number</td><td>Bus number</td><td>I</td></tr><tr><td>Bus.Name</td><td>Bus name</td><td>T</td></tr><tr><td>Bus.BasekV</td><td>Base voltage RMS</td><td>R</td></tr><tr><td>Bus.Status</td><td></td><td>I</td></tr><tr><td>Bus.Vmag</td><td>Magnitude of bus voltage. Solved value.</td><td>R</td></tr><tr><td>Bus.Vangle</td><td>Phase angle of bus voltage. Solved value.</td><td>R</td></tr><tr><td>Bus.MWMismatch</td><td>Net Mw not assigned to generator, load or shunt</td><td>R</td></tr><tr><td>Bus.MvarMismatch</td><td>Net Mvar not assigned to generator, load or shunt</td><td>R</td></tr><tr><td>Bus.TypeCode</td><td>* L or Load (no control)* CB or ControlToBand* CT or ControlToTarget* S = Swing (or reference)* I = Isolated</td><td>T</td></tr><tr><td>Bus.VoltTarget</td><td>Voltage magnitude setpoint</td><td>R</td></tr><tr><td>Bus.LowVoltLim</td><td>Voltage control band lower limit</td><td>R</td></tr><tr><td>Bus.UpVoltLim</td><td>Voltage control band upper limit</td><td>R</td></tr><tr><td>Bus.ControlPriorityCode</td><td>T = transformerS = Synchronous machineN = nonsynchronous shunt</td><td>T</td></tr></table>

v Switching device data

v Terminal

v TieSwitch data

v Transaction data

v System

v Transformer data

## Table 4

Subset of Machine data table

<table><tr><td>Name</td><td>Description</td><td></td></tr><tr><td>Machine.Number</td><td>Unique Number</td><td>I</td></tr><tr><td>Machine.BusRef</td><td>Bus.Number to which machine is connected</td><td>I</td></tr><tr><td>Machine.Id</td><td>Identifier</td><td>T</td></tr><tr><td>Machine.Status</td><td></td><td>I</td></tr><tr><td>Machine.MW</td><td>MW output, solved value</td><td>R</td></tr><tr><td>Machine.Mvar</td><td>MVAR output, solved value</td><td>R</td></tr><tr><td rowspan="4">Machine.ControlMode</td><td>PQ = hold P and Q constant</td><td>I</td></tr><tr><td>PV = adjust Q to hold V</td><td></td></tr><tr><td>NL = adjust Q, no limits</td><td></td></tr><tr><td>SW = case swing Machine</td><td></td></tr><tr><td>Machine.ControlledBusRef</td><td>Bus (Bus.Number) whose voltage is controlled</td><td>I</td></tr><tr><td>Machine.RatingId</td><td>Identification of ratings</td><td>T</td></tr><tr><td>Machine.RatingValue</td><td>A vector of possible generator maximum MW values</td><td>R</td></tr><tr><td>Machine.RatingMinimum( + )</td><td>A vector of possible generator minimum MW values</td><td>R</td></tr><tr><td>Machine.MinQOutput</td><td>Lower limit for reactive power</td><td>R</td></tr><tr><td>Machine.MaxQOutput</td><td>Upper limit for reactive power</td><td>R</td></tr><tr><td>Machine.MinOperatingVolt</td><td>Machine minimum operating voltage</td><td>R</td></tr><tr><td>Machine.MaxOperatingVolt</td><td>Machine maximum operating voltage</td><td>R</td></tr><tr><td rowspan="3">Machine.PostContRespFact</td><td colspan="2">Percent of Machine MW response to system MW imbalance.</td></tr><tr><td>R</td><td></td></tr><tr><td>Values are normalized for each island</td><td></td></tr></table>

Ž . <sup>q</sup> Not in the current version of the data dictionary.

Table 5  
Subset of Load data table

<table><tr><td>Name</td><td>Description</td><td></td></tr><tr><td>Load.Number</td><td>Unique Number</td><td>I</td></tr><tr><td>Load.BusRef</td><td>Bus.Number of bus to which load is connected</td><td>I</td></tr><tr><td>Load.Id</td><td>Identifier</td><td>T</td></tr><tr><td>Load.Status</td><td></td><td>I</td></tr><tr><td rowspan="3">Load.ModelType*</td><td>CONST = constant MW and MVAR</td><td>T</td></tr><tr><td>VFUNC = voltage depend</td><td></td></tr><tr><td>INDMOT = induction motor</td><td></td></tr><tr><td>Load.ModelMinVoltage*</td><td>Minimum model voltage for this models</td><td>R</td></tr><tr><td>Load.ModelMaxVoltage*</td><td>Maximum voltage for this load model</td><td>R</td></tr><tr><td>Load.MinMW*</td><td>Minimum real power</td><td>R</td></tr><tr><td>Load.MaxMW*</td><td>Maximum real power</td><td>R</td></tr><tr><td>Load.ReferenceMW*</td><td>Reference real power at one per unit (for scaling)</td><td>R</td></tr><tr><td>Load.MinMvar*</td><td>Minimum reactive power consumed</td><td>R</td></tr><tr><td>Load.MaxMvar*</td><td>Maximum reactive power</td><td>R</td></tr><tr><td>Load.ReferenceMvar*</td><td>Reference reactive power at one per unit (for scaling)</td><td>R</td></tr><tr><td>Load.Mvar</td><td>Magnitude of Load Mvar. Solved value</td><td>R</td></tr><tr><td>Load.Mw</td><td>Magnitude of Load MW. Solved value</td><td>R</td></tr></table>

Each field of each object type has a type: integer, text, real or date. We only consider text or real types. In some cases, two alternative types are permitted in the PSADD for certain fields. We do not allow this. Only a small subset of all available PSADD fields is used in this paper. Fields or data types mentioned but

Ž<sup>)</sup> not used are indicated with an asterisk . T denotes. Text string data, R denotes real data, I denotesŽ . integer data. The transformer and load data types have subtypes not described here.

The PSADD integrates two viewpoints: a bus-oriented viewpoint common to analytical studies, and an equipment-oriented viewpoint common to measured values and system operation. The miscellaneous application data describes this information. A subset of the miscellaneous application data is illustrated in Table 1.

Table 6  
Subset of Shunt element data table

<table><tr><td>Name</td><td>Description</td><td></td></tr><tr><td>Shunt.Number</td><td>Unique Number</td><td>I</td></tr><tr><td>Shunt.BusRef</td><td>Bus.Number to which shunt is connected</td><td>I</td></tr><tr><td>Shunt.Id</td><td>Identifier</td><td>I</td></tr><tr><td>Shunt.Status</td><td></td><td>I</td></tr><tr><td>Shunt.BaseMVA*</td><td>MVA of this device</td><td>R</td></tr><tr><td>Shunt.BasekV*</td><td>Base voltage of this device</td><td>R</td></tr><tr><td>Shunt.Type</td><td>Identifier of this device (Capacitor, Reactor)</td><td>T</td></tr><tr><td rowspan="3">Shunt.ControlMode</td><td>NONE = fixed shunt value</td><td>I</td></tr><tr><td>VOLT = hold voltage between limits</td><td></td></tr><tr><td>MVAR = hold MVAR flow *</td><td></td></tr><tr><td>Shunt.ControlBusRef</td><td>Bus.Number at which voltage is to be controlled</td><td>I</td></tr><tr><td>Shunt.MaxRegVoltage</td><td>Value at which shunt will change out to lower voltage</td><td>R</td></tr><tr><td>Shunt.MinRegVoltage</td><td>Value at which shunt will change out to raise voltage</td><td>R</td></tr><tr><td>Shunt.BlockSusceptValueNo</td><td>Number of discrete values available. Zero for continuous adjustment</td><td>I</td></tr><tr><td>Shunt.BlockSusceptance</td><td>Susceptance of each block A vector.</td><td>R</td></tr><tr><td>Shunt.MW</td><td>Magnitude of Shunt output MW. A solved value</td><td>R</td></tr><tr><td>Shunt.Mvar</td><td>Magnitude of Shunt output Mvar. A solved value</td><td>R</td></tr></table>

Table 7 Subset of transmission Line data table

<table><tr><td>Name</td><td>Definitions</td><td></td></tr><tr><td>Line.Number</td><td>Unique number</td><td>I</td></tr><tr><td>Line.FromBusRef</td><td>Bus.Number of “from” bus</td><td>I</td></tr><tr><td>Line.ToBusRef</td><td>Bus.Number of “to” bus</td><td>I</td></tr><tr><td>Line.Circuit</td><td>Alphanumeric circuit ID</td><td>T</td></tr><tr><td>Line.Status</td><td></td><td>I</td></tr><tr><td>Line.SectionR</td><td>Series resistance</td><td>R</td></tr><tr><td>Line.SectionX</td><td>Series reactance</td><td>R</td></tr><tr><td>Line.ShuntConductance</td><td>Total uniformly shunt conductance of this section</td><td>R</td></tr><tr><td>Line.ShuntSusceptance</td><td>Total shunt susceptance of this section</td><td>R</td></tr><tr><td>Line.FromMW</td><td>Line MW flow at From end. A solved value</td><td>R</td></tr><tr><td>Line.FromMvar</td><td>Line Mvar flow at From end. A solved value.</td><td>R</td></tr><tr><td>Line.ToMW</td><td>Line MW flow at To end. A solved value</td><td>R</td></tr><tr><td>Line.ToMvar</td><td>Line Mvar flow at To end. A solved value</td><td>R</td></tr><tr><td>Line.TypeId</td><td>Type of equipment type (LINE, CAPACITOR*)</td><td>T</td></tr><tr><td>Line.Length*</td><td>Length</td><td>R</td></tr><tr><td>Line.LossAssignBusRef</td><td>Bus.Number to which losses should be assigned</td><td>I</td></tr><tr><td>Line.FromLumpedCond</td><td>Conductance of lumped shunt element at “from” bus</td><td>R</td></tr><tr><td>Line.FromLumpedSuscept</td><td>Susceptance of lumped shunt element at “from” bus</td><td>R</td></tr><tr><td>Line.ToLumpedCond</td><td>Conductance of lumped shunt element at “to” bus</td><td>R</td></tr><tr><td>Line.ToLumpedSucept</td><td>Susceptance of lumped shunt element at “to” bus</td><td>R</td></tr><tr><td>Line.RateId</td><td>ID of line rating value. A vector of text strings</td><td>T</td></tr><tr><td>Line.RateValue</td><td>Rating value (a vector)</td><td>R</td></tr></table>

Four other tables of generic interest are those for analog data, status data, ratings data and set data. The set data is useful for grouping information into zones, areas, companies, locations and almost any other user-desired grouping. It is not used here. The ratings data specifies rating types. This paper assumes all flow ratings are in MVA, thus no such data is required. Status data is used to denote the status of a device or component. We use 1 to denote in service, active or closed, 0 otherwise. Thus, we do not need status data as a separate data type. Analog data is used to specify metered information as op- Ž posed to parameters of components . Rather than. entering this information as part of each device type, it is entered as analog data with a pointer to the device type where it is used. A subset of the definition of analog data is illustrated in Table 2, and Table 3 illustrates Bus Data.

The nodal injections types used in this paper include machine, load and shunt element, are defined in Tables 4–6, respectively.

Two series PSADD elements are implemented. These include the transmission line line elementŽ . and the transformer Xformer element. These areŽ . illustrated in Tables 7 and 8, respectively.

## 3. Rendition in Matlab

The implementation of the data dictionary in Matlab is done by means of sparse arrays, structures and cells of types real and character. For the sake of clarity, all concepts will be illustrated by means of an example. The example in question corresponds to the six-bus system from Wood and Wollenberg 2 . <sup>w</sup> <sup>x</sup> The common format file CFF can be created to Ž . describe this system. The CFF is not sufficient to describe all the necessary information. Thus, additional assumptions will be made as needed.

To implement the data dictionary, one needs to first establish the necessary structures for all the base

data types and the corresponding fields or attributesŽ . of each data type. Some data types such asŽ . Misc contain only scalar or simple text attributes. The complete definition for the Misc data type subset is:

Misc.Title='This is a sample case'; Misc.BaseMyA=100: MisC.ConnectivitxType=′BM': Misc.ContingencyGenMWResponse='PC'; Misc.DeviceRefMethod='Number'

Most other data types include vector or even sets of vectors as their data elements. The question arises immediately in Matlab whether it is better to represent these types as a single structure with vector structure entries, or to represent each data type entry as a structure and to represent the entire data type as a vector of structures. Either answer is correct and will work, but because of the vectorized nature of Matlab computations, our experiments indicate that it is quite efficient to represent data types as structures of vectors. Furthermore, for the sake all consistence almost all vectors will be column vectors. When it is necessary to represent sets actually vectors of vari-Ž . able-length vectors, this is done by using the notion of cells, which are vectors of arbitrary entry types. This is the convention adopted in the data dictionary.

Table 8  
Subset of Transformer data table

<table><tr><td>Name</td><td>Definition</td><td></td></tr><tr><td>Xformer.Number</td><td>Unique Number</td><td>I</td></tr><tr><td>Xformer.PrimaryBusRef</td><td>Bus.Number to which winding awinding A is connected</td><td>I</td></tr><tr><td>Xformer.SecondaryBusRef</td><td>Bus.Number to which winding B is connected</td><td>I</td></tr><tr><td>Xformer.Circuit</td><td>Identifier</td><td>T</td></tr><tr><td rowspan="4">Xformer.Type</td><td>FIXED Fix ratio and angle</td><td>T</td></tr><tr><td>VOLT Fix angle var ratio</td><td></td></tr><tr><td>MVAR Fix angle var ratio</td><td></td></tr><tr><td>MW — Fix ratio var angle</td><td></td></tr><tr><td>Xformer.TapRatio</td><td>Tap ratio value</td><td>R</td></tr><tr><td>Xformer.TapAngle</td><td>Tap angle value</td><td>R</td></tr><tr><td>Xformer.TapRatioMin</td><td>Minimum Tap ratio value of the transformer</td><td>R</td></tr><tr><td>Xformer.TapRatioMax</td><td>Maximum Tap ratio value of the transformer</td><td>R</td></tr><tr><td>Xformer.TapRatioStep</td><td>Tap ratio step size value of the transformer</td><td>R</td></tr><tr><td>Xformer.TapAngleMin</td><td>Minimum Tap angle value of the transformer</td><td>R</td></tr><tr><td>Xformer.TapAngleMax</td><td>Maximum Tap angle value of the transformer</td><td>R</td></tr><tr><td>Xformer.TapAngleStep</td><td>Tap angle step size value of the transformer</td><td>R</td></tr><tr><td>Xformer.Status</td><td></td><td>I</td></tr><tr><td>Xformer.BaseMVA</td><td>*</td><td>R</td></tr><tr><td>Xformer.FromMw</td><td>Mw flow From bus. Solved value</td><td>R</td></tr><tr><td>Xformer.FromMvar</td><td>Mvar flow From bus. Solved value</td><td>R</td></tr><tr><td>Xformer.ToMw</td><td>Mw flow To bus. Solved value</td><td>R</td></tr><tr><td>Xformer.ToMvar</td><td>Mvar flow To bus. Solved value</td><td>R</td></tr><tr><td>Xformer.LossAssignBusRef</td><td>Bus.Number to which losses should be assigned</td><td>I</td></tr><tr><td>Xformer.Pri-SecR</td><td>s.c. resistance winding A to B</td><td>R</td></tr><tr><td>Xformer.Pri-SecX</td><td>s.c. reactance winding A to B</td><td>R</td></tr><tr><td>Xformer.Pri-SecZeroR*</td><td>s.c. zero sequence resistance winding A to B</td><td>R</td></tr><tr><td>Xformer.Pri-SecZeroX*</td><td>s.c. zero sequence reactance winding A to B</td><td>R</td></tr></table>

Start with a definition of all buses along with, loads, machines and shunts connected to them.

```matlab
% Initialization of Bus Data Type
Bus.Number=[]; Bus.Name=''; Bus.BasekV=[]; Bus.Status=[];
Bus.Vmag=[]; Bus.Vangle=[]; Bus.MwMismatch=[]; Bus.MvarMismatch=[];
Bus.TypeCode=''; Bus.VoltTarget=[]; Bus.LowVoltLim=[]; Bus.UpVoltLim=[];
% Initialization of Machine Data Type
Machine.Number=[]; Machine.BusRef=[]; Machine.Id=''; Machine.Status=[]; Machine.Mw=[];
Machine.Mvar=[];
Machine.ControlMode=''; Machine.ControlledBusRef=[];
Machine.MinQOutput=[]; Machine.MaxQOutput=[];
Machine.MinOperatingVolt=[]; Machine.MaxOperatingVolt=[];
Machine.PostContRespFact=[];
% Initialization of Load Data Type
Load.Number=[]; Load.Id='';
Load.BusRef=[]; Load.Status=[]; Load.Mvar=[]; Load.Mw=[];
% Initialization of Shunt Data Type
Shunt.Number=[]; Shunt.BusRef=[]; Shunt.Id=''; Shunt.Status=[];
Shunt.Type=''; Shunt.ControlMode=[]; Shunt.ControlBusRef='';
Shunt.MaxRegVoltage=[];
Shunt.MinRegVoltage=[];
Shunt.BlockSusceptValueNo=[]; Shunt.BlockSusceptance=[];
Shunt.Mw=[]; Shunt.Mvar=[];
```

Likewise, all structures for lines can be initialized:

```javascript
Line.Number=[]; Line.FromBusRef=[]; Line.ToBusRef=[]; Line.Circuit='';
Line.Status=[];
Line.SectionR=[]; Line.SectionX=[];
Line.ShuntConductance=[]; Line.ShuntSusceptance=[];
Line.FromMw=[]; Line.FromMvar=[]; Line.ToMw=[]; Line.ToMvar=[];
Line.TypeId=''; Line.LossAssignBusRef=[];
Line.FromLumpedCond=[]; Line.FromLumpedSuscept=[];
Line.ToLumpedCond=[]; Line.ToLumpedSuscept=[];
Line.RateId=''; Line.RateValue=[];
```

Since no transformers are used in the example, details of transformers are not illustrated.

At this point, the table values can be loaded for the example at hand more or less directly from the Data Dictionary. Some assumptions are made.

v All machine minimum powers are 10% of the machine maximum powers.

v All machine maximum powers are 200 MW orŽ 2 pu ..

v We prefer to work in per-unit everywhere, even when the data dictionary calls for Mw or Mvar.

v Minimum voltages anywhere are specified at 0.85 pu, maximum voltages at 1.2 pu.

v All shunt susceptances are assumed to be adjustable in exactly two equal-sized steps. Since there are no susceptances in this example, a capacitive susceptance with a value of 0.02 pu is assumed at bus 5.

v Normally, data types would be constructed using a function that reads raw data from a database, from a common format data file, or some other available source. Here, data is constructed directly for the example at hand, without resorting to a reading and translation function.

```matlab
% Bus data specification
n=6;    Bus.Number=(1:n);
Bus.Name=strvcat('BUS1','BUS2',...
    'BUS3','BUS4','BUS5','BUS6');
Bus.BasekV=138*ones(n,1);    Bus.Status=ones(n,1);
Bus.Vmag=[1.05;1.05;1.07;1;1;1];    Bus.Vangle=zeros(n,1);
Bus.TypeCode=...
    strvcat('S','CT','CT','L','L','L');
Bus.VoltTarget=Bus.Vmag;
Bus.LowVoltLim=0.85*ones(n,1);    Bus.UpVoltLim=1.2*ones(n,1);

% Machine data specification
ng=3;    Machine.Number=(1:ng);
Machine.Id=strvcat(Machine.Id,'1','1','1');
Machine.Status=ones(ng,1);
Machine.ControlMode=strvcat('SW','PV','PV');
Machine.BusRef=[1;2;3];    Machine.ControlledBusRef=[1;2;3];
Machine.RatingId=...
    strvcat('NORMAL','NORMAL','NORMAL');
Machine.RatingValue=[1.5;1.5;1.5];    Machine.RatingMinimum=[0.15;0.15;0.15];
Machine.MinQOutput=[-0.25;-0.25;-0.25];    Machine.MaxQOutput=[0.75;0.75;0.75];
Machine.MinOperatingVolt=0.85*ones(ng,1);
Machine.MaxOperatingVolt=1.2*ones(ng,1);
Machine.PostContRespFact=[1;1;1];

% Load data specification
nl=3;    Load.Number=(1:3)';    Load.BusRef=[4;5;6];
Load.Id=strvcat('1','1','1');    Load.Status=[1;1;1];

% Shunt data specification
nsh=1;    Shunt.Number=[1];    Shunt.BusRef=5;    Shunt.Id='1';    Shunt.Status=1;
Shunt.Type='Capacitor';    Shunt.ControlMode='NONE';    Shunt.ControlBusRef=5;
Shunt.MaxRegVoltage=1.25*ones(nsh,1);    Shunt.MinRegVoltage=0.85*ones(nsh,1);
Shunt.BlockSusceptValueNo={2}; % CELL ARRAY
Shunt.BlockSusceptValue={{0.1,0.1}}; %"

% Line data specification
nL=11;    Line.Number=(1:nL)';
Line.FromBusRef=[1;1;1;2;2;2;2;3;3;4;5]; Line.ToBusRef=[2;4;5;3;4;5;6;5;6;5;2];
Line.Circuit=strvcat('1','1','1','1',...
    '1','1','1','1','1','1',...
Line.SectionR=[.1;.05;.008;.05;.05;.05;.07;.12;.02;.02;.1];
Line.SectionX=[.2;.2;.3;.25;.1;.3;.2;.26;.1;.4;.3];
Line.ShuntConductance=zeros(nL,1);
Line.ShuntSusceptance=[.02;.02;.03;.02;.01;.02;.025;.025;.01;.04;.03];
Line.TypeId=char(ones(nL,1)*double('Line')); Line.LossAssignBusRef=Line.FromBusRef;
Line.FromLumpedCond=zeros(nL,1);    Line.FromLumpedSuscept=zeros(nL,1);
Line.ToLumpedCond=zeros(nL,1);    Line.ToLumpedSuscept=zeros(nL,1);
ratid=strvcat('NORMAL','EMERG');    ratval=[1.5;2];
for k=1:nL,
    Line.RateId{k,1}=ratid;
    Line.RateValue{k,1}=ratval;
end
```

The specification of metered parameters for all data types is done by means of the analog data type.

We consider first the specification of data values for all loads, followed by the specification of all ma-

chines, all shunts, all lines and all transformers thisŽ example has no transformers . Ordinarily this would. also be accomplished by an input routine that would translate appropriate database entries, CFF information and<sup>r</sup>or other such available data into the data dictionary structures. Here, the data is specified directly for the example of interest, starting with an initialization of all analog data types:

```matlab
% Initialization of all Analog data
Analog.Number=[];    Analog.Type='';    Analog.AssignDevice='';
Analog.DeviceRef=[];    Analog.Value=[];
% Specification of all Load operating Analog data
for k=1:nl,
    na=length(Analog.Number);
    Analog.Number=[Analog.Number;na+1;na+2];
    Analog.Type=strvcat(Analog.Type,'MW','MVAR');
    Analog.AssignDevice=...
    strvcat(Analog.AssignDevice,'Load','Load');
    Analog.DeviceRef=[Analog.DeviceRef;k;k];
end
Analog.Value=[Analog.Value;0.7;0.7;...
    0.7;0.7;0.7;0.7];

% Specification of all Machine operating Analog data
for k=1:ng,
    na=length(Analog.Number);
    Analog.Number=[Analog.Number;na+1];
    Analog.Type=strvcat(Analog.Type,'MW');
    Analog.AssignDevice = ...
    strvcat(Analog.AssignDevice,'Machine');
end
Analog.DeviceRef=[Analog.DeviceRef;1;2;3];
Analog.Value=[Analog.Value;0;0.5;0.6];
```

## 4. A vanilla Newton power flow

The above structures can be used directly in the implementation of a basic Newton power flow. Convenient computation in Matlab requires a few additional ideas:

v Most data types used for computation should be complex. Thus, a few data types are added to the definition of the bus data type and other dataŽ types as needed ..

v An Internal data type is defined and used to contain all important intermediate matrix variables.

v An overall encapsulation of all data types into a single master data types is done to be able to refer to all the variables and data for a single study by means of a single variable. This is a structure of structures.

The first step is to convert pertinent data dictionary structures into Matlab structures suitable for computation. Also, it is extremely useful to associate any analog measurement data from the Analog data types and associate it with the pertinent data type in a manner suitable for computation. The following code performs these tasks and further encapsulates all information:

```matlab
j=sqrt(-1);
kPL=intersect(strmatch('Load', Analog.AssignDevice), strmatch('MW', Analog.Type));
kQL=intersect(strmatch('Load', Analog.AssignDevice), strmatch('MVAR', Analog.Type));
kPM=intersect(strmatch('Machine', Analog.AssignDevice), strmatch('MW', Analog.Type));
Bus.SL=zeros(n,1); Bus.PM=zeros(n,1);
iPL=Load.BusRef(Analog.DeviceRef(kPL));
iQL=Load.BusRef(Analog.DeviceRef(kQL));
iPM=Machine.BusRef(Analog.DeviceRef(kPM));
Bus.SL(iPL)=Bus.SL(iPL)+Analog.Value(kPL);
Bus.SL(iQL)=Bus.SL(iQL)+j*Analog.Value(kQL);
Bus.PM(iPM)=Bus.PM(iPM)+Analog.Value(kPM);
Line.Z=Line.SectionR+j*Line.SectionX;
Line.ShuntY2=(Line.ShuntConductance+j*Line.ShuntSusceptance)/2;
Line.YI=Line.FromLumpedCond+j*Line.FromLumpedSuscept;
Line.YJ=Line.ToLumpedCond+j*Line.ToLumpedSuscept;
% Shunt devices at bus not considered here
PQlist=strmatch('L', Bus.TypeCode);
PVList=strmatch('CT', Bus.TypeCode);
SlackList=strmatch('S', Bus.TypeCode);
GenList=union(SlackList, PVList);
NonSlack=union(PQlist, PVList);
```

Next we construct the Y-bus matrix:

```javascript
n=length(Bus.Number);
Ybus=sparse([], [], [], n, n);
Ybus=Ybus+sparse(Line.FromBusRef, Line.FromBusRef, 1./Line.Z+Line.ShuntY2, n, n);
Ybus=Ybus+sparse(Line.FromBusRef, Line.ToBusRef, -1./Line.Z, n, n);
Ybus=Ybus+sparse(Line.ToBusRef, Line.FromBusRef, -1./Line.Z, n, n);
Ybus=Ybus+sparse(Line.ToBusRef, Line.ToBusRef, 1./Line.Z+Line.ShuntY2, n, n);
Ybus=Ybus+sparse(Line.FromBusRef, Line.FromBusRef, Line.YI, n, n);
Ybus=Ybus+sparse(Line.ToBusRef, Line.ToBusRef, Line.YJ, n, n);
```

We then illustrate the code to construct the complete power flow Jacobian for any system Note: thisŽ highly vectorized version of the code is due to

Christopher DeMarco of the University of Wisconsin :.

```matlab
function [dSdd,dSdv]=pflowjac(Yb,Vb)
Ib=Yb*Vb;
dSdd=j*diag(conj(Ib).*Vb)-j*diag(Vb)*conj(Yb)*diag(conj(Vb));
dSdv=diag(conj(Ib).*(Vb./abs(Vb)))+diag(Vb)*conj(Yb)*diag(conj(Vb)./abs(Vb));
```

Finally, the complete master vanilla Newton solver is:

```matlab
Vmag=Bus.Vmag; Vang=Bus.Vangle*pi/180;
for iter=1:10,
    V=Vmag.*exp(j*Vang);
    [dSdd,dSdv]=pflowjac(Ybus,V);
    misvect=V.*conj(Ybus*V)+Bus.SL-Bus.PM;
    rmiss=[real(misvect(NonSlack));...
    imag(misvect(PQlist))];
    mismatch=max(abs(rmiss));
    if mismatch<0.0001, break; end
    rjac=[real(dSdd(NonSlack,NonSlack))...
    real(dSdv(NonSlack,PQlist));...
    imag(dSdd(PQlist,NonSlack))...
    imag(dSdv(PQlist,PQlist))];
    dx=rjac\rmiss;
    dxAng=dx(1:length(NonSlack));
    dxMag=dx(length(NonSlack)+1:length(dx));
    Vang(NonSlack)=Vang(NonSlack)-dxAng;
    Vmag(PQlist)=Vmag(PQlist)-dxMag;
end
Bus.Vmag=Vmag; Bus.Vangle=Vang*180/pi;
```

To run the example in this paper, cut and paste every Matlab code segment to a Matlab environment. Store function code segments in m-files.

Extrapolation of these techniques to considerably more complex cases and problems is immediate. We illustrate only one such extension.

## 5. Power Transfer Distribution Factors

As an example of the usefulness of this approach to practical power system computations, we illustrate the code to compute PTDF for an increase in active power demand at any location in the network, relative to the power being supplied at the slack generator. By having the PTDFs for any two or more Ž . locations in the grid, the PTDF for any bilateral orŽ multilateral transaction not involving the slack gen-. erator can also be readily found, although this is not done here. For the example above, the PTDF code requires the determination of a Jacobian matrix that relates the flows at either end of a line to changes in voltage magnitudes and angles. The vectorized code to construct such matrix for the flow at the from end of every line in the system is given next. Here Vb is the vector of complex nodal voltages and Vs refers to the sending end voltages of the lines of interest. Yf is either YflowI or YflowJ, the from or to end flow admittance matrices.

```matlab
function [YflowI, YflowJ] = bldyflow(Bus, Line)
n = length(Bus.Number); nb = length(Line.FromBusRef); nbe = (1:nb)';
YflowI = sparse(nbe, Line.FromBusRef, 1./Line.Z + i * Line.ShuntY2 + Line.YI, nb, n);
YflowI = YflowI + sparse(nbe, Line.ToBusRef, -1./Line.Z, nb, n);
YflowJ = sparse(nbe, Line.FromBusRef, -1./Line.Z, nb, n);
YflowJ = YflowJ + sparse(nbe, Line.ToBusRef, 1./Line.Z + i * Line.ShuntY2 + Line.YJ, nb, n);
```

```matlab
function [dFdd,dFdv]=flowjac(Yf,Line,Vb,Vs)
nb=length(Line.FromBusRef); n=length(Vb); If=Yflow*Vb;
dFdd=j*sparse((1:nb)',Line.FromBusRef,(conj(If).*Vs),nb,n)-j*diag(Vs)*conj(Yf)*diag(conj(Vb));
dFdv=sparse((1:nb)',Line.FromBusRef,(conj(If).*(Vs./abs(Vs))),nb,n)+diag(Vs)*conj(Yf)*diag(conj(Vb))./abs(Vb));
```

This code can be used to determine the sensitivity of flows on any line to any injections at a given operating point. Sample code to do this calculation for our example for an injection at bus 5 would be:

```matlab
[YflowI, YflowJ] = bldyflow(Bus, Line);
[dFdd, dFdv] = flowjac(YflowI, Line, V, V(Line.FromBusRef));
[dSdd, dSdv] = pflowjac(Ybus, V);
rJ = [real(dSdd(NonSlack, NonSlack)), real(dSdv(NonSlack, PQlist)); imag(dSdd(PQlist, NonSlack)), imag(dSdv(PQlist, PQlist))];
rJf = [real(dFdd(:, NonSlack)), real(dFdv(:, PQlist)); imag(dFdd(:, NonSlack)), imag(dFdv(:, PQlist))];
e = zeros(n, 1);    e(5) = 1;    er = [real(e(NonSlack)); imag(e(PQlist))];
dFP5 = rJf * (rJ\er)
```

At this point, the Matlab environment contains already a wealth of useful information for answering a large number of questions about the system.

ratus and Systems, Volume PAS-92, Number 6, pp 1916–1925, November<sup>r</sup>December.

<sup>w</sup> <sup>x</sup> 2 A. Wood, B.F. Wollenberg, Power generation, operation and control, 2nd edition, Wiley, 1996.

## 6. Conclusions

PSADD data types have been used as the basis for a direct implementation of a simple power flow in Matlab. The implementation is remarkably efficient and easy to extend to any desired additional purpose: new methods can be tested with ease, new functions and objectives implemented, all while maintaining the ability to communicate between and among diverse applications in a standardized manner.

## Acknowledgements

Professor Christopher DeMarco made available the key Jacobian routine to this author. Joann Staron has been for years instrumental in developing the PSADD. Thanks are also due to Scott Greene and Taiyou Yong.

<sup>w</sup> <sup>x</sup> 1 IEEE Committee Report, 1973. Common format for exchange of solved load flow data, IEEE Transactions on Power Appa-

## References

![](/api/attachments/EF8RNEQZ/fulltext/images/f8f79b8bdf2b3f808e1f961dc1dfadb3e383076d370e1ef8175c9d2d52df09e6.jpg)

Fernando L. Alvarado is a Professor of Electrical and Computer Engineering at the University of Wisconsin and a Senior Consultant at Christensen Associates. He earned a PhD in Electrical and Computer Engineering from the University of Michigan in 1972, a Masters from Clarkson University in 1969 and a PE and BEE degree from the National University of Engineering in Lima, Peru. He is a fellow of IEEE. He is a member of the IEEE Energy Policy Board. He

has hundreds of journal publications, articles, book chapters, reports and conference presentations. He is recognized for his work on the integration of economics and electric power networks. He has developed methods for efficient trading in power networks, including a method for hedging against price uncertainty with R. Rajaraman . He heads a CIGRE task force on Ž . ancillary services and an IEEE committee on risk management in security of power systems. He is a well-known software expert on large scale computation and sparse matrices.
