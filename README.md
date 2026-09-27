# Mechanical Vibration Analyzer

A Python-based mechanical engineering project for analyzing the behavior of a mass-spring-damper vibration system.

The project combines mechanical vibration theory with numerical programming using Python, NumPy, SciPy, and Matplotlib.

The main system is described by the differential equation:

$$
m\ddot{x} + c\dot{x} + kx = F(t)
$$

where:

* \(m\) = mass
* \(c\) = damping coefficient
* \(k\) = spring stiffness
* \(x\) = displacement
* \(F(t)\) = external force

---

## 1. Project Purpose

The purpose of this project was to build a genuine mechanical-engineering vibration analyzer step by step.

The project demonstrates:

* natural frequency
* damping ratio
* free vibration
* displacement, velocity, and acceleration
* forced vibration
* resonance
* numerical solution of differential equations
* theoretical frequency response
* numerical validation
* influence of damping on resonance
* phase response

The project was developed and tested on Windows using Python 3.13.

---

## 2. Mechanical System

The basic mechanical system uses the following parameters:

| Parameter            | Value | Unit  |
| -------------------- | ----: | ----- |
| Mass                 |  10.0 | kg    |
| Spring stiffness     | 500.0 | N/m   |
| Damping coefficient  |  20.0 | N·s/m |
| Initial displacement |  0.10 | m     |
| Initial velocity     |  0.00 | m/s   |
| Force amplitude      |  20.0 | N     |

The equation of motion is:

$$
m\ddot{x}+c\dot{x}+kx=F(t)
$$

---

## 3. Project Structure

The project directory is:

```text
C:\dev1\mechanical-vibration
```

Important files:

```text
mechanical-vibration
│
├── .venv
│
├── vibration_basic.py
├── resonance_analysis.py
├── resonance_validation.py
├── damping_study.py
├── phase_response.py
│
└── README.md
```

### File descriptions

### `vibration_basic.py`

The main introductory vibration program.

It covers:

* natural frequency
* damping ratio
* free vibration
* forced vibration
* displacement
* velocity
* acceleration
* external applied force

It uses SciPy's `solve_ivp` numerical differential-equation solver for forced vibration.

---

### `resonance_analysis.py`

Performs a frequency sweep to investigate resonance.

The forcing frequency is varied from approximately:

```text
0.1 Hz to 2.5 Hz
```

The program determines the frequency at which the displacement response reaches its maximum.

The calculated peak response was approximately:

```text
Peak response frequency: 1.0939 Hz
Peak displacement amplitude: 0.142507 m
Natural frequency: 1.1254 Hz
```

The peak occurs slightly below the undamped natural frequency because the system is damped.

---

### `resonance_validation.py`

Compares:

1. numerical frequency response obtained with the RK45 solver
2. theoretical steady-state frequency response

The theoretical displacement amplitude is:

$$
X(\omega)=
\frac{F_0}
{\sqrt{(k-m\omega^2)^2+(c\omega)^2}}
$$

The numerical and theoretical results were:

```text
Numerical peak frequency:      1.0939 Hz
Numerical peak amplitude:      0.142507 m

Theoretical peak frequency:    1.0939 Hz
Theoretical peak amplitude:    0.142649 m

Maximum difference:            0.000164 m
Maximum relative error:        0.115 %
```

The small error demonstrates that the numerical model agrees very closely with the analytical solution.

---

### `damping_study.py`

Investigates how damping affects resonance.

Three damping coefficients were compared:

```text
10 N*s/m
20 N*s/m
40 N*s/m
```

Results:

|  Damping | Damping ratio | Peak frequency | Peak amplitude |
| -------: | ------------: | -------------: | -------------: |
| 10 N·s/m |       0.07071 |      1.1186 Hz |     0.283524 m |
| 20 N·s/m |       0.14142 |      1.1018 Hz |     0.142855 m |
| 40 N·s/m |       0.28284 |      1.0321 Hz |     0.073721 m |

The study demonstrates that increasing damping significantly reduces the resonance amplitude.

It also causes the resonance frequency to move to a lower frequency.

---

### `phase_response.py`

Calculates the phase difference between the applied force and the displacement.

The phase angle is calculated using:

$$
\phi =
\operatorname{atan2}
\left(
c\omega,
k-m\omega^2
\right)
$$

Selected results:

| Frequency | Phase angle |
| --------: | ----------: |
|   0.20 Hz |      2.971° |
|   0.50 Hz |      8.899° |
|   1.00 Hz |     50.061° |
|   1.10 Hz |     80.831° |
| 1.1258 Hz |     90.155° |
|   1.50 Hz |    154.104° |
|   2.00 Hz |    166.890° |

The phase approaches 90° near the natural frequency and approaches 180° at higher frequencies.

---

# 4. Important Mechanical Calculations

## Natural frequency

The undamped natural angular frequency is:

$$
\omega_n=\sqrt{\frac{k}{m}}
$$

For this system:

$$
\omega_n=7.0711\text{ rad/s}
$$

The natural frequency in Hz is:

$$
f_n=\frac{\omega_n}{2\pi}
$$

giving:

$$
f_n=1.1254\text{ Hz}
$$

---

## Damping ratio

The damping ratio is:

$$
\zeta=
\frac{c}{2\sqrt{km}}
$$

For:

```text
m = 10 kg
k = 500 N/m
c = 20 N*s/m
```

the result is:

$$
\zeta=0.1414
$$

Therefore the system is **underdamped**.

---

## Damped natural frequency

For an underdamped system:

$$
\omega_d=
\omega_n\sqrt{1-\zeta^2}
$$

For this system:

$$
\omega_d=7.0000\text{ rad/s}
$$

---

# 5. Free Vibration

For the underdamped system, the displacement has the form:

$$
x(t)=
e^{-\alpha t}
\left[
A\cos(\omega_d t)
+
B\sin(\omega_d t)
\right]
$$

where:

$$
\alpha=\frac{c}{2m}
$$

For this system:

$$
\alpha=1.0000\text{ s}^{-1}
$$

The resulting free-vibration graph shows oscillations whose amplitude gradually decreases because mechanical energy is dissipated by damping.

---

# 6. Forced Vibration

The external force used in the project is:

$$
F(t)=F_0\sin(\omega t)
$$

with:

```text
F0 = 20 N
```

The forcing frequency was varied to investigate the system response.

The forced-vibration problem was solved numerically using:

```text
SciPy solve_ivp
RK45 method
```

The second-order differential equation was represented as two first-order equations:

$$
\dot{x}=v
$$

$$
\dot{v}=
\frac{F(t)-cv-kx}{m}
$$

---

# 7. Resonance

The project demonstrated that the vibration amplitude becomes large when the forcing frequency approaches the system's resonant region.

For the original system:

```text
Natural frequency: approximately 1.1254 Hz
Peak response: approximately 1.10 Hz
```

The resonant frequency is slightly below the undamped natural frequency because damping is present.

---

# 8. Numerical Validation

One of the important engineering aspects of this project is that the numerical simulation was not simply accepted without verification.

The numerical RK45 solution was compared against the theoretical frequency-response equation.

The maximum relative difference was:

```text
0.115 %
```

This provides a strong numerical validation of the implementation for the selected system and simulation settings.

---

# 9. Effect of Damping

The damping study demonstrated an important engineering principle.

When damping increased:

```text
c = 10 N*s/m
        ↓
c = 20 N*s/m
        ↓
c = 40 N*s/m
```

the resonance peak became substantially smaller.

The approximate peak amplitudes were:

```text
c = 10 N*s/m  → 0.2835 m
c = 20 N*s/m  → 0.1429 m
c = 40 N*s/m  → 0.0737 m
```

Thus damping is an important method for controlling excessive vibration near resonance.

---

# 10. Phase Response

The project also calculated the phase difference between force and displacement.

At low forcing frequency, the displacement is nearly in phase with the applied force.

Near the natural frequency, the phase approaches:

$$
90^\circ
$$

At frequencies substantially above resonance, the phase approaches:

$$
180^\circ
$$

This phase behavior is a fundamental characteristic of a damped second-order mechanical system.

---

# 11. Python Environment

The project uses a Python virtual environment:

```text
C:\dev1\mechanical-vibration\.venv
```

The main packages are:

```text
numpy
scipy
matplotlib
```

The environment can be activated with PowerShell:

```powershell
cd C:\dev1\mechanical-vibration
.\.venv\Scripts\Activate.ps1
```

The prompt should then show:

```text
(.venv) PS C:\dev1\mechanical-vibration>
```

---

# 12. Running the Programs

With the virtual environment activated:

### Basic vibration analysis

```powershell
python vibration_basic.py
```

### Resonance analysis

```powershell
python resonance_analysis.py
```

### Numerical/theoretical validation

```powershell
python resonance_validation.py
```

### Damping study

```powershell
python damping_study.py
```

### Phase response

```powershell
python phase_response.py
```

Matplotlib opens graphical windows for the various analyses.

The Python process remains active while a Matplotlib graph window is open. Close the graph window when finished before starting another analysis from the same PowerShell session.

---

# 13. Technologies Used

* Python 3.13
* NumPy
* SciPy
* Matplotlib
* Differential-equation numerical integration
* Analytical mechanical-vibration equations
* Windows PowerShell
* Python virtual environment

---

# 14. Engineering Concepts Demonstrated

This project demonstrates the relationship between programming and mechanical engineering.

The main concepts are:

```text
Mass
   ↓
Spring stiffness
   ↓
Natural frequency
   ↓
Damping
   ↓
Free vibration
   ↓
Forced vibration
   ↓
Resonance
   ↓
Frequency response
   ↓
Phase response
   ↓
Numerical validation
```

The project therefore provides a practical computational model of a classical single-degree-of-freedom mechanical vibration system.

---

# 15. Project Completion

The project was intentionally completed at **Step 10**.

Completed stages:

```text
Step 1   Natural frequency
Step 2   Damping
Step 3   Free vibration
Step 4   Displacement graph
Step 5   Velocity and acceleration
Step 6   Forced vibration
Step 7   Resonance analysis
Step 8   Numerical vs theoretical validation
Step 9   Effect of damping on resonance
Step 10  Phase response
```

The project successfully combines mechanical engineering theory with numerical Python programming and graphical analysis.

**Project status: COMPLETED**
