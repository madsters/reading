<!-- SOURCE-RECONCILED against arXiv:2105.07769 (F. Milano, Complex Frequency):
     \wp -> j (imaginary unit); \bar{a} -> \bar{\imath} (current). See flags.md. -->

<!-- image -->

## Modelling, Control, Stability Analysis and Simulation of Low-Inertia Power Systems

New Concepts for New Power Systems: Complex Frequency, Local Synchronization and Transient Slack Capability

Federico Milano

University College Dublin

PSCC 2026 Tutorial

<!-- image -->

<!-- image -->

## Table of Contents

- 1 Motivations
- 2 Complex Frequency
- 3 Local Synchronization
- 4 Transient Slack Capability (TSC)
- 5 Application: Dual-GFM
- 6 References

<!-- image -->

<!-- image -->

<!-- image -->

Modelling, Control, Stability Analysis and Simulation of Low-Inertia Power Systems

Federico Milano

Motivations

Complex Frequency

Local Synchronization

Transient Slack Capability (TSC)

Application: Dual-GFM

References

## Research Questions

## Complex Frequency

Converter introduce new modelling, control and stability challenges. Do we need new concepts to address these challenges?

## Local Synchronization

What is the link between synchronization and stability from the grid point of view?

## Transient Slack Capability

What features should a device have to be capable of sustaining the grid after a large disturbance?

## Beyond Synchronous Machines

Is the synchronous machine the 'best' possible way to generate power?

<!-- image -->

Modelling, Control, Stability Analysis and Simulation of Low-Inertia Power Systems

## Table of Contents

- 1 Motivations
- 2 Complex Frequency
- 3 Local Synchronization
- 4 Transient Slack Capability (TSC)
- 5 Application: Dual-GFM
- 6 References

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Frequency and Power Variations

This section defines the link between complex power and complex frequency in ac power systems.

<!-- image -->

<!-- image -->

## Frequency and Power Variations

This section defines the link between complex power and complex frequency in ac power systems.

Let us consider the power injection at network buses:

$$\bar { s } ( t ) = p ( t ) + j q ( t ) = \bar { v } ( t ) \circ \bar { \imath } ^ { * } ( t ) \, ,$$

<!-- image -->

<!-- image -->

## Frequency and Power Variations

This section defines the link between complex power and complex frequency in ac power systems.

Let us consider the power injection at network buses:

$$\bar { s } ( t ) = p ( t ) + j q ( t ) = \bar { v } ( t ) \circ \bar { \imath } ^ { * } ( t ) \, ,$$

where voltages and currents are Park's vectors (or analytic signals), i.e., are valid in transient conditions:

$$\bar { v } ( t ) = v _ { d } ( t ) + \jmath v _ { q } ( t ) \, .$$

<!-- image -->

<!-- image -->

## Complex Frequency

Let us rewrite the Park vector of the voltage in polar coordinates:

$$\bar { v } = v \, e ^ { j \theta } = e ^ { ( u + j \theta ) }$$

<!-- image -->

where u = ln( v ).

<!-- image -->

## Complex Frequency

Let us rewrite the Park vector of the voltage in polar coordinates:

$$\bar { v } = v \, e ^ { j \theta } = e ^ { ( u + j \theta ) }$$

where u = ln( v ).

Then, the complex frequency is defined as follows:

$$\bar { \eta } = \frac { d } { d t } ( u + j \theta ) = u ^ { \prime } + j \theta ^ { \prime } = \rho + j \omega \, ,$$

<!-- image -->

<!-- image -->

## Complex Frequency

Let us rewrite the Park vector of the voltage in polar coordinates:

$$\bar { v } = v \, e ^ { j \theta } = e ^ { ( u + j \theta ) }$$

where u = ln( v ).

Then, the complex frequency is defined as follows:

$$\bar { \eta } = \frac { d } { d t } ( u + j \theta ) = u ^ { \prime } + j \theta ^ { \prime } = \rho + j \omega \, ,$$

<!-- image -->

<!-- image -->

## Complex Frequency

Let us rewrite the Park vector of the voltage in polar coordinates:

$$\bar { v } = v \, e ^ { j \theta } = e ^ { ( u + j \theta ) }$$

where u = ln( v ).

Then, the complex frequency is defined as follows:

$$\bar { \eta } = \frac { d } { d t } ( u + j \theta ) = u ^ { \prime } + j \theta ^ { \prime } = \rho + j \omega \, ,$$

It is possible to show that the complex frequency is a special case of geometric frequency .

<!-- image -->

<!-- image -->

## Assumption

Let us assume that transmission line dynamics are fast, hence:

$$\bar { \imath } ( t ) & \approx \bar { Y } \, \bar { v } ( t ) \, , \\ \\ \iota _ { 1 } ( t ) & \approx \dot { \bar { Y } } \, \bar { v } ( t ) \, ,$$

where ¯ Y is the conventional admittance matrix of the grid.

<!-- image -->

<!-- image -->

## Assumption

Let us assume that transmission line dynamics are fast, hence:

$$\bar { \imath } ( t ) & \approx \bar { Y } \, \bar { v } ( t ) \, , \\ \\ \iota _ { 1 } ( t ) & \approx \dot { \bar { Y } } \, \bar { v } ( t ) \, ,$$

where ¯ Y is the conventional admittance matrix of the grid.

Hence the power injections into the grid nodes can be rewritten as:

$$\bar { s } ( t ) = \bar { v } ( t ) \circ [ \bar { Y } \, \bar { v } ( t ) ] ^ { * } \, .$$

<!-- image -->

<!-- image -->

## Link of the Complex Frequency with the Current

From the previous definition, the following identity holds:

$$\bar { v } ^ { \prime } = \frac { d } { d t } \bar { v } = \bar { v } \circ \bar { \eta } .$$

<!-- image -->

<!-- image -->

## Link of the Complex Frequency with the Current

From the previous definition, the following identity holds:

$$\bar { v } ^ { \prime } = \frac { d } { d t } \bar { v } = \bar { v } \circ \bar { \eta } .$$

Then, from ¯ ı ≈ ¯ Y ¯ v , one obtains:

$$\bar { i } ^ { \prime } = \bar { Y } \, \bar { v } ^ { \prime } = \bar { Y } \left ( \bar { v } \circ \bar { \eta } \right ) = \bar { Y } \, d i a g ( \bar { v } ) \, \bar { \eta } = \bar { I } \, \bar { \eta } \, .$$

<!-- image -->

<!-- image -->

## Link of the Complex Frequency with the Complex Power

Then taking the conjugate and multiplying by the voltage

$$\bar { v } \circ \bar { \imath } ^ { \prime * } = \bar { S } \bar { \eta } ^ { * } \, .$$

<!-- image -->

<!-- image -->

## Link of the Complex Frequency with the Complex Power

Then taking the conjugate and multiplying by the voltage

$$\bar { v } \circ \bar { \imath } ^ { \prime * } = \bar { S } \bar { \eta } ^ { * } \, .$$

Where ¯ S is a matrix whose elements are the complex power flow in the branches of the grid.

<!-- image -->

<!-- image -->

## Rate of Change of Power (RoCoP) [grid side]

## And finally, we note that:

$$\bar { s } ^ { \prime } & = \frac { d } { d t } ( \bar { v } \circ \bar { i } ^ { * } ) \\ & = \bar { v } ^ { \prime } \circ \bar { i } ^ { * } + \bar { v } \circ \bar { i } ^ { \prime * } \\ & = \bar { v } \circ \bar { \eta } \circ \bar { i } ^ { * } + \bar { v } \circ \bar { i } ^ { \prime * } \\ & = \bar { s } \circ \bar { \eta } + \bar { v } \circ \bar { i } ^ { \prime * }$$

<!-- image -->

<!-- image -->

## Rate of Change of Power (RoCoP) [grid side]

And finally, we note that:

$$\bar { s } ^ { \prime } & = \frac { d } { d t } ( \bar { v } \circ \bar { i } ^ { * } ) \\ & = \bar { v } ^ { \prime } \circ \bar { i } ^ { * } + \bar { v } \circ \bar { i } ^ { \prime * } \\ & = \bar { v } \circ \bar { \eta } \circ \bar { i } ^ { * } + \bar { v } \circ \bar { i } ^ { \prime * } \\ & = \bar { s } \circ \bar { \eta } + \bar { v } \circ \bar { i } ^ { \prime * } \\$$

So we obtain the expression:

$$\bar { s } ^ { \prime } - \bar { s } \circ \bar { \eta } = \bar { S } \bar { \eta } ^ { * }$$

<!-- image -->

$$- \bar { s } \circ i$$

<!-- image -->

## Rate of Change of Power (RoCoP) [grid side]

And finally, we note that:

$$\bar { s } ^ { \prime } & = \frac { d } { d t } ( \bar { v } \circ \bar { i } ^ { * } ) \\ & = \bar { v } ^ { \prime } \circ \bar { i } ^ { * } + \bar { v } \circ \bar { i } ^ { \prime * } \\ & = \bar { v } \circ \bar { \eta } \circ \bar { i } ^ { * } + \bar { v } \circ \bar { i } ^ { \prime * } \\ & = \bar { s } \circ \bar { \eta } + \bar { v } \circ \bar { i } ^ { \prime * } \\$$

So we obtain the expression:

$$\bar { s } ^ { \prime } - \bar { s } \circ \bar { \eta } = \bar { S } \bar { \eta } ^ { * }$$

$$- \bar { s } \circ i$$

We need now an expression for ¯ s ′ from the device side . . .

<!-- image -->

<!-- image -->

## System Model

Let consider the conventional DAE model for transient stability analysis:

$$z ^ { \prime } & = f ( z , y ) \\ 0 & = g ( z , y )$$

<!-- image -->

<!-- image -->

## System Model

Let consider the conventional DAE model for transient stability analysis:

$$z ^ { \prime } & = f ( z , y ) \\ 0 & = g ( z , y )$$

Under usual assumptions, we can write:

$$y ^ { \prime } & = \frac { \partial \phi } { \partial z } \, z ^ { \prime } = \left ( \frac { \partial g } { \partial y } \right ) ^ { - 1 } \frac { \partial g } { \partial z } \, z ^ { \prime } \\ & = \left ( \frac { \partial g } { \partial y } \right ) ^ { - 1 } \frac { \partial g } { \partial z } \, f ( z , \phi ( z ) ) \, .$$

<!-- image -->

<!-- image -->

## Rate of Change of Power (RoCoP) [device side]

In the conventional DAE model of power systems, voltages and powers are algebraic variables.

<!-- image -->

<!-- image -->

## Rate of Change of Power (RoCoP) [device side]

In the conventional DAE model of power systems, voltages and powers are algebraic variables.

Let assume we can write the expression of the power injections of each device connected to the grid as:

$$\bar { s } ^ { \prime } = \bar { s } ^ { \prime } ( \bar { v } , z , y )$$

Then, the time derivatives of ¯ s ′ can be written as:

$$\bar { s } ^ { \prime } = \frac { \partial \bar { s } } { \partial \bar { v } } \, \bar { v } ^ { \prime } + \left [ \frac { \partial \bar { s } } { \partial z } + \frac { \partial \bar { s } } { \partial y } \left ( \frac { \partial g } { \partial y } \right ) ^ { - 1 } \frac { \partial g } { \partial z } \right ] \, z ^ { \prime }$$

<!-- image -->

<!-- image -->

## Rate of Change of Power (RoCoP) [device side]

In the conventional DAE model of power systems, voltages and powers are algebraic variables.

Let assume we can write the expression of the power injections of each device connected to the grid as:

$$\bar { s } ^ { \prime } = \bar { s } ^ { \prime } ( \bar { v } , z , y )$$

Then, the time derivatives of ¯ s ′ can be written as:

$$\bar { s } ^ { \prime } = \frac { \partial \bar { s } } { \partial \bar { v } } \, \bar { v } ^ { \prime } + \left [ \frac { \partial \bar { s } } { \partial z } + \frac { \partial \bar { s } } { \partial y } \left ( \frac { \partial g } { \partial y } \right ) ^ { - 1 } \frac { \partial g } { \partial z } \right ] \, z ^ { \prime }$$

where we already know that ¯ v ′ = ( ρ + ȷω ) ◦ ¯ v = ¯ η ◦ ¯ v , hence:

$$\bar { s } ^ { \prime } = \frac { \partial \bar { s } } { \partial \bar { v } } \, \bar { \eta } \circ \bar { v } + \left [ \frac { \partial \bar { s } } { \partial z } + \frac { \partial \bar { s } } { \partial y } \left ( \frac { \partial g } { \partial y } \right ) ^ { - 1 } \frac { \partial g } { \partial z } \right ] \, z ^ { \prime }$$

<!-- image -->

<!-- image -->

## Component of the RoCoP

From the definition of complex frequency we can define the following components of the RoCoP:

$$\bar { s } _ { 1 } ^ { \prime } & = \bar { j } \bar { s } \circ \omega - \bar { j } \bar { S } \omega \, , \\ \bar { s } _ { 2 } ^ { \prime } & = \bar { s } \circ \varrho + \bar { s } \, \varrho \, .$$

<!-- image -->

<!-- image -->

## Component of the RoCoP

From the definition of complex frequency we can define the following components of the RoCoP:

$$\bar { s } _ { 1 } ^ { \prime } & = \bar { j } \bar { s } \circ \omega - \bar { j } \bar { S } \omega \, , \\ \bar { s } _ { 2 } ^ { \prime } & = \bar { s } \circ \varrho + \bar { s } \, \varrho \, .$$

$$\bar { s } ^ { \prime } = \bar { s } _ { 1 } ^ { \prime } + \bar { s } _ { 2 } ^ { \prime } \, .$$

<!-- image -->

where

<!-- image -->

## Special Cases: Constant Power Injection

The constraint is ¯ s = const .

<!-- image -->

<!-- image -->

## Special Cases: Constant Power Injection

The constraint is ¯ s = const .

Then, we obtain:

$$\bar { s } ^ { \prime } = 0 \ \Rightarrow \ \bar { s } _ { 1 } ^ { \prime } = - \bar { s } _ { 2 } ^ { \prime }$$

<!-- image -->

<!-- image -->

## Special Cases: Constant Power Injection

The constraint is ¯ s = const .

Then, we obtain:

$$\bar { s } ^ { \prime } = 0 \ \Rightarrow \ \bar { s } _ { 1 } ^ { \prime } = - \bar { s } _ { 2 } ^ { \prime }$$

This is a quite interesting result as it indicates that, during a transient, a constant power device (even a constant power load) affects the frequency at a bus if the voltage magnitude changes, and vice versa !

<!-- image -->

<!-- image -->

## Special Cases: Constant Admittance

The constraint is ¯ ı = ¯ Y o ¯ v

<!-- image -->

<!-- image -->

## Special Cases: Constant Admittance

The constraint is ¯ ı = ¯ Y o ¯ v

Then (after some tedious algebra), we obtain:

$$\bar { s } _ { 1 } ^ { \prime } = 0 \ \text { and } \ \bar { s } ^ { \prime } = \bar { s } _ { 2 } ^ { \prime }$$

<!-- image -->

<!-- image -->

## Special Cases: Constant Admittance

The constraint is ¯ ı = ¯ Y o ¯ v

Then (after some tedious algebra), we obtain:

$$\bar { s } _ { 1 } ^ { \prime } = 0 \ \text { and } \ \bar { s } ^ { \prime } = \bar { s } _ { 2 } ^ { \prime }$$

This is another interesting result as it indicates that a constant admittance cannot impact the frequency. It only impacts the voltage magnitude.

<!-- image -->

<!-- image -->

## Special Cases: Constant Current and Power Factor

The constraint is | ¯ ı | = const . and ϕ = const .

<!-- image -->

<!-- image -->

## Special Cases: Constant Current and Power Factor

The constraint is | ¯ ı | = const . and ϕ = const .

Then (after some tedious algebra), we obtain:

$$\bar { s } _ { 2 } ^ { \prime } = 0 \ \text { and } \ \bar { s } ^ { \prime } = \bar { s } _ { 1 } ^ { \prime }$$

<!-- image -->

<!-- image -->

## Special Cases: Constant Current and Power Factor

The constraint is | ¯ ı | = const . and ϕ = const .

Then (after some tedious algebra), we obtain:

$$\bar { s } _ { 2 } ^ { \prime } = 0 \ \text { and } \ \bar { s } ^ { \prime } = \bar { s } _ { 1 } ^ { \prime }$$

Yet another interesting result. This tells us that a constant current device cannot impact the voltage. It only impacts the frequency.

<!-- image -->

<!-- image -->

Modelling, Control, Stability Analysis and Simulation of Low-Inertia Power Systems

References

## Table of Contents

- 1 Motivations
- 2 Complex Frequency
- 3 Local Synchronization
- 4 Transient Slack Capability (TSC)
- 5 Application: Dual-GFM
- 6 References

<!-- image -->

<!-- image -->

## Conventional Stability and Synchronism - I

In conventional power systems, the study of synchronization is substantially a synonym of transient stability analysis, the ultimate goal of which is to determine whether generators remain synchronized after a disturbanc

<!-- image -->

<!-- image -->

## Conventional Stability and Synchronism - II

The IEEE Task Force on the Definition and Classification of Power System Stability states:

## Synchronism &amp; Stability

A machine keeps synchronism if the electromagnetic torque is equal and opposite to the mechanical torque delivered by the prime mover. Accordingly, this type of stability depends on the ability of the synchronous machines to maintain or restore the equilibrium between these two opposing torques

<!-- image -->

<!-- image -->

## Revisiting The Concept of Synchronization

The conventional understanding of synchronization no longer appears adequate for modern power systems.

<!-- image -->

<!-- image -->

## Revisiting The Concept of Synchronization

The conventional understanding of synchronization no longer appears adequate for modern power systems.

It falls short of capturing the high heterogeneity of devices influencing system transient behavior and does not take into account the dynamics of the amplitude of the voltage.

<!-- image -->

<!-- image -->

References

## Revisiting The Concept of Synchronization

The conventional understanding of synchronization no longer appears adequate for modern power systems.

It falls short of capturing the high heterogeneity of devices influencing system transient behavior and does not take into account the dynamics of the amplitude of the voltage.

In recent years, there has been a growing interest in revisiting the definition, interpretation and control of synchronization in power systems

<!-- image -->

<!-- image -->

## Complex Frequency &amp; Synchronization

Let's see how complex frequency can be utilized in the context of (local) synchronization.

<!-- image -->

<!-- image -->

## Complex Frequency &amp; Synchronization

Let's see how complex frequency can be utilized in the context of (local) synchronization.

Consider voltage ¯ v , current ¯ ı and admittance ¯ y .

<!-- image -->

<!-- image -->

## Complex Frequency &amp; Synchronization

Let's see how complex frequency can be utilized in the context of (local) synchronization.

Consider voltage ¯ v , current ¯ ı and admittance ¯ y .

Let denote the CF of these vectors as ¯ η , ¯ ξ and ¯ χ , respectively. Then, the time derivative of the Park vectors of voltage, current and impedance can be written in terms of their CF:

$$\bar { v } ^ { \prime } = \bar { v } \, \bar { \eta } \, , \quad \bar { \imath } ^ { \prime } = \bar { \imath } \bar { \xi } \, , \quad \bar { y } ^ { \prime } = \bar { y } \, \bar { \chi } \, .$$

<!-- image -->

<!-- image -->

## Alternative Expression of the RoCoP

Note that, in general, the complex frequency of the voltage is not equal to the complex frequency of the current, hence:

$$\bar { v } ^ { \prime } = \bar { \eta } _ { v } \bar { v }$$

¯ ı ′ = ¯ η ı ¯ ı

<!-- image -->

<!-- image -->

## Alternative Expression of the RoCoP

Note that, in general, the complex frequency of the voltage is not equal to the complex frequency of the current, hence:

$$\bar { v } ^ { \prime } = \bar { \eta } _ { v } \bar { v }$$

$$\bar { i } ^ { \prime } = \bar { \eta } _ { n } \bar { i }$$

$$p ^ { \prime } = ( \rho _ { v } + \rho _ { \imath } ) p - ( \omega _ { v } - \omega _ { \imath } ) q$$

$$q ^ { \prime } = ( \omega _ { v } - \omega _ { \imath } ) p - ( \rho _ { v } + \rho _ { \imath } ) q$$

<!-- image -->

Then, one obtains:

and

<!-- image -->

## Dynamic Equivalent of a Device connected to the Grid - I

Consider a three-phase balanced power system.

It is always possible to calculate a dynamic equivalent admittance of the device at terminals, ¯ y ∈ C , such that:

$$\bar { \imath } = \bar { y } \, \bar { v } \, .$$

<!-- image -->

<!-- image -->

<!-- image -->

## Dynamic Equivalent of a Device connected to the Grid - II

The time derivative of (2) gives:

$$\bar { \imath } ^ { \prime } & = \bar { y } ^ { \prime } \, \bar { v } + \bar { y } \, \bar { v } ^ { \prime } \, , \\ \bar { \imath } \, \bar { \xi } & = \bar { y } \, \bar { \chi } \, \bar { v } + \bar { y } \, \bar { v } \, \bar { \eta } \, , \\ \bar { \imath } \, \bar { \xi } & = \bar { y } \, \bar { v } \, \left ( \bar { \chi } + \bar { \eta } \right ) \, , \\ & \Rightarrow \bar { \chi } = \bar { \xi } - \bar { \eta } \, .$$

The CF of the dynamic equivalent admittance of the device, ¯ χ , is equal to the difference between the CF of the current injected at terminals and the CF of the terminal voltage.

In the following, local synchronization of devices is studied in terms of the complex variable ¯ χ .

<!-- image -->

<!-- image -->

## General expression of ¯ χ - I

It is possible to show that. for shunt-connected devices, the complex frequency of the current injected at terminals, ¯ ξ , can be written as:

$$\bar { \xi } = \bar { \xi } _ { a } + \bar { \kappa } _ { \rho } \rho + \bar { \kappa } _ { \omega } \omega \, ,$$

where ρ, ω ∈ R are the real and imaginary parts of the CF of the voltage at the point of connection of the device, respectively.

¯ ξ a , ¯ κ ρ , ¯ κ ω ∈ C are complex quantities that (potentially) depend on (some of) the states and algebraic variables of the dynamic model of the device.

<!-- image -->

<!-- image -->

## General expression of ¯ χ - II

Subtracting ¯ η from both sides of (4):

$$\bar { \xi } - \bar { \eta } & = \bar { \xi } _ { a } + \bar { \kappa } _ { \rho } \rho + \bar { \kappa } _ { \omega } \omega - \bar { \eta } \\ \bar { \chi } & = \bar { \xi } _ { a } + ( \bar { \kappa } _ { \rho } - 1 ) \rho + ( \bar { \kappa } _ { \omega } - j ) \omega \, .$$

In the following, (5) is utilized to find an analytical expression for ¯ χ to describe the different synchronization mechanisms devices have.

<!-- image -->

<!-- image -->

References

## Requirements of Local Synchronization

The starting point is the assumption that a shunt-connected device operates coherently if it can exchange active and/or reactive power with the rest of the grid.

In steady-state ac systems, this can happen only if the voltage and the injected current at the grid bus are isofrequential.

This condition is fulfilled if the imaginary part of the CF of the voltage and current injected at terminals are equal, i.e., ℑ{ ¯ ξ } = ℑ{ ¯ η } or, equivalently, ℑ{ ¯ χ } = 0.

It is also desirable to have an operation where ℜ{ ¯ ξ } = ℜ{ ¯ η } = ℜ{ ¯ χ } 0, which means an operation with a constant magnitude of the voltage and current injected at the terminals of the device.

<!-- image -->

<!-- image -->

Application:

Dual-GFM

References

## Bounded Local Synchronization (BLS)

<!-- image -->

BLS accounts for the constantly varying nature of power systems which are always subject to small perturbations.

<!-- image -->

<!-- image -->

## Asymptotic Local Synchronization (ALS)

<!-- image -->

ALS represents the strict theoretical condition where an exact complex isofrequential condition is achieved.

<!-- image -->

<!-- image -->

Modelling, Control, Stability Analysis and Simulation of Low-Inertia Power Systems

Federico Milano

Motivations

Complex Frequency

Local Synchronization

Transient Slack Capability (TSC)

Application: Dual-GFM

References

## Synchronization vs. Stability

## Important Remark

Local synchronization does not imply stability and stability does not imply local synchronization.

Of course, in many situations synchronization and stability are achieved simultaneously and the loss of one leads to the lack of the other.

However, there are cases where the system might be unstable but a certain device still locally synchronous, and the opposite case where the system might be stable but a device not local synchronous.

<!-- image -->

<!-- image -->

## Taxonomy of Local Synchronization

Let us derive the terms ¯ ξ a , ¯ κ ρ and ¯ κ ω for some common and relevant devices:

- Synchronous generator
- ZIP loads
- Induction motor
- Grid-following inverter-based resource (GFL-IBR)
- Grid-forming inverter-based resource (GFM-IBR)

<!-- image -->

<!-- image -->

## Synchronous Machine - I

## Sixth-order model:

$$\text {xth-order model} \colon & \\ & \bar { \chi } = \jmath \left ( \omega _ { r } - \omega \right ) \left ( \frac { \bar { \imath } ^ { * } ( \bar { Z } _ { q } ^ { * } v _ { d } - j \, \bar { Z } _ { d } v _ { q } ) } { ( x _ { 2 d } x _ { 2 q } - R _ { s } ^ { 2 } ) \imath ^ { 2 } } + 1 \right ) \\ & - \rho \left ( \frac { \bar { \imath } ^ { * } ( j \, \bar { Z } _ { q } ^ { * } v _ { q } - \bar { Z } _ { d } v _ { d } ) } { ( x _ { 2 d } x _ { 2 q } - R _ { s } ^ { 2 } ) \imath ^ { 2 } } + 1 \right ) \\ & + \frac { j \, \bar { \imath } ^ { * } \bar { Z } _ { q } ^ { * } ( \gamma _ { d 1 } e ^ { \prime } _ { 1 q } + ( 1 - \gamma _ { d 1 } ) \psi ^ { \prime } _ { 2 d } ) } { ( x _ { 2 d } x _ { 2 q } - R _ { s } ^ { 2 } ) \imath ^ { 2 } } \\ & + \frac { \bar { \imath } ^ { * } \bar { Z } _ { d } ( - \gamma _ { q 1 } e ^ { \prime } _ { 1 d } + ( 1 - \gamma _ { q 1 } ) \psi ^ { \prime } _ { 2 q } ) } { ( x _ { 2 d } x _ { a q } - R _ { s } ^ { 2 } ) \imath ^ { 2 } }$$

<!-- image -->

<!-- image -->

## Synchronous Machine - II

## Fourth order model:

$$\int \lim i t s _ { \ } e q \colon & \int ( \bar { \frac { i ^ { * } ( \bar { Z } _ { q } ^ { * } v _ { d } - j \, \bar { Z } _ { d } v _ { q } ) } { ( x _ { 1 d } x _ { 1 q } - R _ { s } ^ { 2 } ) ^ { i ^ { 2 } } } + 1 ) \right ] \\ & - \rho \left [ \left ( x _ { 1 d } x _ { 1 q } - R _ { s } ^ { 2 } \right ) v ^ { 2 } \right ] \\ & + \frac { \bar { \imath } ( j \, \bar { Z } _ { q } ^ { * } e _ { 1 q } ^ { \prime } - \bar { Z } _ { d } e _ { 1 d } ^ { \prime } ) } { ( x _ { 1 d } x _ { 1 q } - R _ { s } ^ { 2 } ) \, i ^ { 2 } }$$

<!-- image -->

<!-- image -->

## Synchronous Machine - III

## Second-order model:

$$\boxed { \bar { \chi } = \left ( \frac { - j \, \bar { s } } { x _ { 1 d } \, i ^ { 2 } } + 1 \right ) ( - \rho + j ( \omega _ { r } - \omega ) ) }$$

<!-- image -->

<!-- image -->

## Synchronous Machine - IV

Imposing the ALS condition (7), we obtain:

$$\left ( \frac { - j \, \bar { s } } { x _ { 1 d } \imath ^ { 2 } } + 1 \right ) ( - \rho + j \, ( \omega _ { r } - \omega ) ) & \to 0 \, , \\ \Rightarrow & - \rho + j \, ( \omega _ { r } - \omega ) \to 0 \, , \\ & \Leftrightarrow \rho \to 0 \land \omega \to \omega _ { r } \, . \\ \intertext { a l c a l l } \text {a locally synchronized synchronous machine sets } \rho & = 0 \, \text {and} \, \omega$$

Thus, a locally synchronized synchronous machine sets ρ = 0 and ω equal to its internal state ω r .

<!-- image -->

<!-- image -->

Motivations

Complex Frequency

References

## ZIP Load - I

The standard model of a ZIP load is:

$$p = p _ { 0 } \left ( k _ { p p } + k _ { \imath p } v + k _ { z p } v ^ { 2 } \right ) \, ,$$

$$q = q _ { 0 } \left ( k _ { p q } + k _ { \imath q } v + k _ { z q } v ^ { 2 } \right ) \, ,$$

where the k-parameters represent the quota of the load that behaves as constant impedance, current or power.

According to ALS, a constant impedance is always locally synchronous.

For a constant impedance load, namely k zp = k zq = 1, the results for ¯ ξ a , ¯ κ ρ and ¯ κ ω are:

$$\bar { \xi } _ { a } = 0 \, , \quad \bar { \kappa } _ { \rho } = 1 \, , \quad \bar { \kappa } _ { \omega } = \jmath \, .$$

$$\bar { \chi } = 0$$

<!-- image -->

Therefore:

<!-- image -->

## ZIP Load - II

For a constant current load ( k ı p = k ı q = 1):

$$\bar { \xi } _ { a } = 0 \, , \quad \bar { \kappa } _ { \rho } = 0 \, , \quad \bar { \kappa } _ { \omega } = \jmath \, .$$

$$\boxed { \bar { \chi } = - \rho }$$

Imposing the ALS condition (7), we obtain ρ → 0, which means that, a locally synchronized constant current load sets ρ = 0 while allowing ω to be free.

<!-- image -->

Therefore:

<!-- image -->

## ZIP Load - III

For a constant power load ( k pp = k pq = 1):

$$\bar { \xi } _ { a } = 0 \, , \quad \bar { \kappa } _ { \rho } = - 1 \, , \quad \bar { \kappa } _ { \omega } = J \, .$$

$$\boxed { \bar { \chi } = - 2 \rho }$$

Hence, the ALS condition for a constant power load requires ρ = 0 but does not impose any constraint in ω .

<!-- image -->

Therefore:

<!-- image -->

## Induction Motor - I

For a single-cage induction machine:

$$\bar { \xi } _ { \bar { \imath } } & = - \frac { r ^ { \prime } } { r } \left ( \frac { r ^ { 2 } ( x _ { t } ^ { 2 } - x ^ { 2 } ) + j \, r x _ { \mu } ( r ^ { 2 } - x ^ { 2 } - x _ { \mu } x ) } { z ^ { 2 } ( r ^ { 2 } + x _ { t } ^ { 2 } ) } \right ) , \\ \bar { \kappa } _ { \rho } & = 1 , \quad \bar { \kappa } _ { \omega } = \jmath .$$

The sought expression for ¯ χ is:

$$\boxed { \bar { \chi } = - \frac { r ^ { \prime } } { r } \left ( \frac { r ^ { 2 } ( x _ { t } ^ { 2 } - x ^ { 2 } ) + \jmath r x _ { \mu } ( r ^ { 2 } - x ^ { 2 } - x _ { \mu } x ) } { z ^ { 2 } ( r ^ { 2 } + x _ { t } ^ { 2 } ) } \right ) }$$

<!-- image -->

<!-- image -->

## Induction Motor - II

Imposing the ALS condition (7), we obtain:

$$- \frac { r ^ { \prime } } { r } \left ( \frac { r ^ { 2 } ( x _ { t } ^ { 2 } - x ^ { 2 } ) + j \, r x _ { \mu } ( r ^ { 2 } - x ^ { 2 } - x _ { \mu } x ) } { z ^ { 2 } ( r ^ { 2 } + x _ { t } ^ { 2 } ) } \right ) \to 0 \, , \\ \Rightarrow \frac { r ^ { \prime } } { r } \to 0 \, , \\ \Rightarrow \sigma ^ { \prime } \to 0 \, .$$

Therefore, an induction motor is locally synchronous as long as the torque balance is satisfied.

This means that the synchronization of the motor is solely determined by this internal balance, not by imposing any constraint on ¯ η at terminals.

<!-- image -->

<!-- image -->

## Grid Following Inverter-Based Resources (GFL-IBR) - I

Consider a simplified GFL-IBR model with a synchronous reference Phase Locked Loop (PLL) whose frequency estimation is ˜ ω , constant DC voltage v dc0 , and PI controllers for the internal current control loops ( K p , K i ) with fixed references ¯ ı ref = ı dref + ȷ ı qref .

The modulated signal is ¯ m = m ∠ α , and ¯ z f , ¯ y f are the output filter series impedance and shunt conductance, respectively.

<!-- image -->

<!-- image -->

## Grid Following Inverter-Based Resources (GFL-IBR) - II

The results for ¯ ξ a , ¯ κ ρ and ¯ κ ω are:

$$\bar { \xi } _ { a } & = \frac { \bar { m } v _ { d c 0 } } { \bar { z } _ { \bar { f } } \bar { \imath } } \left ( \frac { m ^ { \prime } } { m } + \jmath \left ( \alpha ^ { \prime } + \tilde { \omega } \right ) \right ) , \\ \bar { \kappa } _ { \rho } & = 1 - \frac { \bar { m } v _ { d c 0 } } { \bar { z } _ { \bar { f } } \bar { \imath } } \, , \quad \bar { \kappa } _ { \omega } = \jmath \left ( 1 - \frac { \bar { m } v _ { d c 0 } } { \bar { z } _ { \bar { f } } \bar { \imath } } \right ) .$$

The sought expression for ¯ χ is:

$$\bar { \chi } = \frac { \bar { m } \, v _ { d c 0 } } { \bar { z } _ { f } \, \bar { \imath } } \left ( \frac { m ^ { \prime } } { m } - \rho + j \left ( \alpha ^ { \prime } + \tilde { \omega } - \omega \right ) \right )$$

<!-- image -->

<!-- image -->

## Grid Following Inverter-Based Resources (GFL-IBR) - III

Applying the ALS condition (7), we obtain:

$$\frac { \bar { m } _ { \, v _ { d c } 0 } } { \bar { z } _ { f } \, \bar { \imath } } \left ( \frac { m ^ { \prime } } { m } - \rho + j \left ( \tilde { \omega } + \alpha ^ { \prime } - \omega \right ) \right ) & \to 0 \, , \\ & \Rightarrow \frac { m ^ { \prime } } { m } - \rho + j \left ( \tilde { \omega } + \alpha ^ { \prime } - \omega \right ) \to 0 \, , \\ & \Leftrightarrow \rho \to \frac { m ^ { \prime } } { m } \wedge \omega \to \tilde { \omega } + \alpha ^ { \prime } \, .$$

Therefore, a locally synchronized GFL-IBR drives ρ to m ′ m and ω to (˜ ω + α ′ ).

<!-- image -->

<!-- image -->

## Grid Forming Inverter-Based Resources (GFM-IBR) - I

We consider a GFM-IBR according to the WECC REGFM A1 model proposed by NREL:

$$e ^ { \prime } & = K _ { i } ( v _ { r e f } - v _ { m } ) - \frac { K _ { p } } { T _ { v } } ( v _ { m } - v ) \, , \\ \delta ^ { \prime } & = \Omega _ { b } ( \omega _ { g f m } - 1 ) \, ,$$

along with the algebraic equations:

$$\omega _ { g f m } & = m _ { p } ( p _ { r e f } - p _ { m } ) + 1 , \\ \bar { v } & = \bar { e } - \bar { z } _ { t } \bar { \iota } .$$

<!-- image -->

<!-- image -->

## Grid Forming Inverter-Based Resources (GFM-IBR) - II

The results for ¯ ξ a , ¯ κ ρ and ¯ κ ω are:

$$\bar { \xi } _ { a } & = \frac { \bar { e } } { \bar { z } _ { t } \bar { \i } } \left ( \frac { e ^ { \prime } } { e } + \jmath _ { \text {gfm} } \right ) , \\ \bar { \kappa } _ { \rho } & = 1 - \frac { \bar { e } } { \bar { z } _ { t } \bar { \i } } \, , \quad \bar { \kappa } _ { \omega } = \jmath \left ( 1 - \frac { \bar { e } } { \bar { z } _ { t } \bar { \i } } \right ) .$$

The sought expression for ¯ χ is:

$$\left [ \bar { \chi } = \frac { \bar { e } } { \bar { z } _ { t } \bar { \imath } } \left ( \frac { e ^ { \prime } } { e } - \rho + \jmath \left ( \omega _ { g f m } - \omega \right ) \right ) \right ]$$

<!-- image -->

<!-- image -->

## Grid Forming Inverter-Based Resources (GFM-IBR) - III

Imposing the ALS condition (7), we obtain:

$$\text {mg} \, \text { the } & \text {es} \, \text { combination} \, ( \real ) , \text { we } \, \text { sbtam.} \\ & \quad \frac { \bar { \ e } } { \bar { z } _ { t } \, \bar { \imath } } \left ( \frac { e ^ { \prime } } { e } - \rho + \jmath \left ( \omega _ { g f m } - \omega \right ) \right ) \to 0 \, , \\ & \quad \Rightarrow \frac { e ^ { \prime } } { e } - \rho + \jmath \left ( \omega _ { g f m } - \omega \right ) \to 0 \, , \\ & \quad \Leftrightarrow \rho \to \frac { e ^ { \prime } } { e } \wedge \omega \to \omega _ { g f m } \, .$$

Therefore, a locally synchronized GFM-IBR drives ρ to e ′ e and ω to ω gfm .

<!-- image -->

<!-- image -->

Motivations

Complex

Frequency

Local

Synchronization

Transient Slack

Capability (TSC)

Application:

Dual-GFM

References

## Example: Synchronous machine infinite bus (SMIB) - I

<!-- image -->

A three-phase short circuit is applied at simulation time t = 1 s in the middle of L2 and cleared at t cl by opening the breakers of line.

<!-- image -->

<!-- image -->

Modelling, Control, Stability Analysis and Simulation of Low-Inertia Power Systems

Federico Milano

Motivations

Complex

Frequency

Local

Synchronization

Transient Slack

Capability (TSC)

Application:

Dual-GFM

References

## Example: Synchronous machine infinite bus (SMIB) - II

<!-- image -->

We consider the response of the internal angle of the machine in two cases: t cl = 1 . 12 s and t cl = 1 . 13 s.

The critical clearing time is thus ∼ 130 ms.

<!-- image -->

<!-- image -->

References

## Example: Synchronous machine infinite bus (SMIB) - III

<!-- image -->

<!-- image -->

In this case, local synchronization and stability always coincide!

<!-- image -->

<!-- image -->

Modelling,

Control, Stability

Analysis and

Simulation of

Low-Inertia

Power Systems

Motivations

Complex

Frequency

Local

Synchronization

Transient Slack

Capability (TSC)

Application:

Dual-GFM

References

## Example: Kundur's two-areas system - I

A three-phase short circuit is applied in the middle of one of the circuits of line 07-09. The fault is applied at simulation time t = 1 s and cleared after 120 ms by opening the faulted circuit.

<!-- image -->

<!-- image -->

<!-- image -->

Local Synchronization

References

## Example: Kundur's two-areas system - II

<!-- image -->

The contingency forces the two groups of machines to drift away, separating the system and leading to an unstable response.

<!-- image -->

<!-- image -->

Complex

Frequency

Local

Synchronization

Transient Slack

Capability (TSC)

Application:

Dual-GFM

References

## Example: Kundur's two-areas system - III

<!-- image -->

<!-- image -->

The system is unstable but devices are locally synchronous to their own area.

<!-- image -->

<!-- image -->

References

## Example: Induction machine to infinite bus system - I

Consider a system composed of a first-order classical model of an induction motor connected to an infinite bus through a transformer and a line.

The synchronous condenser is suddenly disconnected at simulation time t = 1 s.

<!-- image -->

<!-- image -->

<!-- image -->

Modelling, Control, Stability Analysis and Simulation of Low-Inertia Power Systems

Federico Milano

Motivations

Complex

Frequency

Local

Synchronization

Transient Slack

Capability (TSC)

Application:

Dual-GFM

References

## Example: Induction machine to infinite bus system - II

<!-- image -->

<!-- image -->

The motor synchronization depends mostly on the real part of ¯ χ as the nature of the problem is associated with the inability of the system to supply the motor reactive power demand, leading to a voltage collapse at its terminals.

<!-- image -->

<!-- image -->

Modelling, Control, Stability Analysis and Simulation of Low-Inertia Power Systems

Local Synchronization

Transient Slack

Capability (TSC)

Application:

Dual-GFM

References

## Example: IEEE 14-bus system - I

A three-phase short circuit is applied at bus 14 at simulation time t = 1 s and cleared at t cl .

Two different cases in terms of the clearing time are considered, 60 ms and 120 ms.

Following the fault, the system trajectory ends up on a limit cycle.

<!-- image -->

<!-- image -->

<!-- image -->

## Example: IEEE 14-bus system - II

<!-- image -->

<!-- image -->

The limit cycle is stable but the machines are not locally synchronous!

<!-- image -->

<!-- image -->

References

## Example: GFL-IBR and series line compensation system - I

A three-phase short circuit is applied at bus 14 at simulation time t = 1 s and cleared at t cl .

<!-- image -->

This example is a typical scenario of resonance between the series compensation of a weak line and a poorly tuned SRF-PLL of a standard grid-following controlled converter.

A three-phase fault at L2 close to the terminals of the converter is applied at simulation time t = 1 s and cleared after 100 ms by opening the line.

<!-- image -->

<!-- image -->

Modelling, Control, Stability Analysis and Simulation of Low-Inertia Power Systems

Federico Milano

Motivations

Transient Slack

Capability (TSC)

Application:

Dual-GFM

References

## Example: GFL-IBR and series line compensation system - II

<!-- image -->

<!-- image -->

The dynamic response is characterized by poorly damped high-frequency oscillations caused by the interaction between the series capacitor and the PLL.

The GFL-IBR achieves asymptotic local synchronization as ¯ χ tends to zero.

<!-- image -->

<!-- image -->

Modelling, Control, Stability Analysis and Simulation of Low-Inertia Power Systems

Federico Milano

Motivations

Complex Frequency

Local Synchronization

Application: Dual-GFM

References

## Remarks

We have seen a novel concept of local synchronization based on the difference between the complex frequency of the voltage and current injected at device terminals.

This concept is formalized through two definitions that account for bounded and asymptotic local synchronization.

If one knows the model of the device,s it is possible to obtain analytically the synchronization mechanisms, i.e., the expression of ¯ χ .

<!-- image -->

<!-- image -->

Modelling, Control, Stability Analysis and Simulation of Low-Inertia Power Systems

Federico Milano

Motivations

Complex Frequency

Local Synchronization

Transient Slack Capability (TSC)

Application: Dual-GFM

References

## Take-home messages

## Local vs. Global

Synchronization is a local property, stability is a system-wide property.

## Synchronization vs. Stability

Synchronization does not imply stability and stability does not imply synchronization.

<!-- image -->

<!-- image -->

Modelling, Control, Stability Analysis and Simulation of Low-Inertia Power Systems

Motivations

## Table of Contents

- 1 Motivations
- 2 Complex Frequency
- 3 Local Synchronization
- 4 Transient Slack Capability (TSC)
- 5 Application: Dual-GFM
- 6 References

<!-- image -->

<!-- image -->

## Introduction

- Displacement of Synchronous Machines (SM) by Inverter-Based Resources (IBR) removes physical rotational inertia.
- The Gap: Standard GFL/GFM definitions describe how a device interacts with the grid, but not if it can maintain stability under sustained power imbalances.
- Objective: Propose a technology-agnostic metric, Transient Slack Capability (TSC) , based on energy storage and control bandwidth.

<!-- image -->

<!-- image -->

## Port-Hamiltonian (pH) Formulation

Any grid-connected device k is modeled as a pH system:

$$x _ { k } ^ { \prime } = [ \mathbf J _ { k } ( x _ { k } ) - \mathbf R _ { k } ( \mathbf x _ { k } ) ] \nabla \mathcal { H } _ { k } ( \mathbf x _ { k } ) + G _ { k } ( \mathbf x _ { k } ) \mathbf u _ { k } \quad ( 3 1 )$$

where:

- H k : Stored energy (The Hamiltonian).

- J k = - J ⊤ k :

Internal energy routing (conservative).

- R k = R ⊤ k ≥ 0:

Internal losses/dissipation.

- u k :

Input vectors (Source, Control, Grid).

<!-- image -->

<!-- image -->

Modelling,

Control, Stability

Analysis and

Simulation of

Low-Inertia

Power Systems

Motivations

Complex

Frequency

Local

Synchronization

Transient Slack

Capability (TSC)

Application:

Dual-GFM

References

## The 3-Condition Structure

<!-- image -->

Figure: Interaction between internal storage, external source, and control scheme.

<!-- image -->

<!-- image -->

## Condition 1: Energy Storage Capacity

A device must have a non-zero storage function H k ( x k ) such that:

$$\mathcal { H } _ { k } ^ { \prime } = \nabla \mathcal { H } _ { k } ^ { \top } \mathbf x _ { k } ^ { \prime } = - \nabla \mathcal { H } _ { k } ^ { \top } \mathbf R _ { k } \nabla \mathcal { H } _ { k } + \nabla \mathcal { H } _ { k } ^ { \top } \mathbf G _ { k } \mathbf u _ { k } \quad$$

## Requirements:

- H k must be positive semi-definite and radially unbounded.
- Physical examples: Rotating mass kinetic energy (SM) or DC-link capacitor energy (IBR).

<!-- image -->

<!-- image -->

## Condition 2: Dynamic Slack (Source Control)

To survive a sustained perturbation ∆ P , the input source power u S , k must be dynamic:

$$\mathfrak { u } _ { S , k } ^ { \prime } = f _ { s } ( \mathfrak { x } _ { k } , \mathfrak { u } _ { k } , \mu _ { k } )$$

Necessary Requirement:

$$\lim _ { t \to \infty } P _ { S , k } ( t ) = P _ { l o a d } + P _ { l o s s e s }$$

If P s is fixed, the energy buffer H k will eventually deplete (GFL collapse).

<!-- image -->

<!-- image -->

## Condition 3: Convergence and Synchronization

Control signals u C , k must enforce that the device synchronizes to the grid frequency ω s :

$$\lim _ { t \to \infty } \mathcal { H } ^ { \prime } ( t ) = 0 \ \text { and } \ \lim _ { t \to \infty } \omega ( t ) = \omega _ { s }$$

Using the complex frequency η = σ + j ω :

- σ must decay to zero (Energy balance).
- ω must track the grid (Synchronization).

<!-- image -->

<!-- image -->

Motivations

Complex

Frequency

References

## Test System Architecture

<!-- image -->

Figure: Modified WSCC 9-bus system where generators 1-3 are replaced by IBRs.

<!-- image -->

<!-- image -->

## Case Study: GFL Stability Boundaries

- Case 1: Base GFL (C1 only).
- Case 2: GFL with Frequency Support (C1 + C3).
- Case 3: GFL with TSC Source Control (C1 + C2 + C3).

Time-domain trajectories for GFL at Bus 1.

<!-- image -->

<!-- image -->

<!-- image -->

References

## The Impact of T slack

The speed of the source control (Condition 2) is critical.

Eigenvalue migration and V dc recovery as T slack varies.

<!-- image -->

<!-- image -->

<!-- image -->

## The Buffer Effect: C dc

Stability analysis relative to DC-link capacitance size.

<!-- image -->

<!-- image -->

<!-- image -->

## Condition 1 Visualization: DC-Voltage Buffer

<!-- image -->

Figure: Transient voltage dip for different C dc values following a load step.

<!-- image -->

<!-- image -->

## Grid-Forming (GFM) Converters and TSC

While GFM is often touted as the 'savior' of weak grids, it fails if Condition 2 is ignored:

- Case 4: GFM with fixed P s (Ideal DC-source assumption).
- Case 5: GFM with TSC source control.

<!-- image -->

<!-- image -->

## GFM Stability Comparison

<!-- image -->

Figure: Comparison of DC-link voltage stability for Case 4 vs. Case 5.

<!-- image -->

<!-- image -->

## GFM Synchronization Limits

<!-- image -->

Figure: Synchronization of GFM 1-3 under high-stress conditions.

<!-- image -->

<!-- image -->

## Trading Storage for Control Bandwidth

The paper proves a fundamental duality:

$$Stability \, \infty \, \frac { \mathcal { H } _ { c a p } } { T _ { s l a c k } }$$

- High storage (SM inertia) allows for slow governors.
- Low storage (small C dc ) requires ultra-fast source control.

<!-- image -->

<!-- image -->

## Inertia-less Operation ( M = 0)

<!-- image -->

Figure: VSM performance as inertia M → 0. Stability is maintained via Condition 2.

<!-- image -->

<!-- image -->

## Secondary Control Sensitivity

<!-- image -->

Figure: Effect of frequency gain K ω on system frequency nadir and recovery.

<!-- image -->

<!-- image -->

## Remarks

- TSC is a necessary but not sufficient condition for global stability.
- It provides a unified language for comparing disparate technologies (SM vs. IBR).
- Transitioning to 100% IBR requires specific focus on the source control dynamics (C2).

<!-- image -->

<!-- image -->

Modelling, Control, Stability Analysis and Simulation of Low-Inertia Power Systems

Motivations

Complex

Frequency

## Table of Contents

- 1 Motivations
- 2 Complex Frequency
- 3 Local Synchronization
- 4 Transient Slack Capability (TSC)
- 5 Application: Dual-GFM
- 6 References

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

Application:

Dual-GFM

References

## Dual Grid-Forming Converter

We now consider a dual model for grid-forming (GFM) controlled converters.

The model is inspired from the observation that the structures of the active and reactive power equations of lossy synchronous machine models are almost symmetrical in terms of armature resistance and transient reactance.

<!-- image -->

<!-- image -->

## Conventional Synchronous Machine - I

Consider the power injections of the lossy electromechanical model of the synchronous machine shown in the figure below:

$$p & = \frac { [ e v \cos ( \delta - \theta ) - v ^ { 2 } ] r _ { a } + [ e v \sin ( \delta - \theta ) ] x _ { 1 d } } { r _ { a } ^ { 2 } + x _ { 1 d } ^ { 2 } } \, , \\ q & = \frac { [ e v \cos ( \delta - \theta ) - v ^ { 2 } ] x _ { 1 d } - [ e v \sin ( \delta - \theta ) ] r _ { a } } { r _ { a } ^ { 2 } + x _ { 1 d } ^ { 2 } } \, .$$

<!-- image -->

<!-- image -->

<!-- image -->

## Conventional Synchronous Machine - II

In synchronous machines, the armature resistance r a is small with respect to x 1 d and is often neglected, thus leading to the well-known equations:

$$p & = \frac { e v \sin ( \delta - \theta ) } { x _ { 1 d } } \, , \\ q & = \frac { e v \cos ( \delta - \theta ) - v ^ { 2 } } { x _ { 1 d } } \, .$$

<!-- image -->

<!-- image -->

## Dual Model - I

Consider now the dual parts of the machine equations, that is, the terms that depend on the armature resistance and suppose that the reactance x 1 d is zero or negligible:

$$\tilde { p } & = \frac { \ e v \cos ( \delta - \theta ) - v ^ { 2 } } { r _ { a } } \, , \\ \tilde { q } & = - \frac { \ e v \sin ( \delta - \theta ) } { r _ { a } } \, .$$

<!-- image -->

<!-- image -->

## Dual Model - II

For simplicity, assume that the virtual parameter that represents the armature resistance is negative, say K = -1 / r a , thus leading to:

$$\tilde { p } & = K v ^ { 2 } - K e v \cos ( \delta - \theta ) \, , \\ \tilde { q } & = K e v \sin ( \delta - \theta ) \, . \\$$

For this hyptotheical device, the active power strongly depends on the magnitude of the internal emf e , while the reactive power strongly depends on the phase angle δ .

<!-- image -->

<!-- image -->

## Swing Equations

Recall that the conventional swing equation is defined in terms of the machine rotor angle:

$$\delta ^ { \prime } & = \omega - \omega _ { o } \, , \\ M \omega ^ { \prime } & = p _ { m } - p ( e , v , \delta , \theta ) - D ( \omega - \omega _ { o } ) \, ,$$

<!-- image -->

<!-- image -->

## Dual Swing Equations - I

To obtain the dual swing equation, consider the complex quantity:

$$\bar { e } = e \exp ( j \, \delta ) \, .$$

Define u = ln( e ), e = 0, then the previous equation becomes:

$$\bar { e } = \exp ( u + j \, \delta ) \, ,$$

̸

and its time derivative is:

$$\bar { e } ^ { \prime } = ( u ^ { \prime } + j \, \delta ^ { \prime } ) \exp ( u + j \, \delta ) = ( \varrho + j \, \omega ) \, \bar { e } \, ,$$

where ω is defined as in (37) and ϱ is:

$$\varrho = u ^ { \prime } = e ^ { \prime } / e \, .$$

<!-- image -->

<!-- image -->

## Dual Swing Equations - II

Finally, the swing equation dual to (37) is defined as:

$$u ^ { \prime } & = \rho \, , \\ \tilde { M } \rho ^ { \prime } & = p ^ { r e f } - \tilde { p } ( u , v , \delta , \theta ) - \tilde { D } \rho \, , \\$$

$$e ^ { \prime } & = \varrho \, e \, , \\ \tilde { M } _ { \varrho ^ { \prime } } & = p ^ { r e f } - \tilde { p } ( e , v , \delta , \theta ) - \tilde { D } _ { \varrho } \, ,$$

<!-- image -->

or, equivalently

<!-- image -->

## Primary Controllers

The simplest first order model for the turbine governor can be written as:

$$T _ { m } p _ { m } ^ { \prime } = \frac { 1 } { R } ( \omega ^ { r e f } - \omega ) + p _ { m , o } - p _ { m } \, ,$$

For a 3-rd order machine model, a basic automatic voltage control has the form:

$$T _ { 1 d 0 } e ^ { \prime } & = v _ { f } - ( x _ { d } - x _ { 1 d } ) i _ { d } - e \, , \\ T _ { r } v _ { f } ^ { \prime } & = K _ { r } ( v ^ { r e f } - v ) - v _ { f } \, ,$$

<!-- image -->

<!-- image -->

## Dual Primary Controllers

In the same vein, the primary active power control for the dual-GFM control is required to track ϱ , for example:

$$\tilde { T } _ { m } p _ { r e f } ^ { \prime } = \frac { 1 } { \tilde { R } } ( \varrho _ { r e f } - \varrho ) + p _ { r e f , o } - p _ { r e f } \, ,$$

The dual to the AVR can be written as:

$$T _ { q } \delta ^ { \prime } & = K _ { q } ( q ^ { \text {ref} } - \tilde { q } ) - \delta \, , \\ \tilde { T } _ { r } q _ { r e f } ^ { \prime } & = \tilde { K } _ { r } ( \omega _ { r e f } - \omega ) - q _ { r e f } \, , \\$$

or alternatively, defining:

$$\delta _ { r } = K _ { q } \, q ^ { r e f } \, .$$

$$T _ { q } \delta ^ { \prime } & = \delta _ { r } - K _ { q } \, \tilde { q } - \delta \, , \\ \tilde { T } _ { r } \delta ^ { \prime } _ { r } & = \tilde { K } ^ { \prime } _ { r } ( \omega ^ { r e f } - \omega ) - \delta _ { r } \, , \\ & \quad + \circ \, , \, \circ \, , \, \circ \, ,$$

<!-- image -->

we obtain:

<!-- image -->

Modelling,

Control, Stability

Analysis and

Simulation of

Low-Inertia

Power Systems

Motivations

Complex

Frequency

Local

Synchronization

Transient Slack

Capability (TSC)

Application:

Dual-GFM

References

## Complete Model of the Dual-GFM

<!-- image -->

<!-- image -->

<!-- image -->

Modelling, Control, Stability Analysis and Simulation of Low-Inertia Power Systems

Federico Milano

Motivations

Complex Frequency

Local Synchronization

Transient Slack Capability (TSC)

Application:

Dual-GFM

References

## Synchronism of Dual-GFMs

The virtual angular speed does not appear in the formulation of the dual-GFM control except for the time derivative of the internal signal δ in the reactive power control.

It is still necessary, of course, to fix the frequency in the system. The dual-GFM converter imposes the frequency at the bus through the regulation of the reactive power.

δ is relative to the phase angle θ of the voltage at the point of connection of the converter to the grid. Hence, to reach steady state, the rest of the grid must be synchronous at the rated frequency ω ref .

<!-- image -->

<!-- image -->

References

## Example 1: WSCC 9-bus System - I

All generators are dual-GFMs. 20% of loss of load.

<!-- image -->

<!-- image -->

<!-- image -->

## Example 1: WSCC 9-bus System - II

All generators are dual-GFMs. Short-circuit at but 7, cleared after 60 ms removing a line.

<!-- image -->

<!-- image -->

<!-- image -->

Modelling,

Control, Stability

Analysis and

Simulation of

Low-Inertia

Power Systems

Complex

Frequency

References

## Example 2: Modified All-Island Irish System - I

We illustrate the dynamic performance of the proposed dual-GFM converter for a dynamic model of the all-island Irish transmission system.

The original system includes 1479 buses, 1851 transmission lines and transformers, 22 synchronous generators, along with their appropriate control systems, 169 wind power plants and 245 loads.

All wind power plants are assumed to be GFLs and not to provide any inertial response nor fast-frequency regulation.

We have substituted all synchronous machiens with dual-GFMs with same capacity.

<!-- image -->

<!-- image -->

References

## Example 2: Modified All-Island Irish System - II

Outage of the largest infeed (connection with UK).

<!-- image -->

<!-- image -->

<!-- image -->

## Remarks

## Robustness

The dual-GFM is particularly robust and stable following large contingencies.

## Compatibility

The dual-GFM does not seem to work well combined with synchronous machines, but more tests are needed.

## Universality?

The dual-GFM seems to be able to work both in AC and DC. Future work will explore this feature and the implementation of a prototype!

<!-- image -->

<!-- image -->

Modelling, Control, Stability Analysis and Simulation of Low-Inertia Power Systems

Motivations

Complex

Frequency

Local Synchronization

## Table of Contents

- 1 Motivations
- 2 Complex Frequency
- 3 Local Synchronization
- 4 Transient Slack Capability (TSC)
- 5 Application: Dual-GFM
- 6 References

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## References

- F. Milano, Complex Frequency , IEEE Transactions on Power Systems, vol. 37, no. 2, pp. 1230-1240, March 2022. arXiv: 2105.07769
- I. Ponce, F. Milano, Local Synchronization of Power System Devices . IEEE Transactions on Power Systems, vol. 40, no. 5, pp. 4194-4204, September 2025. arXiv: 2407.02661
- F. Milano, Dual Grid-Forming Converter , IEEE Transactions on Power Systems, vol. 40, no. 2, pp. 1993-1996, March 2025. arXiv: 2408.13185
- R. Bernal, F. Milano, Transient Slack Capability . arXiv: 2505.17984

<!-- image -->

<!-- image -->

## Further Reading - I

## Works on applications of complex frequency.

- D. Moutevelis, J. Rold´ an-P´ erez, M. Prodanovic and F. Milano, Taxonomy of Power Converter Control Schemes based on the Complex Frequency Concept , in IEEE Transactions on Power Systems, preprint available. arXiv: 2209.11107
- R. Bernal, F. Milano, A Complex Frequency-Based Control for Inverter-Based Resources , Journal of Modern Power Systems and Clean Energy (MPCE), SGEPRI, accepted for publication in March 2025. arXiv: 2501.00448
- I. Ponce, R. Bernal, F. Milano, Coherency among Power System Devices . arXiv: 2511.02486
- I. Ponce, F. Milano, Analytical Framework for Power System Strength . arXiv: 2507.16061

<!-- image -->

<!-- image -->

## Further Reading - II

Works on the generalization of complex frequency.

- F. Milano, A Geometrical Interpretation of Frequency , IEEE Transactions on Power Systems, vol. 37, no. 1, pp. 816-819, January 2022.
- F. Milano, Equivalence between Geometric Frequency and Lagrange Derivative , IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 72, no. 9, pp. 4800-4809, September 2025. arXiv: 2410.02340
- J. Guti´ errez Florensa, ´ A. Ortega, L. Sigrist, F. Milano, Quasi Steady-State Frequency , IEEE Transactions on Circuits and Systems I: Regular Papers, accepted for publication in September 2025. arXiv: 2505.21461

<!-- image -->

<!-- image -->

Thank you!

<!-- image -->