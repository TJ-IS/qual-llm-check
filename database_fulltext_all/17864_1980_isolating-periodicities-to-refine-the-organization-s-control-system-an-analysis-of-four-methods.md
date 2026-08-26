---
otero_id: 17864
otero_key: "FDVMBS64"
title: "Isolating periodicities to refine the organization's control system: an analysis of four methods"
authors: "Edward J. Lusk"
year: "1980"
journal: "Information & Management"
doi: "10.1016/0378-7206(80)90001-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Isolating Periodicities to Refine the Organization's Control System: an Analysis of Four Methods

Edward J. Lusk \*

Associate Professor Social Systems Sciences and Operations Research, The Wharton School, University of Pennsylvania, Social Systems Sciences Unit, Vance Hall CS, 3733 Spruce Street, Philadelphia, PA 19174, USA

Effective organizational control not only requires sophisticated monitoring systems but also depends upon the coordination of the various processes monitored. When important periodicities are inherent in these processes, knowledge of such periodicities aids in the development of simple models that generate useful monitoring information and facilitates the coordination of these processes. Failure to recognize important process periodicities often results in control information confounding which over time causes a deterioration of control system effectiveness.

In this paper, the author examines four methods which may be used to isolate process periodicities. Each method is specified, analyzed and illustrated. Two cases are provided and the four methods are compared on ten criteria which the manager may use to evaluate the methods. The discussion of the methods is intended to provide management with a general understanding of the nature of the methods as well as indicate the relative trade-offs inherent in their use.

Keywords: Isolating Periodicities, Control Systems Refinement, ARFIA Models, Spectral Methods, Periodogram, Fourier Transformation.

## 1. Introduction

Control, as one of the managerial imperatives, must be provided if the organization is to proceed systematically along an expansion path of its selection. An effective control system requires the analysis of performance deviations, specification of the problems and causes likely to have resulted in the set of the performance deviations observed, selection and implementation of a solution strategy, and evaluation of the implemented solution strategy. Each of these phases essentially depends on the meaning which managers may ascribe to the pattern and magnitude of performance deviations measured at any point during the production process. Therefore, to provide for adequate control, management must formulate relevant estimates of expected performance so that when problems exist, meaningful performance deviations will be measured. When there are important periodicities in processes monitored, the effect of these periodicities on the performance statistics used to develop performance contrasts must be estimated so that relevant control information is generated.

To illustrate some of the problems which may result when important periodicities are not recognized in developing performance expectations, consider the events surrounding the investigation of a budgeting system in a large teaching hospital [8]. In this case, management required investigation of significant monthly performance deviations. Due to the periodicities inherent in patient mix over the year, the activity of most departments exhibited significant periodicities. This variation in activity resulted in regular changes in the values of the performance statistics used by the controller in monitoring performance. However, rather than estimating the effects of these periodicities on the monthly cost statistics for the various departments, the controller used one-twelfth of budgeted departmental cost as the contrast against which costs actually incurred by the department would be judged. In this case failure to recognize inherent periodicities caused "favorable" cost variances during periods of relatively low activity and "unfavorable" cost variances during periods of relatively high activity. Departmental managers were dissatisfied with the control system. They maintained that often the observed variation was induced by erroneous parameterization which necessitated a substantial amount of paper work on their part. The hospital administration also was dissatisfied because they observed that often the induced variation was blamed for all variations even though some were real. As a consequence of the failure of the control system to provide creditable information, the generation of variance reports was given a low priority which resulted in monthly variance reports being delivered to departmental managers an average of six weeks after the end of the month. These circumstances were used by departmental managers to rationalize their indifference to the administration's control efforts.

![](/api/attachments/FDVMBS64/fulltext/images/4598e3b09fe54dcbd5994a253e1103f05fffc83d5bb2cab6ca265bce39c736e5.jpg)

Another aspect of the control function which is affected by important process periodicities is the coordination of the processes being monitored. When periodicities inherent in the processes monitored crate dysfunctional process interfaces, the potential and desire to control often are influenced adversely. For example, in one hospital significant periodicities in the cash flows were experienced during the year. Unfortunately, the cash inflows were not in phase with the cash outflows. This lack of coordination necessitated the frequent use of expensive short-term financing and was responsible for the hospital's failure to take advantage of time discounts available from vendors. In this situation, actions were not being taken to reduce the size of the vendor discounts lost because management felt that nothing could be done, i.e. the control environment or atmosphere did not foster actions to correct the dysfunction created by inherent periodicities in the cash flows. [10, Chapter 2]. After a change in top management, the economic effect of the cash flow problems was documented and used as an argument for increases in the frequency of remittances from third party payers. Considering the periodicity of the cash expenditures, a reimbursement frequency of two weeks was recommended by management. After considering the evidence presented by the hospital, Blue Cross and Medicare agreed to reimburse the hospital every two weeks. This enabled the hospital to correct the dysfunction and positively affected management's interest in providing control over the cash management function. These two simple examples illustrate the importance of isolating periodicities and using frequency information in monitoring and coordinating organizational processes.

The purpose of this paper is to examine four methods used to identify process periodicities which are reflected in sample data. The discussion of the technical aspects of each method will be presented in terms which will enable the non-technical manager to (1) comprehend the operational requirements of each method, and (2) communicate with technical personnel regarding method selection and implementation. To facilitate this development, each method will be illustrated with a simple example and two cases will be presented. The first case illustrates the use of a particular technique which generated information used to develop a simple forecasting model. The second case, provides a comparison between the four methods regarding the evaluation of a patient admission process. The paper concludes with a comparison of the four methods on ten criteria.

## 2. Methods of isolating periodicities

Four principal methods may be used to isolate periodicities of constant duration, as reflected in a set of time series observations samples from a stationary process. Three of these methods are statistical. The other method is mathematical in nature and will be considered after the statistical methods are examined.

## 2.1. Statistical methods useful in isolating periodicities

The three methods of statistical analysis often employed to isolate periodicities are (1) developing an autoregressive integrated moving average (ARIMA) model from the sampled data and inferring the periodicities from the form of the model, (2) computing the periodogram of the time series and (3) computing the spectrum of the time series. Consider now the general nature of these three methods.

## 2.2. ARIMA modeling

The development of ARIMA models to represent the time series of observations is accomplished in three stages: model specification, estimation of model parameters, and criticism of the model [2,5].

In the model specification phase, the autocorrelation and partial-autocorrelation function of the observed time series $\{z_{t}\}$ are analyzed to gain insights for selecting a model which is likely to underlie the generation of the data. The reason for analyzing the autocorrelation function $^{1}$ is that, in general, the solution to the difference equation represented by the autocorrelation function has the same form as the solution of the difference equation of the model underlying the data. For example, assume the observed time series is generated by a first order auto-regressive process represented by the following difference equation:

$$
z _ {t} = \phi z _ {t - 1} + a _ {t},\tag{1}
$$

where $a_{t}$ is a random disturbance usually assumed to have a zero mean and constant variance. Equation (1) indicates that the current value observed consists of $\phi$ times the value observed one time period in the past, plus some random disturbance. The autocorrelation function which would result in equation (1) were used to generate a time series of infinite length would be:

$$
\rho_ {k} = \phi \rho_ {k - 1},\tag{2}
$$

where $\rho_{k}$ represents the theoretical autocorrelation function at lag $k$ . Therefore, assuming $|\phi| < 1$ , the theoretical autocorrelation function of equation (1) would be a damped exponential. In this case, the solution of the difference equation of the observed time series (ignoring the random distribuance $a_{t}$ ) is identical to the solution of the difference equation of the autocorrelation function. Therefore, if one does not know the model generating the data, but only has an observed time series $\{z_{t}\}$ , computing the autocorrelation of $\{z_{t}\}$ often provides profound insights regarding the form of the model responsible for generating $\{z_{t}\}$ . For example, if the sample autocorrelation function of a set of time series observations is $r_{k} = -0.8r_{k-1}$ , then a logical choice for the model responsible for generating the observed time series is: $z_{t} = -0.8z_{t-1} + a_{t}$ .

Once the model form has been specified, the parameters of the specified model are estimated using least squares methods. For example, assume the ARIMA model initially specified is $z_{t} = -0.8z_{t-1} + a_{t}$ . Given the set of time series observations $\{z_{t}\}, z_{t} = -0.8z_{t-1} + a_{t}$ would be fitted to $\{z_{t}\}$ allowing the parameter $\Phi = -0.8$ to vary so the sum of the squared deviations between the actual and estimated $z_{t}$ is minimized. The value of $\phi$ which results, noted as $\dot{\phi}$ , is referred to as the least squares estimate of $\phi$ which may be shown to approximate the maximum likelihood estimate [2, Chapter 7].

To ascertain if the estimated model is an adequate representation of the model responsible for generating the observed time series, $\{z_{t}\}$ , the residual series, which is the difference between the estimated values of $z_{t}$ and the actual time series values, is generated. If the model is adequate, the residual series should not exhibit any structure and thus the autocorrelation function of the residual series should be that of a random process. In this case, no structural changes in the model are justified given the set of observations. Finally, if the model conforms to the physical realities of the situation, then the model may be analyzed to isolate inherent periodicities of the process generating $\{z_{t}\}$ . Two cases are prevalent in practice. In the first case, the period of the process is regular, i.e. the interval of time between periods is constant. The ARIMA models used to represent such processes are referred to as seasonal models. The other case encountered in practice is that of stochastic periodicity, i.e., variation is associated with the duration of the period as well as the interval of time between periods.

When a time series has an important seasonal component, the autocorrelation function will have significant values at the period and all the integer multiples of the period. For example, the autocorrelation function for a time series of daily patient admissions taken over the year had significant values at the following lags: $k = 7, 14, 21, 28, \dots, 7m$ , where $m \leqslant 12$ . Clearly, this process exhibits a weekly period. However, to ascertain objectively if the only seasonality is 7, the difference between every observation and the seventh ensuing observation is computed. This is referred to as taking a seasonal difference and is noted as $\nabla^s$ , where: $s$ is the seasonality. In this case $s = 7$ . If there was only a weekly period, then the seasonally differenced time series noted as $\nabla^7 z_t$ would have a theoretical autocorrelation function with no significant values since all of the structure would have been explained by the seasonal difference. In the case of daily patient admissions this is exactly what was observed. The autocorrelation function of $\nabla^7 z_t$ does not exhibit any significant values; therefore the only periodicity inherent in the patient admission process is weekly.

If the period of the process is stochastic, then this periodic behavior will be represented best with a second order autoregressive model which allows for the stochastic nature of the periodicity. For example, assume the observed time series is used to develop the following ARIMA model:

$$
z _ {t} = + 0. 9 z _ {t - 1} - 0. 8 z _ {t - 2} + a _ {t}.\tag{3}
$$

In equation (3), the current value observed is composed of 90 percent of the previous value, less 80 percent of the value which was observed two periods previously, plus a random disturbance. Equation (3) may be written as

$$
(1 - 0. 9 B + 0. 8 B ^ {2}) z _ {t} = a _ {t},\tag{4}
$$

where $B$ represent a backshift operation so that $Bz_{t} = z_{t - 1}$ and $B^{2}z_{t} = z_{t - 2}$ .

In most cases, if a periodicity is inherent in the process from which the sample was selected, the roots of the polynomial of equation (4) will be complex. $^{2}$ These complex roots may be represented in exponential forms as $\lambda \exp[\pm\theta i]$ and the period of the process may be computed as $2\pi/\theta$ [4]. For example, the roots of the ARIMA model represented by equation (4) are $0.5625 \pm 0.9662i$ . These complex roots may be represented in exponential form as:

## 1.12 exp[±1.045i]

$$
\begin{array}{l} \text { where } \lambda = [ (0. 5 6 2 5) ^ {2} + (0. 9 6 6 2) ^ {2} ] ^ {1 / 2}, \\ \text { and } \theta = \cos^ {- 1} [ 0. 5 6 2 5 / 1. 1 2 ]. \end{array}
$$

Given $\theta = 1.045$ , the period of the process is $2\pi/1.045 \approx 6$ . In this case, the autocorrelation function of the residuals, $\hat{a}_{t}$ , is a random series which indicates that the only periodicity is the one represented by the polynomial $(1 - 0.9B + 0.8B^{2})$ .

In summary, the ARIMA approach to ascertaining periodicities inherent in the process generating the observed data requires use of the observed time series to develop an ARIMA model. The ARIMA model is analyzed to infer the period as reflected in the observed time series.

## 2.3. The periodogram

The ARIMA models are representations in the time domain, i.e. they are explicit functions of time. The periodicity inferred from the form of the ARIMA model is the period of time during which unique motion is observed. For an observed time series of finite length, the number of these time periods over which unique motion is observed defines a frequency. For example, assume that an observed time series is represented in Figure 1.

$^{2}$ When the roots of the second order difference equation are real and at at least one of them is negative the period of the oscillations may be inferred from the period of time between an up-and-down-crossing of the mean. This is illustrated in Table 1. The second order ARIMA equation has the following roots $\lambda_{1}=3.3$ and $\lambda_{2}=-1.5$ . The theoretical autocorrelation of $1-3.7B-0.2B^{2}$ at lag 1 is $\rho_{1}=0.47$ and the time between oscillations is $\pi/\cos^{-1}(0.47)=2.9$ which represents the minor period.

![](/api/attachments/FDVMBS64/fulltext/images/17e556322b45406ec63086f07c91002978d209ab2f88df2a65a196722540cbfb.jpg)  
Fig. 1. Periodic pattern.

In this case, there is one unique pattern which repeats 3 times. The frequency then is 3 patterns in 30 units of time or a frequency of 1/10, i.e. every unit of time 1/10 of the pattern is observed or in 10 units of time one pattern is observed. This illustrates the following fundamental relationship which exist between frequency and period:

## Period = 1/Frequency

If the frequency can be observed, the period can be simply ascertained since the period is the inverse of the frequency. For this reason, if the observed time series can be represented by a function in the frequency domain (rather than the time domain), those frequencies which are important will indicate the likely periodicities as reflected in the observed time series.

The relationship between frequency and period suggests an important constraint in analyzing sample data to isolate periodicities. The shortest period which can be detected using discrete data is a period of 2 since the frequency cannot be greater than every other sample point. Therefore, if weekly data is collected, the shortest period which could be isolated is a bi-weekly cycle. Management must be aware that the sample plan places a limit on the analysis regarding the shortest period which can be detected. Therefore, management must develop a sampling plan recognizing the types of problems likely to occur and the inherent periodicities generated by those problems if the sampled data is to provide relevant control information.

Assuming an adequate sampling plan, one method of isolating important frequencies is to compute the periodogram of the data. The periodogram is computed from the following Fourier series representation of the observed data set $\{z_{t}\}$ :

$$
z _ {t} = \alpha_ {0} + \sum_ {i = 1} ^ {h} \left[ \alpha_ {i} \cos (2 \pi t i / N) + \beta_ {i} \sin (2 \pi t i / N) \right] + a _ {t},\tag{5}
$$

where N represents the size of the sample, $i,N$ represents the ith harmonic of the fundamental frequency 1/N, and h = N/2 - 1 if N is odd and $r_{2} = N/2$ if N is even because the shortest period which can be measured is 2.

Equation (5) may be fitted statistically to the observed time series $\{z_t\}$ and the least squares estimates of the coefficients $\alpha_0$ and $(\alpha_i, \beta_i)$ derived. Note these statistical estimates as $a_0$ and $(a_i, b_i)$ respectively. When the coefficients associated with the $j$ the frequency $(a_j, b_j)$ are large, an important frequency is likely to be in the neighborhood of $j/N$ .

For example, consider the following eight observations (1.98, 3.04, 4.11, 3.01, 2.06, 0.99, 01, 1.03) and assume that the observed time series $\{z_i\}_{32}$ consists of 4 repetitions of the same eight observations, i.e. the unique pattern of eight observations repeated four times. By plotting these 32 observations it may be ascertained that there are 4 cycles in the 32 observations or a frequency of $4/32 = 1/8$ . The Fourier series coefficients $(a_i, b_i)$ of this time series are:

$$
\begin{array}{l} (a (i / 3 2), b (i / 3 2)) = 0 \\ \text { for } i = 1, 2, 3, 5, 6, 7, 8, 9, 1 0, 1 1, 1 3, 1 4, 1 5, 1 6 \\ \text { and } \end{array}
$$

$$
\begin{array}{l} (a (4 / 3 2), b (4 / 3 2)) = (- 1. 2 2, 1. 2 2) \text { and } \\ (a (1 2 / 3 2), b (1 2 / 3 2)) = (0. 2 6, 0. 2 0) \end{array}
$$

This indicates that an important frequency exists in the neighborhood of 4/32 which supports the facts as they are known. Further, there seems to be a frequency in the neighborhood of 12/32. However, the magnitudes of $a(12/32)$ and $b(12/32)$ are less than $a(4/32)$ and $b(4/32)$ . This raises an important question. Could $a(12/32)$ and $b(12/32)$ occur by chance, i.e. when the only periodicity is 8? This is a statistical question, the answer to which depends upon the distribution of $a_{t}$ in equation (5). If $a_{t}$ is normally distributed with mean zero and variance $\sigma^2$ , then the magnitude:

$$
\mathrm{P} (i \mid N) = \frac {N}{2} \left(a _ {i} ^ {2} + b _ {i} ^ {2}\right)\tag{6}
$$

may be compared to $\sigma^{2}X_{(2)}^{2}$ , where $X_{(2)}^{2}$ represents a chi-square distribution with two degrees of freedom, to ascertain the approximate statistical significance of the Fourier coefficients at frequency $i|N$ . In the case presented previously, the only periodogram value which is statistically significant, $\alpha \leqslant 0.01$ , is P(4/32).

The other periodogram value P(12/32) is not statistically significant at a reasonable level of confidence i.e. the probability that $a(12/32)$ and $b(12/32)$ reflect a process periodicity is relatively low.

## 2.4. The spectrum

The periodogram estimates are computed only at frequencies which are harmonics of the fundamental frequency $1/N$ , i.e., the computed frequencies are integer multiples of $1/N$ . If the number of observations constituting the sample is not an integer multiple of the actual periodocities reflected in the data, then the various harmonics measured using the periodogram will not correspond exactly to the actual frequencies reflected in the sample data. However, when $N$ is not an integer multiple of a particular frequency reflected in the sample, the coefficients in the neighborhood of the actual frequency will have large values. This distortion results because the magnitudes of the Fourier series values are distributed over frequencies in the neighborhood of the actual frequency [3]. One way to compensate for this, is to allow the frequency at which the periodogram estimates are computed to be a continuous variable in the interval $[0, 1/2]$ . These continuous frequency estimates are referred to as the sample spectrum. However, there are also problems with the frequency estimates derived with the sample spectrum which relate to the stochastic nature of the amplitudes, frequencies and phases of sinusoidal components exhibited by most stationary time series. Therefore, rather than use the actual data values to transform $\{z_t\}$ from the time to the frequency domain, the autocorrelation function of the data is used to compute the spectrum of the time series. Since the theoretical autocorrelation function is an even function (i.e., $\rho(k) = \rho(-k)$ ), the theoretical spectrum is the cosine transformation of the theoretical autocorrelation function.

To develop the spectral density function, which indicates the distribution of sample variance over frequency for a time series of finite length, $\rho_{k}$ must be estimated. Unfortunately, the usual estimator of $\rho_{k}$ , $r_{k}$ , the sample autocorrelation function, has statistical properties associated with it which confound the information regarding the distribution of variance over frequency. $^{3}$ However, by truncating or attenuating various values of the sample autocorrelation function (a procedure known as windowing), the spectral estimates can be smoothed and useful information can be developed regarding the isolation of important periodicities. Windowing results in relative attenuation of the autocorrelation values developed at substantial lags. Windowing is important because the reliability of the autocorrelation values developed when the number of lags exceeds one-forth the sample size diminishes dramatically compared to the reliability of autocorrelation values developed for $k \leq N/4$ . Thus, windowing attempts to use only the most reliable information available from the autocorrelation function.

In summary, to develop the spectral density function the following three parameters must be established:

(1) What spectral window is to be used, i.e., how is the sample autocorrelation function to be attenuated,

(2) How many lags (k) are used to compute the sample autocorrelation function, (sometimes called window closing), and

(3) How many points of the spectrum are to be computed and plotted.

For example, assume that the spectral density function is to be computed for $\{z_t\}_{32}$ using the Tukey-Hanning spectral window. Assume that the spectral density function is computed using $k = 3$ , and $k = 8$ . Further, when $k = 3$ , six frequencies are computed and plotted and when $k = 8$ , 30 frequencies are computed and plotted. The spectral density functions developed under these two conditions are represented in Figure 2.

As can be seen, Figure 2-B gives a more accurate picture of the frequency structure of $\{z_{t}\}_{32}$ than the spectral estimates represented in Figure 2-A. This is to be expected since more information from the correlation function ( $k = 8$ opposed to $k = 3$ ) was used in developing Figure B and more points of the spectrum are computed and plotted.

## Mathematical analysis

The three methods discussed previously are statistical in nature. There is, however, a mathematical procedure which closely parallels the periodogram, referred to as the Fourier transformation of the data. The Fourier transformation of an observed time series $\{z_{t}\}$ , noted as FT[ $\{z_{t}\}$ ], is computed as:

![](/api/attachments/FDVMBS64/fulltext/images/031ff20e024d7a15b6daddb2d1f73d96d19e5051a8aea4c00f0f4951980f7549.jpg)

![](/api/attachments/FDVMBS64/fulltext/images/104d6647acdada1702f9d7b47b64bdd55d2af5158fef1957bdb89c22dbfb121c.jpg)  
Fig. 2. Spectral density functions.

$$
\begin{array}{l} \mathrm{FT} [ z _ {t} ] \equiv Z (n / N T) = 2 / P N \left[ \sum_ {k = 0} ^ {N - 1} \left\{z _ {k} \right\} \cos (2 \pi \omega) \right. \\ \left. - \mathrm{i} \sum_ {k = 0} ^ {N - 1} \left\{z _ {k} \right\} \sin (2 \pi \omega) \right], \end{array}\tag{7}
$$

where $N$ represents the size of the sample, $T$ represents the sample interval (usually assumed to equal one), $n$ is an index $(n=0,1,-\infty, N/2-1)$ , $i=(-1)^{1/2}$ , $\omega=nk/N$ , and $P=2$ when $n=0$ ; when $n>0$ , $P=1$ . Like the periodogram, equation (7) has $N/2-1$ different components $N/2-2$ of which represent a particular harmonic of the fundamental fre quency 1/NT. Equation (7) takes observations made in the time domain and represents them as a function in the frequency domain. Each of the N/2-1 components is used to compute the Fourier series' cosine and sine coefficients each of which correspond to a particular frequency. The results of the Fourier transformation applied to the set of observations $\{z_t\}$ are most simply arranged as in Table 1. The larger the magnitude of the cosine component or the sine component, the more important the corresponding Fourier series equation is in representing the observed data series. Since a unique period is associated with each of the N/2-1 components, the relative magnitudes of the cosine and sine component indicate which periods are demonstratably important respecting the data sampled [7].

Table 1

<table><tr><td>Frequency</td><td>Period</td><td colspan="2">Fourier Coefficients</td></tr><tr><td></td><td></td><td>Cosine</td><td>Sine</td></tr><tr><td>0</td><td>...</td><td> $\overline{z}$ </td><td>-</td></tr><tr><td>1/NT</td><td>NT</td><td> $a_{1}$ </td><td> $b_{1}$ </td></tr><tr><td>2/NT</td><td>NT/2</td><td> $a_{2}$ </td><td> $b_{2}$ </td></tr><tr><td>.</td><td>.</td><td>.</td><td>.</td></tr><tr><td>.</td><td>.</td><td>.</td><td>.</td></tr><tr><td>.</td><td>.</td><td>.</td><td>.</td></tr><tr><td>(N/2-1)/NT</td><td>(NT)/(N/2-1)</td><td> $a_{N/2-1}$ </td><td> $b_{N/2-1}$ </td></tr></table>

For example, Table 2 shows the Fourier transformation of $\{z_{t}\}_{32}$ where all other frequencies have cosine and sine coefficients which were less than |0.1|. In this case, the equation

Table 2

<table><tr><td rowspan="2">Frequency</td><td colspan="3">Fourier Coefficients(In excess of |0.1|)</td></tr><tr><td>Period</td><td>Cosine</td><td>Sine</td></tr><tr><td> $f_0 = \text{mean of } \{z_t\}_{32}$ </td><td>-</td><td>2.04</td><td>-</td></tr><tr><td> $f_4 = 4/32$ </td><td>8</td><td>+0.004</td><td>-1.72</td></tr><tr><td> $f_{12} = 12/32$ </td><td>2.7</td><td>-0.04</td><td>0.32</td></tr></table>

$$
\begin{array}{l} Z (4 / 3 2) = \frac {2}{N} \left[ \sum_ {k = 0} ^ {3 1} \left\{z _ {k} \right\} \cos (2 \pi k / 8) \right. \\ \left. - \mathrm{i} \sum_ {k = 0} ^ {3 1} \left\{z _ {k} \right\} \sin (2 \pi k / 8) \right] \end{array}
$$

develops cosine and sine coefficients which are materially larger than the coefficients associated with the other frequencies. This means that the Fourier series equation: $z_{t}=2.04+0.004\cos(2\pi t/8)-1.72\sin(2\pi t/8)$ , which has a period of 8, has more explanatory power or fits the sampled time series better than any other single equation which may be developed from the cosine and sine coefficients generated from FT[ $\{z_{i}\}_{32}$ ].

In this case, the actual frequency, $f_{a}$ , of the process generating the data was equal to one of the harmonics. Specifically, the first harmonic, 2/NT, happens to equal $f_{a}$ . In practice this rarely occurs and as in the case of the periodogram, unless the number of sample points is an integer multiple of the actual period of the process, the Fourier transformation will not precisely isolate the actual frequencies constituting $\{z_{t}\}$ . However, when these distortions occur, those frequencies close to the actual frequency will have large coefficient values. By evaluating clusters of frequencies which have relatively large coefficients, the analyst may infer that the interval represented by adjacent frequencies contains the actual frequency.

The principal difference between the periodogram [equation (5)] and the direct Fourier transformation is that no statistical inferences can be made from the coefficient information generated by the mathematical relationships represented in equation (7). Periodogram estimates, on the other hand, are formed from the least squares estimates of the coefficients of equation (5) which has an explicit error term, $a_{t}$ , as one of its arguments. Recall this error term permits statistical inferences.

Historically, the Fourier transformation of the observed time series was constrained technologically because, as the number of observations exceeds 256, the computational effort required to derive the coefficients of the Fourier series increases exponentially. However, with the advent of the Fast Fourier Transformation [3] the computational constraint effectively has been removed so the coefficient information developed using equation (7) is feasible for even large numbers of observations.

## 3. Case examples

In order to illustrate the use of these techniques in isolating process periodicities, two cases will be examined.

In the first case, the administrator of a large urban teaching hospital was interested in developing a forecasting model of daily patient admissions. As the first step in the model building process, the periodicities inherent in the daily patient admission process were measured. The technique used was spectral analysis because a spectral analysis computer program was supported by the hospital. Three years of daily patient admissions were analyzed. The analysis indicated a statistically significant frequency peak in the area of 0.143 cycles per day reflecting a period of 1/0.143 approximately equal to 7 days. Also, a second statistically significant peak was discerned in the area of 0.003 indicative of a yearly cycle. Based upon this information, the following simple forecasting model was formulated:

$$
\text { Current   Daily   Forecast } = \beta \times \frac {\text { Daily   Patient   Admission }}{\text { Previous   Year }}
$$

where $\beta$ represents the ratio of total patient admissions expected to total patient admissions of the previous year.

The forecasts developed using this simple model had a standard error less than the forecasts developed using an ARIMA model or a Centered Moving Average model.

In this case, periodicity information facilitated the development of a simple forecasting model which compared favorably to more sophisticated modelling approaches. This model was used to schedule hospital resources and formulate monitoring information.

The second case involved the evaluation of a hospital patient admission process. As part of the evaluation process, the administration wished to know if there were any changes in the pattern of admissions over the last year. Previously the administration had believed, without any substantial analysis, that there was only a weekly admission's cycle. To evaluate this question, daily patient admissions data for the past year were collected. In the original study the FFT was used to detect inherent periodicities; however to provide a basis of comparison, results for all four methods are reported in Table 3.

Table 3
Analyses of Hospital Daily Admissions $\{z_{t}\}$ 365.

<table><tr><td colspan="3"></td><td>Period</td><td>CPU time</td></tr><tr><td colspan="5">ARIMA</td></tr><tr><td colspan="5">- Model Developed (1-.37B-.2B2)∇7zt=(1-.95B7)at±.07 ±.07 ±.01</td></tr><tr><td colspan="5">- Standard Errors of the Parameters</td></tr><tr><td></td><td colspan="2">Box-Pierce Statistic: 23.4Indicates x2significanceof the model at (.25-.1)</td><td>73</td><td>0:5.69</td></tr><tr><td colspan="5">Periodogram</td></tr><tr><td colspan="5">Frequencies which have periodogram estimates which are statistically significant (α&lt;.01)</td></tr><tr><td>Frequency</td><td colspan="2">Periodogram Estimate</td><td></td><td></td></tr><tr><td>.1428</td><td colspan="2">104,375</td><td>7.0</td><td></td></tr><tr><td>.2849</td><td colspan="2">12,987</td><td>3.51</td><td>0:11.10</td></tr><tr><td colspan="5">Spectral Estimates (Tukey-Hanning Window)-30 lags used</td></tr><tr><td colspan="5">-10 Frequencies Plotted</td></tr><tr><td colspan="5">Spectral Estimates which are statistically significant (α&lt;.01):</td></tr><tr><td></td><td colspan="2">Spectral Estimate</td><td></td><td></td></tr><tr><td>Frequency .15</td><td colspan="2">661.1</td><td>6.67</td><td>0:7.20</td></tr><tr><td>Frequency .30</td><td colspan="2">84.2</td><td>3.33</td><td></td></tr><tr><td colspan="5">FFT of [zt]365</td></tr><tr><td colspan="5">Coefficients which account for at 30 percent of the variation of the data:</td></tr><tr><td>Frequency</td><td>Cos</td><td>Sin</td><td></td><td></td></tr><tr><td>.1425781</td><td>-10.1</td><td>14.1</td><td>7.0</td><td></td></tr><tr><td>.2851563</td><td>5.9</td><td>2.7</td><td>3.51</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>0:0.11</td></tr></table>

\*CPU Time measured in seconds on Dec 10

In this case, it is clear that there are two periods. The period of seven is the dominant periodicity as anticipated. However, there is an important minor cycle approximately one-half of the major cycle. This minor cycle was investigated and it was ascertained that admissions for the first 48–72 hours and the second 48–72 hours of the week were cyclical, e.g., if a large number of patients were admitted during the first 48–72 hours then not many were admitted during the second 48–72 hours. The administration could not explain for this behavior but began to investigate possible causes to ascertain if actions could be taken to eliminate the minor cycle and smotth out the admission pattern.

## Summary

In the author's experience with developing control information from time series data, the four methods examined in this paper have proven useful in isolating the periodicities reflected in observed time series. However, the utility of these techniques varies, depending upon the nature of the problem, computational resources available, and the degree of statistical verifiably desired. To facilitate consideration of these issues Table 4 has been provided.

Table 4
Generalized Comparisons of Methods

<table><tr><td>CRITERIA</td><td>ARIMA</td><td>PERIODOGRAM</td><td>SPECTRAL ESTIMATION</td><td>FFT</td></tr><tr><td colspan="5">Location of Single Periodicity</td></tr><tr><td>Fixed</td><td>Good</td><td>Good</td><td>Good</td><td>Good</td></tr><tr><td>Stochastic</td><td>Good</td><td>Fair</td><td>Good</td><td>Fair</td></tr><tr><td colspan="5">Location of Multiple Periodicities:</td></tr><tr><td>Fixed</td><td>Fair</td><td>Good</td><td>Good</td><td>Good</td></tr><tr><td>Stochastic</td><td>Fair</td><td>Fair</td><td>Good</td><td>Fair</td></tr><tr><td>StatislncExpertise Required to Develop Appropriate Information</td><td>Advanced Statistical Training Required</td><td>None</td><td>Advanced Statistical Training Required</td><td>None</td></tr><tr><td>Statistical Expertise Required To Interpret the Information Developed by the Method</td><td>Advanced Statistical Training Required</td><td>Elementary Statistical Training Required</td><td>Advanced Statistical Training Required</td><td>Elementary Mathematical Training Required</td></tr><tr><td>Time Required to Complete an Analysis Given Computer Supported Interactive Programs</td><td>Minimum: 30-45 min. Average: 1 hour Maximum: 3-4 hours</td><td>Minimum: 5-10 min. Average: 15 min. Maximum: 20-30 min.</td><td>Minimum: 30-45 min. Average: 1 hour Maximum: 2-3 hours</td><td>Minimum: 5-10 min. Average: 15 min. Maximum: 20-30 min.</td></tr><tr><td>Cost of Installing and Preparing the Interactive Programs for Users</td><td>Minimum: $15,000 Average: 30,000 Maximum: 50,000</td><td>Nominal (less than $500.)</td><td>Minimum: $2,000 Average: 3,000 Maximum: 5,000</td><td>Nominal (less than $500)</td></tr><tr><td>Cost of Obtaining the Programs Necessary to Perform the Analysis</td><td>Commercially: $50-$100</td><td>Generally not Commercially Available. Programming is Very Simple However</td><td>Commercially: $35-$100</td><td>Commercially: $35-$100</td></tr><tr><td>CRITERIA</td><td>ARIMA</td><td>PERIODOGRAM</td><td>SPECTRAL ESTIMATION</td><td>FFT</td></tr><tr><td>Basis of Ascertaining Important Frequencies Among all the Frequencies Reported</td><td>Statistical and Goodness of Fit</td><td>Statistical Evaluation of Periodogram and Estimates and Goodness of Fit</td><td>Statistical Evaluation of the Area Around Delineated Frequency Peaks</td><td>Goodness of Fit</td></tr><tr><td>Relative CPU Time Required (DEC 10) Compared to the FFT</td><td>Substantially Greater. On Average 50 x to 100x Greater.</td><td>Same If The Number of Observations is less than 256. Increases as the Number of Observations exceeds 256.</td><td>Moderately Greater. On Average 10x - 20x Greater</td><td>BASIS</td></tr><tr><td>Relative Amount of data required to isolate Periodicity Compared to an ARIMA Analysis</td><td>BASIS</td><td>Less. Often About 1/2 of the DATA is necessary</td><td>SAME</td><td>Less. Often About 1/2 of the DATA is necessary.</td></tr><tr><td rowspan="2">Reference Texts Advanced: Introductory: Discussion of Practical Experiences:</td><td>Box and Jenkins(1976) Pinckyck and Rubinfeld Chapters 13-17 (1976)</td><td>Jenkins and Watts(1968) Bloomfield (1976)</td><td>Jenkins and Watts(1968) Chow (1975)</td><td>Brigham (1976) Bloomfield (1976)</td></tr><tr><td>Jenkins (1979)</td><td>Bloomfield (1976)</td><td>Chow (1975)</td><td>Bloomfield (1976)</td></tr></table>

## References

[1] P. Bloomfield, Fourier Analysis of Time Series: An Introduction, (John Wiley and Sons, 1976).

[2] G.E.P. Box, G.M. Jenkins, Time Series Analysis: Forecasting and Control, (Holden Day 1976).

[3] E.O. Brigham, The Fast Fourier Transformer, (Prentice-Hall, 1975).

[4] G. Chow, Analysis and Control of Dynamic Economic Systems, (John Wiley, 1975).

[5] G.M. Jenkins, Practical Experiences with Modeling and Forecasting Time Series, (GJP Publication 1979.)

[6] G.M. Jenkins, and D. Watts, Spectral Analysis and Its Applications, (Holden Day, 1968).

[7] E.J. Lusk, A Reduction of Variance Method of Evaluating Fourier Series Coefficients, Working Paper, Wharton School, 1979.

[8] E.J. Lusk and J.G. Lusk, Financial and Managerial Control: A Health Care Perspective, (Aspen Systems 1979).

[9] R.S. Pindyck and D.L. Rubinfeld, Econometric Models and Economic Forecasts, (McGraw-Hill 1976).

[10] O.E. Williamson, Markets and Hierarchies: Analysis and Antitrust Implications, (Free Press, 1975).
