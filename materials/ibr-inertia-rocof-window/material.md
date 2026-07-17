<!-- image -->

Transactions

## Online Inertia Estimation for IBR Plants: Error Analysis and RoCoF Window Length Selection

Submission ID

4e0ec051-c67b-4f5f-9200-7064c244f37b

Submission Version

Initial Submission

PDF Generation

25 May 2026 08:11:42 EST by Atypon ReX

## Authors

Dr. Shihan Wang

Submitting Author

## [CRediT](https://credit.niso.org/)

Writing - original draft, Writing - review &amp; editing, Software, Data curation, Validation, Methodology, Visualization, Formal analysis

Prof. Liansong Xiong Corresponding Author

ORCiD

[https://orcid.org/0000-0002-1251-1006](https://orcid.org/0000-0002-1251-1006)

## [CRediT](https://credit.niso.org/)

Supervision, Project administration, Funding acquisition, Formal analysis

Dr. Lei Liu

<!-- image -->

[https://orcid.org/0000-0002-4642-8833](https://orcid.org/0000-0002-4642-8833)

## [CRediT](https://credit.niso.org/)

Software, Writing - review &amp; editing

Mr. Xupeng Wang

## [CRediT](https://credit.niso.org/)

Data curation, Visualization, Writing - review &amp; editing

## Affiliations

- State Key Laboratory of Electrical Insulation and Power Equipment, Xi'an Jiaotong University, Xi'an 710049, China

## Affiliations

- State Key Laboratory of Electrical Insulation and Power Equipment, Xi'an Jiaotong University, Xi'an 710049, China

## Affiliations

- State Key Laboratory of Electrical Insulation and Power Equipment, Xi'an Jiaotong University, Xi'an 710049, China

## Affiliations

- State Key Laboratory of Electrical Insulation and Power Equipment, Xi'an Jiaotong University, Xi'an 710049, China

<!-- image -->

## Additional Information

## Technical Topic Area

Transactions on Sustainable Energy / Grid interaction of sustainable energy sources Grid interaction of sustainable energy sources

Transactions on Sustainable Energy / Wind turbine generators

Wind turbine generators

## Keywords

Frequency control Frequency response Frequency stability Inverters Power system parameter estimation Power system stability

## Paper Classification

Research Paper (This type of paper presents mainly academic research results. They will be reviewed mainly by university researchers)

## Files for peer review

All files submitted by the author for peer review are listed below. Files that could not be converted to PDF are indicated; reviewers are able to access them online.

| Name                                                                                          | Type of File        | Size   | Page   |
|-----------------------------------------------------------------------------------------------|---------------------|--------|--------|
| Online Inertia Estimation for IBR Plants Error Analysis and RoCoF Window Length Selection.pdf | Main Document - PDF | 3.2 MB | Page 4 |

## Online Inertia Estimation for IBR Plants: Error Analysis and RoCoF Window Length Selection

Shihan Wang, Liansong Xiong, Senior Member, IEEE , Lei Liu, Graduate Student Member, IEEE , and Xupeng Wang

Abstract -Accurate online inertia estimation of inverter-based resource (IBR) plants is essential for evaluating frequency stability and guiding inertial resource allocation. However, existing inertia estimation methods based on the rate of change of frequency (RoCoF) primarily focus on system-level estimation, making it difficult to quantify single-plant inertia contributions; moreover, the error mechanisms induced by sampling noise and RoCoF calculation window length remain unclear. To address these challenges, this paper proposes an online inertia estimation method for IBR plants. A unified model is developed to characterize the frequency response (FR) of diverse IBR control types. Under a controllable active-power disturbance, the damping term is estimated from the steady-state response, and the inertia-response power is then decomposed from FR power for inertia estimation. An analytical error propagation model is further established to quantify the influence of sampling noise and RoCoF window length on estimation accuracy, providing a practical guideline for window selection. Experimental results on a full-power hardware platform demonstrate the accuracy of the proposed scheme and validate the effectiveness of the RoCoF window-length selection guideline.

Index Terms -IBR plants, online inertia estimation, RoCoF calculation, window length selection, error analysis.

## I. INTRODUCTION

O VER the past decade, the penetration of inverter-based resource (IBR) plants has continued to increase, while grid inertia has been declining [1]. Lower inertia leads to a higher rate of change of frequency (RoCoF) and more severe transient frequency deviations during disturbances, which may trigger protection actions and result in large-scale blackouts and cascading system collapse [2]. To mitigate these risks, organizations such as NERC, ENTSO-E, IRENA, and IEEE have established inertia support standards for IBR plants [3], [4], [5], [6]. Accurate inertia estimation is essential for compliance verification with these standards and for subsequent tasks including stability assessment [9], inertia responsibility partitioning [7], and dynamic resource allocation [8].

Existing inertia estimation methods can generally be categorized into passive observation methods and active disturbance methods. Among passive approaches, Gorbunov et al. [10] used phasor measurement unit (PMU) data to estimate oscillation modes and identify inertia and damping through modal approximation. Building on this, subsequent studies partitioned

Manuscript created May, 2026. This work was supported in part by the National Natural Science Foundation of China (52377196), in part by the Key Research and Development Program of Shaanxi (2024GX-YBXM517).(Corresponding author: Liansong Xiong.)

S. Wang, L. Xiong, L. Liu, and X. Wang are with State Key Laboratory of Electrical Insulation and Power Equipment, Xi'an Jiaotong University, Xi'an 710049, China (e-mail: shihanwang@stu.xjtu.edu.cn; xiongliansong@xjtu.edu.cn; leiliuxjtu@stu.xjtu.edu.cn; wxpeng@stu.xjtu.edu.cn).

systems based on the center of inertia and aggregated regional parameters to estimate the equivalent system inertia [11]. However, with the increasing integration of IBR plants, the effectiveness of such methods is increasingly constrained by the accuracy of the underlying equivalent models. To alleviate this limitation, studies have introduced hybrid approaches combining equivalent modeling with data-driven extraction [12], [13], alongside purely data-driven techniques such as federated learning [14] and extended subspace identification [15]. Although these methods reduce dependence on accurate physical models, they require substantial amounts of highquality training data to learn the mapping between frequency response (FR) characteristics and inertia.

More fundamentally, passive observation methods rely on naturally occurring FR data, where the response caused by disturbances is usually weak. Although measurement noise exists in all measured data, its relative influence is more pronounced in passive observation, leading to a lower signal-to-noise ratio (SNR). As recognized in [11], [12], this low SNR condition makes inertia estimation more susceptible to measurement uncertainty. To increase the SNR, active disturbance methods have been proposed. Fault-induced responses, event-driven responses such as generator tripping and load shedding, and HVDC switching have all been used to excite system dynamics for inertia estimation [16], [17], [18]. However, these methods inevitably disrupt the normal operation of power systems, thus limiting their practical applicability.

Despite the evolution from passive observation to active disturbance methods, two fundamental bottlenecks remain unresolved. First, most existing studies focus on regional or system-level assessment, failing to distinguish the inertia contribution of an individual IBR plant. Second, many existing methods inherently rely on frequency derivatives to establish the relationship between system dynamics and inertia, which amounts to calculating the RoCoF. In practice, RoCoF is obtained by finite-difference calculation, and its accuracy is strongly affected by both measurement noise and the differentiation window length [19], [20]. The ENTSO-E report on inertia and RoCoF further highlights that uncertainty in RoCoF calculation under noisy conditions remains one of the key challenges in frequency stability assessment [21].

The window length used for RoCoF calculation varies considerably across existing studies. The NERC report indicates that RoCoF is commonly estimated over short windows ranging from 0.1 s to 0.5 s, with 0.5 s often adopted in practical applications [5]. Brogan et al. [22] evaluated several window lengths, including 0.1 s, 0.25 s, and 0.5 s, whereas Zhang et al. [23] adopted a fixed 0.1 s window. Although these

1

studies recognize the importance of window length selection, the adopted values remain largely empirical. A rigorous theoretical basis for window length selection is still lacking, and the relationship between noise-induced estimation error and window length has not yet been systematically revealed or quantitatively characterized.

To address these issues, this paper proposes an online inertia estimation method for IBR plants and further analyzes the impact of noise-induced error on the estimation process. Specifically, a controllable step active power disturbance is applied at the point of common coupling (PCC) to excite the FR. By combining steady-state identification with response decomposition, the inertia and damping power components can be separated, thereby enabling quantitative estimation of plant inertia. Furthermore, the relationship among noise, RoCoF calculation window length, and estimation error is analyzed.

The main contributions of this paper are summarized as follows:

- 1) An FR-based power decomposition scheme is proposed for online inertia estimation of IBR plants. By estimating the damping contribution from the steady-state response, the damping- and inertia-related power components are separated, reducing the influence of steady-state deviations on inertia estimation.
- 2) The impact of sampling noise and window length on estimation error is analytically revealed. A window length of 250-300 ms is found to balance accuracy and stability under noisy conditions.
- 3) Experimental validation on a full-power hardware platform demonstrates the effectiveness of the proposed method. The damping required for power decomposition is accurately estimated, and the inertia estimation error remains within 5%.

The rest of this paper is organized as follows. Section II establishes the unified FR model for IBR plants. Building on this theoretical foundation, Section III details the proposed online inertia estimation method and its implementation workflow. The underlying error propagation mechanism is analytically explored in Section IV to provide theoretical guidance for window selection. Subsequently, Section V validates the proposed method through full-power hardware experiments. Finally, Section VI concludes this article.

## II. FR CHARACTERISTICS OF IBR PLANTS

## A. Unified FR Model for IBR Plants

Typically, IBR plants can be categorized into two main types: current-source (CS) type and voltage-source (VS) type, as illustrated in Fig. 1(a) and Fig. 1(b), respectively. For the CS-type plant, the grid frequency is measured by a phaselocked loop (PLL), and the active-power reference is adjusted through the control loop, which can be expressed as

<!-- formula-not-decoded -->

where H CS and D CS are the inertia and damping of the CS-type plant; ∆ f = f N -f denotes the frequency deviation, with f N and f being the nominal and actual frequencies, respectively; and P FR,CS denotes the FR power.

Fig. 1. Two typical control methods for IBR plants.

<!-- image -->

The VS-type plant regulates its internal frequency f and phase angle θ based on the deviation between the output power P e and the reference value P ref, which can be formulated as

<!-- formula-not-decoded -->

where H VS and D VS denote the inertia and damping of the VS-type plant.

Although the control implementations differ, (1) and (2) exhibit the same FR characteristics after per-unit normalization. Therefore, a unified FR model for IBR plants can be established as:

<!-- formula-not-decoded -->

where ∆ P ∗ FR and ∆ f ∗ denote the per-unit FR power and perunit frequency deviation, respectively; H and D are the inertia and damping of the IBR plant. For simplicity, the superscript ∗ is omitted hereafter, and all variables and parameters used in the estimation process are expressed in per-unit (p.u.).

## B. FR Composition and Parameter Decomposition

Following a step active power disturbance P dis at t dis , the frequency and ∆ P FR are shown in Fig. 2(a) and (b), respectively. As intuitively illustrated by the equivalence relationship in Fig. 2, ∆ P FR can be decoupled into two distinct components, as shown in Fig. 2(c) and (d). Specifically, they correspond to the damping power ∆ P D driven by the frequency deviation, and the inertia power ∆ P H governed by the RoCoF (denoted as r = d∆ f/ d t ). This physical decomposition is formulated as

<!-- formula-not-decoded -->

At steady state, the frequency deviation converges to ∆ f ∞ , while the RoCoF becomes zero. Therefore, the inertiaresponse power vanishes, i.e., ∆ P H = 0 , and (4) reduces to

<!-- formula-not-decoded -->

Accordingly, the damping coefficient can be obtained as

<!-- formula-not-decoded -->

t

3

Fig. 2. FR curves under a step disturbance: (a) frequency, (b) FR power, (c) damping power, (d) inertia power.

<!-- image -->

Once D is determined, the inertia can be calculated as

<!-- formula-not-decoded -->

The above derivation is based on ideal noiseless response curves, which clarify the physical meanings of the damping and inertia as well as their time-domain decoupling characteristics. In practice, however, RoCoF is estimated from discretely sampled frequency data. A standard finite-difference scheme is form as

<!-- formula-not-decoded -->

where T w denotes the window length for RoCoF calculation.

Numerical differentiation is highly susceptible to measurement noise, and the estimation error depends strongly on the length T w. As summarized in Table I, grid codes and interconnection standards across different countries recommend widely varying, empirical window lengths T w for RoCoF calculation [5], [6], [24], [25], underscoring the lack of a unified theoretical consensus.

Section IV further analyzes the noise propagation mechanism in RoCoF-based inertia estimation and provides rigorous theoretical guidance for T w selection.

TABLE I ROCOF MEASUREMENT WINDOW LENGTHS IN GRID CODES

| Country/Organization   | China   | U.S.    |   Europe | IEEE   |
|------------------------|---------|---------|----------|--------|
| Window length T w (ms) | 100-200 | 100-500 |      500 | > 100  |

## III. ONLINE INERTIA ESTIMATION

This section details the entire procedure of the proposed online inertia estimation method for IBR plants.

## A. Measurement Preprocessing and Noise Modeling

As illustrated in Fig. 3, the raw sampled frequency and power signals contain high-frequency fluctuations. To suppress high-frequency noise, a first-order low-pass filter (LPF) is applied:

<!-- formula-not-decoded -->

where τ ∈ [0 . 05 , 0 . 2] is the LPF time constant.

After LPF preprocessing, the actual filtered sequences (denoted by the 'Filtered' curves in Fig. 3) are modeled as theoretical responses superimposed with residual noise:

<!-- formula-not-decoded -->

Fig. 3. Measurement preprocessing for f and P FR under a step disturbance.

<!-- image -->

where t i = iT s is the i th sampling instant, with T s being the constant sampling interval; ˆ P and ˆ f are the actual filtered active power and frequency measurements, respectively; P and f are the theoretical ideal responses (corresponding to the 'Average' dashed lines in steady state); and n P and n f represent the noise terms after LPF.

The noise terms are assumed to be mutually independent, zero-mean random variables:

<!-- formula-not-decoded -->

where σ 2 P and σ 2 f are the noise variances of ˆ P and ˆ f , respectively.

## B. Steady-State Interval Detection and Power Decomposition

A sliding-window standard-deviation criterion is used to detect steady-state intervals from noisy measurements. For a window of length M , the signal is regarded as steady-state if

<!-- formula-not-decoded -->

where ¯ x is the mean value of the signal within the window, x i denotes the ˆ P FR ( t i ) or ˆ f ( t i ) at time t i . In this study, the steady-state detection threshold ε x is set to 1% of the predisturbance steady-state power and 0 . 03 Hz for the frequency signal.

Based on the detected segments, the steady-state variations of ∆ P FR and f are calculated as

<!-- formula-not-decoded -->

Fig. 4. Sliding-window linear fitting for RoCoF estimation.

<!-- image -->

where ¯ P pre FR and ¯ P post FR denote the mean active power before and after the disturbance, respectively; and ¯ f pre and ¯ f post are the corresponding mean frequencies.

According to (6), the damping estimate D m is obtained as

<!-- formula-not-decoded -->

Subsequently, the transient damping power ∆ P D is calculated from the measured frequency deviation:

<!-- formula-not-decoded -->

Finally, ∆ P H is obtained as

<!-- formula-not-decoded -->

## C. RoCoF and Inertia Estimation

As shown in Fig. 4, the RoCoF is estimated using a slidingwindow linear fitting method. Let T w denote the physical length of the RoCoF calculation window, which contains N discrete samples (i.e., T w = NT s ). For a fitting window centered at t c with N samples, the filtered frequency is approximated by a linear function with an intercept c :

<!-- formula-not-decoded -->

To simplify the derivation, the time axis is centered at t c as t i = t c + τ i , where τ i denotes the local time offset of the i th

4

sample within the window. Given the sampling period T s , τ i is given by

<!-- formula-not-decoded -->

which inherently satisfies ∑ N i =1 τ i = 0 .

Consequently, the least-squares estimate of RoCoF ˆ r at t c is obtained as

<!-- formula-not-decoded -->

To avoid the initial transient region around the RoCoF peak and the late stage dominated by noise, the effective inertia-estimation interval is selected according to the RoCoF magnitude. Let the peak magnitude of the RoCoF r p and its associated time t p be defined as

<!-- formula-not-decoded -->

The region immediately adjacent to r p is excluded to mitigate the estimation delay inherently introduced by the sliding window. Furthermore, as the dynamic response decays, the SNR drops severely, rendering continued estimation highly susceptible to noise amplification. To avoid these adverse regions, the effective computation interval is defined as Ω = [ t 0 . 8 , t 0 . 2 ] (as indicated by the red-shaded region in Fig. 5). These boundary instants correspond to the first instances after t p where the RoCoF magnitude decays to a specific proportion k of its peak:

<!-- formula-not-decoded -->

Finally, the pointwise inertia is evaluated within the valid interval Ω . To approximate the true equivalent inertia and reduce the impact of noise, the final estimate is obtained by averaging these pointwise results:

<!-- formula-not-decoded -->

where ¯ H is the final estimated inertia, and | Ω | denotes the total number of valid samples within the interval.

Fig. 5. Overall procedure of the proposed online inertia estimation method.

<!-- image -->

## D. Inertia Estimation Procedure

The schematic diagram of the power decomposition logic and the flowchart of the overall online inertia estimation procedure are integrated in Fig. 5, consisting of the following four main steps:

- 1) Signal preprocessing and damping estimation : The measured power and frequency under a step active-power disturbance are preprocessed using an LPF. The preand post-disturbance steady-state segments are extracted using (12), and D m is obtained from (13) and (14).
- 2) Power decomposition : Using D m, ∆ P D is calculated and subtracted from ∆ P FR to isolate ∆ P H, as expressed in (15) and (16).
- 3) RoCoF estimation and valid interval selection : The RoCoF estimate ˆ r is obtained using the least-squares fitting in (19), and the valid interval Ω = [ t 0 . 8 , t 0 . 2 ] is then determined according to (21).
- 4) Inertia estimation : The pointwise inertia estimates within Ω are averaged to yield the final inertia estimate ¯ H using (22).

## IV. ERROR ANALYSIS OF INERTIA ESTIMATION

According to the estimation principle in Section III, the inertia estimation error originates from the extracted inertia response power and the estimated RoCoF. This section analyzes the error propagation of the proposed method, with emphasis on the power component and the effect of RoCoF window length.

## A. Error Propagation Model

To simplify the notation, let P (representing ∆ P H) and r denote the theoretical inertia response power and RoCoF, respectively. Their estimates ˆ P and ˆ r are modeled as

<!-- formula-not-decoded -->

where δp and δr denote the corresponding estimation errors.

For each sample within the valid interval, the pointwise inertia estimate can be written as

<!-- formula-not-decoded -->

Expanding (24) and retaining terms up to the second order gives

<!-- formula-not-decoded -->

Since H = P/ (2 r ) , the pointwise inertia estimation error is

<!-- formula-not-decoded -->

Taking the expectation of (26), the mean difference can be written as

<!-- formula-not-decoded -->

Equation (27) separates the mean bias into terms involving the power-component error δp and terms associated with the RoCoF estimation error δr .

## B. Power Component Error Analysis

Taking the average over a detected steady-state segment and using the zero-mean noise assumption in (11) gives

<!-- formula-not-decoded -->

Thus, the steady-state variations used in (13) and the estimate D m do not introduce systematic bias in expectation.

During the transient stage, the calculated ∆ P D and ∆ P H remain affected by measurement noise through (15) and (16). However, because these equations are linear operations, the zero-mean property of the noise is preserved in the extracted inertia-response power. Therefore, the power-component error can be regarded as zero-mean in the averaging sense, and its correlation with the RoCoF estimation error is neglected:

<!-- formula-not-decoded -->

Substituting (29) into (27), the terms involving δp vanish:

<!-- formula-not-decoded -->

Equation (30) indicates that, after the power-component error is averaged out, the remaining mean bias is mainly governed by the mean and second moment of the RoCoF estimation error.

## C. RoCoF Error and Window Length Effect

Applying a Taylor series expansion to the frequency trajectory around t c yields

<!-- formula-not-decoded -->

where f ( k ) denotes the k th derivative of f ( t ) evaluated at t c . Substituting (31) into the least-squares estimator in (19), the RoCoF estimation error δr = ˆ r -f (1) can be decomposed into a model truncation bias and a noise component:

<!-- formula-not-decoded -->

In practice, the sliding window length T w is significantly larger than the sampling interval T s. Therefore, the number of samples satisfies N ≫ 1 , simplifying the truncation bias and noise variance to the asymptotic forms:

Fig. 6. Relative inertia estimation error versus T w under parameter variations.

<!-- image -->

<!-- formula-not-decoded -->

According to (32), the mean and second moment of the RoCoF estimation error are given by

<!-- formula-not-decoded -->

To characterize the expected estimation error, the relative error is defined as

<!-- formula-not-decoded -->

By substituting (33) and (34) into (30), and normalizing the expression with H = P/ (2 r ) and T w = NT s , (35) can be explicitly expressed as

<!-- formula-not-decoded -->

6

Eq. (36) reveals that the total estimation error is governed by two competing mechanisms. The bias term E b increases with T w, reflecting the model truncation error from linear approximation. Conversely, the noise term E n is inversely proportional to T 3 w , reflecting the noise suppression capability of the sliding window. As shown in Fig. 6, a smaller T w amplifies noise, whereas a larger T w increases the truncation bias. Therefore, the selection of T w involves a trade-off between noise suppression and model truncation error.

The optimal window length T ∗ w is obtained by setting dε/dT w = 0 . Since T w is typically in the sub-second range, the derivative term associated with T 4 w is negligible. This gives

<!-- formula-not-decoded -->

The fifth-root form in (37) indicates that T ∗ w is weakly sensitive to parameter variations. Consequently, the error curve exhibits a slowly varying, flat region near the optimal point (as illustrated in Fig. 6). In practice, this implies that strictly pursuing the exact mathematical optimum T ∗ w is unnecessary; selecting T w within the flat region is sufficient for robust and accurate estimation.

## V. EXPERIMENTAL VALIDATION

To accurately reproduce the external characteristics of an IBR plant and the power grid, experiments were conducted based on the system diagrams shown in Fig. 7. The main circuit parameters of the experimental setup are listed in Table II, and a photo of the setup is shown in Fig. 8. The setup includes two YXPHM-TP210b-I inverters, their corresponding DC sources, an oscilloscope, a resistive load, and an IT8617 AC/DC electronic load. The low-order system FR model is adopted for grid emulation, as it is widely used and accepted [1], [8], [26]. The corresponding control parameters are listed in Table III. Next, Fig. 9 shows the steady-state voltage and current waveforms of the two inverters operating at rated power without disturbance, where only phase-A components are given for simplicity.

Fig. 7. Structure of the experimental testing system.

<!-- image -->

Fig. 8. Photograph of the experimental platform.

<!-- image -->

Fig. 9. Voltage and current experimental waveforms of PCC.

<!-- image -->

TABLE II MAIN PARAMETERS OF THE EXPERIMENTAL PLATFORM

| Description                          | Plant emulator     | Grid emulator      |
|--------------------------------------|--------------------|--------------------|
| Rated active power                   | 2.85 kW            | 2.85 kW            |
| DC-link voltage                      | 650 V              | 650 V              |
| Filter inductance Filter capacitance | 5 mH, 0.1 mH 5 µ F | 5 mH, 0.1 mH 5 µ F |
| Rated phase                          | 220                |                    |
| voltage                              | V                  | rms                |
| Rated frequency                      | 50                 | Hz                 |
| Rated load                           |                    | 5.7 kW             |
| Switching frequency                  |                    | 10 kHz             |

TABLE III CONTROL PARAMETERS USED IN TESTS

| Part           | Description                                                 | Symbol                        | Value                              |
|----------------|-------------------------------------------------------------|-------------------------------|------------------------------------|
| Plant emulator | Inertia constant Damping coefficient Current-loop PI        | H D k P , k I                 | 2/4/6/8/10/12 s 3 5, 0.01          |
| Plant emulator | Mechanical power                                            | K m                           |                                    |
| Plant emulator | gain                                                        |                               | 1                                  |
| Grid emulator  | Reheater time constant Inertia constant Damping coefficient | F H T R H g D g V ref k P , k | 5 s 6 s 3 220 V rms 0.3, 0.01 0.01 |
| Grid emulator  | HP turbine power fraction                                   |                               | 0.5                                |
| Grid emulator  | Voltage reference                                           |                               |                                    |
| Grid emulator  | Voltage-loop PI                                             | I                             |                                    |
| Grid emulator  | Current-loop PI                                             | k P , k I                     | 5,                                 |
| Grid emulator  |                                                             |                               |                                    |
| Grid emulator  |                                                             |                               |                                    |
| Grid emulator  |                                                             |                               |                                    |

## A. Performance Under Various Inertia Levels

Considering that plant inertia varies due to diverse manufacturer factory settings, six inertia conditions ( H = 2 , 4 , 6 , 8 , 10 , 12 s) were evaluated to verify the reliability of the proposed method.

During steady-state operation, a step active power disturbance ( ∆ P dis = 0 . 05 p.u.) was introduced via the electronic load. The subsequent frequency and power signals were sam- pled and preprocessed in real time. Once the post-disturbance steady state was detected according to (12), the inertia estimation was executed. Fig. 10 illustrates the corresponding waveforms at the IBR plant side under varying H conditions.

<!-- image -->

Fig. 10. Plant frequency and active power waveforms under different inertia.

Fig. 11. Estimated damping and errors for different inertia.

<!-- image -->

Fig. 12. Relative inertia estimation error versus RoCoF window length for different inertia.

<!-- image -->

Since the inertia-response power is obtained by subtracting the damping component from the measured FR power, the damping coefficient must be identified before inertia estimation. In the experiment, the per-unit damping coefficient was set to D = 3 . The estimated damping coefficient D m was calculated from the detected steady-state segments using (12)(14), and the results are shown in Fig. 11. The estimation errors are around 1% , indicating that the damping component can be reliably separated.

8

Fig. 13. Real-time experimental estimation results under different inertia settings.

<!-- image -->

To verify the accuracy of the proposed analytical results, Fig. 12 shows the inertia estimation errors obtained by the proposed least-squares method with T w ranging from 50 to 550 ms. The results show that the inertia estimation error first decreases and then increases as T w increases. This validates the error analysis presented in this paper and indicates that inertia estimation methods involving RoCoF calculation generally exhibit a clear T w tradeoff. When T w is too short, the RoCoF calculation becomes more sensitive to measurement noise, leading to a larger estimation variance. By contrast, when T w is too long, the influence of higher order terms becomes more pronounced, thereby increasing the model truncation bias. More accurate inertia estimation results are consistently obtained within the T w ∈ [250 , 300] ms range, where most errors remain within 5% .

In addition, the experimental results show that T ∗ w increases with the inertia of the IBR plant under test. This is because the frequency variation of a high-inertia plant is slower, which allows a longer T w to improve noise immunity. In contrast, a low-inertia plant experiences faster frequency variation, which requires a shorter window to reduce dynamic mismatch, but also makes the estimation more sensitive to measurement noise.

To further highlight the advantages of the proposed method, verification was carried out at T w = 280 ms for H = 2 s , 4 s , 6 s , 8 s , 10 s , and 12 s . As shown in Figs. 13, all testing errors remain within 5% . These results provide strong evidence for the effectiveness and robustness of the proposed method.

It is worth noting that the inertia of the simulated grid in the experiments was H g = 6 s . When the inertia of the IBR plant gradually exceeded that of the grid, significant electromagnetic oscillations appeared, which affected the inertia estimation. Such oscillations were obvious within the effective estimation range. However, when the inertia of the IBR plant becomes excessively large, there is no need to worry about it violating grid-connection requirements. In this case, precise inertia estimation is no longer the primary concern for grid stability.

Fig. 14. Plant frequency and active power waveforms under different disturbance levels.

<!-- image -->

## B. Impact of Different Disturbance Levels

To verify the effectiveness of the proposed method under different disturbance amplitudes, four disturbance levels were tested: ∆ P dis = 0 . 03 , 0 . 05 , 0 . 07 , and 0 . 09 p.u., with H = 6 s .

After the system reached the steady state, step active power disturbances with different levels were applied. The corresponding plant-side frequency and active power responses are shown in Fig. 14. It can be observed that, as the disturbance level increases, the frequency nadir becomes deeper, the RoCoF peak becomes larger, and the inertia-related power response becomes more pronounced. This indicates that larger disturbances excite stronger system dynamics and provide a clearer FR for inertia estimation. Nevertheless, even under small disturbances, the variations in frequency and active power remain distinct,ensuring a sufficient SNR for reliable estimation.

Fig. 15. Estimated damping and errors under different disturbance levels.

<!-- image -->

Fig. 16. Relative inertia estimation error versus time-window length and disturbance level.

<!-- image -->

As in the previous tests, the decoupling of P D and P H is still indispensable for accurate inertia estimation. In these experiments, the per-unit damping coefficient was set to D = 3 . As illustrated in Fig. 15, the proposed method ensures highaccuracy damping measurement across different disturbance intensities, with the error remaining below 1% .

To systematically investigate the influence of disturbance level on inertia estimation accuracy, Fig. 16 presents the fitted surface of the relative inertia estimation error with respect to T w and disturbance level. Consistent with the inertia tests, the region of minimum estimation error remains stable within the 250 -300 ms range across all tested levels. Although smaller disturbances are slightly more susceptible to noise at very short windows, the estimation accuracy remains highly robust once T w is appropriately selected.

A closer examination further shows that, under relatively small disturbances, the inertia response power is weaker, making the estimation more susceptible to measurement noise, especially when short RoCoF windows are used. However, as the disturbance level increases, the error minimum consistently concentrates around 280 ms. This demonstrates that the proposed method does not rely on large disturbances. With a properly selected RoCoF window, reliable and accurate online inertia estimation can still be achieved under weak disturbance conditions.

For further validation, real-time estimation results obtained with T w = 280 ms are presented in Fig. 17. For all tested disturbance levels, the estimation errors remain within 1% . Compared with the results under different inertia settings, the variation caused by the disturbance level is significantly smaller. This suggests that, once the plant inertia is within

9

Fig. 17. Real-time experimental estimation results under different disturbance levels.

<!-- image -->

a moderate range, the disturbance level has only a limited effect on the steady-state estimation accuracy. Therefore, the proposed approach shows strong robustness and good engineering applicability for IBR plants operating under various disturbance conditions.

## VI. CONCLUSION

This paper proposes an online inertia estimation method for IBR plants and analyzes the effect of RoCoF window length on estimation error. The main conclusions are summarized as follows:

- 1) A complete and practical online inertia measurement scheme is proposed for IBR plants. By utilizing small power perturbations and terminal measurements, the scheme effectively separates the damping- and inertiarelated power components, without requiring internal control parameters of the plants.
- 2) An analytical error model is derived to describe the effect of RoCoF window length T w on inertia estimation. The results show a trade-off between noise suppression and model truncation error, indicating that T w = 250 -300 ms provides a suitable balance in the tested cases.
- 3) Hardware experiments under different inertia constants and disturbance levels verify the proposed method. The damping estimation error is approximately 1%, and the inertia estimation error remains within 5%.

## REFERENCES

- [1] L. Liu, L. Xiong, X. Luo, Q. Han, and L. Xiu, 'Derivative-free grid inertia estimation via frequency ramp test,' IEEE Trans. Power Electron. , vol. 41, no. 7, pp. 11726-11739, July 2026.
- [2] S. Dulal et al., 'Inertia estimation and trend analysis of the United States power grid interconnections,' IEEE Access , vol. 12, pp. 194436-194448, May 2024.
- [3] ENTSO-E, 'Ten-Year Network Development Plan 2020-The inertia challenge in Europe: Present and long-term perspective,' Insight Rep., Aug. 2021. [Online]. Available: https://eepublicdownloads.blob. core.windows.net/public-cdn-container/tyndp-documents/TYNDP2020/ FINAL/entso-e TYNDP2020 Insight Report Inertia 2108.pdf
- [4] International Renewable Energy Agency, 'Grid codes for renewable powered systems,' Apr. 2022. [Online]. Available: https://www.spr.pe/wp-content/uploads/2022/04/IRENA Grid Codes Renewable Systems 2022.pdf
- [5] NERC Inverter-Based Resource Performance Task Force, 'Fast frequency response concepts and BPS reliability needs,' White Paper, Mar. 2020. [Online]. Available: https://www.nerc.com/globalassets/our-work/reports/white-papers/ fast-frequency-response-concepts-and-bps-reliability-needs.pdf
- [6] IEEE Standard for Interconnection and Interoperability of InverterBased Resources (IBRs) Interconnecting with Associated Transmission Electric Power Systems , IEEE Std 2800-2022, 2022.
- [7] K. Li, H. Guo, X. Fang, S. Liu, F. Teng, and Q. Chen, 'Market mechanism design of inertia and primary frequency response with consideration of energy market,' IEEE Trans. Power Syst. , vol. 38, no. 6, pp. 5701-5713, Nov. 2023.
- [8] B. She, F. Li, H. Cui, J. Wang, Q. Zhang, and R. Bo, 'Virtual inertia scheduling (VIS) for real-time economic dispatch of IBR-penetrated power systems,' IEEE Trans. Sustain. Energy , vol. 15, no. 2, pp. 938951, Apr. 2024.
- [9] X. Wang, M. G. Taul, H. Wu, Y. Liao, F. Blaabjerg, and L. Harnefors, 'Grid-synchronization stability of converter-based resources-An overview,' IEEE Open J. Ind. Appl. , vol. 1, pp. 115-134, Aug. 2020.
- [10] A. Gorbunov, A. Dymarsky, and J. Bialek, 'Estimation of parameters of a dynamic generator model from modal PMU measurements,' IEEE Trans. Power Syst. , vol. 35, no. 1, pp. 53-62, Jan. 2020.
- [11] T. Kerdphol, M. Watanabe, R. Nishikawa, Y. Hayashi, and Y. Mitani, 'Inertia estimation of the 60 Hz Japanese power system from synchrophasor measurements,' IEEE Trans. Power Syst. , vol. 38, no. 1, pp. 753-766, Jan. 2023.
- [12] S.-H. Lee, J.-H. Liu, B.-Y. Chen, and C.-C. Chu, 'A two-stage datadriven method for estimating the system inertia utilizing event-driven PMU measurements,' IEEE Trans. Ind. Appl. , vol. 59, no. 5, pp. 52435256, Sept./Oct. 2023.
- [13] G. Ma, H. Wang, M. Xia, H. Bevrani, Z. Chen, and J. Yang, 'A cyberphysical framework for estimating inertia distribution in power systems,' Int. J. Electr. Power Energy Syst. , vol. 175, pp. 111578, Feb. 2026.
- [14] A. Poudyal, U. Tamrakar, R. D. Trevizan, R. Fourney, R. Tonkoski, and T. M. Hansen, 'Multiarea inertia estimation using convolutional neural networks and federated learning,' IEEE Syst. J. , vol. 16, no. 4, pp. 64016412, Dec. 2022.

10

- [15] P. Sharma, V. Ajjarapu, and U. Vaidya, 'Data-driven identification of nonlinear power system dynamics using output-only measurements,' IEEE Trans. Power Syst. , vol. 37, no. 5, pp. 3458-3468, Sept. 2022.
- [16] D. Yang et al., 'Data-driven estimation of inertia for multiarea interconnected power systems using dynamic mode decomposition,' IEEE Trans. Ind. Inform. , vol. 17, no. 4, pp. 2686-2695, Apr. 2021.
- [17] D. Gotti et al., 'Inertia estimation of a power system area based on iterative equation error system identification,' IEEE Trans. Power Syst. , vol. 39, no. 5, pp. 6469-6481, Sept. 2024.
- [18] R. J. Best, P. V. Brogan, and D. J. Morrow, 'Power system inertia estimation using HVDC power perturbations,' IEEE Trans. Power Syst. , vol. 36, no. 3, pp. 1890-1899, May 2021.
- [19] D. Macii, D. Fontanelli, G. Barchi, and D. Petri, 'Impact of acquisition wideband noise on synchrophasor measurements: A design perspective,' IEEE Trans. Instrum. Meas. , vol. 65, no. 10, pp. 2244-2253, Oct. 2016.
- [20] A. J. Roscoe, S. M. Blair, W. Dickerson, and G. Rietveld, 'Dealing with front-end white noise on differentiated measurements such as frequency and ROCOF in power systems,' IEEE Trans. Instrum. Meas. , vol. 67, no. 11, pp. 2579-2591, Nov. 2018.
- [21] ENTSO-E System Operations Committee, 'Inertia and RoCoFTechnical background and analysis,' SOC document, 2020. [Online]. Available: https://eepublicdownloads.entsoe.eu/clean-documents/SOC% 20documents/Inertia%20and%20RoCoF v17 clean.pdf
- [22] P. V. Brogan, R. J. Best, D. J. Morrow, K. McKinley, and M. L. Kubik, 'Effect of BESS response on frequency and RoCoF during underfrequency transients,' IEEE Trans. Power Syst. , vol. 34, no. 1, pp. 575-583, Jan. 2019.
- [23] C. Zhang, X. Dou, Z. Zhang, G. Lou, F. Yang, and G. Li, 'Inertiaenhanced distributed voltage and frequency control of low-inertia microgrids,' IEEE Trans. Power Syst. , vol. 36, no. 5, pp. 4270-4280, Sept. 2021.
- [24] Technical Requirements for Power System Inertia Support and Primary Frequency Control , DL/T 2669-2023, National Energy Administration of China, Oct. 11, 2023.
- [25] ENTSO-E, 'Rate of change of frequency (RoCoF) withstand capability: Implementation guidance document,' ENTSO-E AISBL, Brussels, Belgium, Jan. 31, 2018. [Online]. Available: https: //eepublicdownloads.entsoe.eu/clean-documents/Network%20codes% 20documents/NC%20RfG/IGD RoCoF withstand capability final.pdf
- [26] Z. Zhao et al., 'Generic low-order primary frequency response model for frequency nadir prediction,' IEEE Trans. Power Syst. , vol. 40, no. 6, pp. 5221-5236, Nov. 2025.