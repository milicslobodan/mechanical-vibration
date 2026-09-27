# Mechanical Vibration Analyzer

## User Instructions

---

## 1. Purpose of the Program

The **Mechanical Vibration Analyzer** is a Python program for studying the vibration of a mechanical mass-spring-damper system.

It can calculate and display:

* natural frequency
* damping
* free vibration
* displacement
* velocity
* acceleration
* forced vibration
* resonance
* frequency response
* effect of damping
* phase response

The program also compares numerical calculations with theoretical mechanical-vibration equations.

---

# 2. Project Location

The project is located at:

```text
C:\dev1\mechanical-vibration
```

The main program files are:

```text
vibration_basic.py
resonance_analysis.py
resonance_validation.py
damping_study.py
phase_response.py
```

---

# 3. Starting the Program

Open **PowerShell**.

Enter:

```powershell
cd C:\dev1\mechanical-vibration
```

Activate the Python virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

The PowerShell prompt should change to:

```text
(.venv) PS C:\dev1\mechanical-vibration>
```

This means that the project's Python environment is active.

---

# 4. Running the Basic Vibration Analysis

Enter:

```powershell
python vibration_basic.py
```

The program performs the basic mechanical-vibration calculations and displays graphs.

Depending on the version of the program, several graph windows may appear.

These include:

* displacement
* velocity
* acceleration
* external applied force

---

# 5. Running the Resonance Analysis

Enter:

```powershell
python resonance_analysis.py
```

This program changes the forcing frequency over a range and determines where the vibration response becomes largest.

The program reports the peak response frequency and displacement amplitude.

A frequency-response graph is displayed.

---

# 6. Running the Numerical Validation

Enter:

```powershell
python resonance_validation.py
```

This program compares:

**Numerical solution**

with

**Theoretical solution**

The program reports the difference between the two methods.

For the completed project, the maximum relative error was approximately:

```text
0.115 %
```

This demonstrates that the numerical calculation agrees closely with the theoretical result for the selected system.

---

# 7. Studying the Effect of Damping

Enter:

```powershell
python damping_study.py
```

The program compares three damping coefficients:

```text
10 N*s/m
20 N*s/m
40 N*s/m
```

A graph titled:

```text
Effect of Damping on Resonance
```

is displayed.

The graph allows the user to see how increasing damping changes the resonance curve.

In this project, increasing damping reduced the maximum displacement response.

---

# 8. Studying Phase Response

Enter:

```powershell
python phase_response.py
```

A graph titled:

```text
Mechanical Vibration - Phase Response
```

is displayed.

The program calculates the phase difference between the applied force and the displacement.

The phase changes from approximately:

```text
0 degrees
```

at low frequencies toward:

```text
180 degrees
```

at higher frequencies.

Near the natural frequency, the phase is approximately:

```text
90 degrees
```

---

# 9. Understanding the Main Mechanical Parameters

The system used in this project has:

| Parameter         |     Value | Meaning                    |
| ----------------- | --------: | -------------------------- |
| Mass              |     10 kg | Mass of vibrating body     |
| Spring stiffness  |   500 N/m | Stiffness of spring        |
| Damping           |  20 N*s/m | Resistance to motion       |
| Force amplitude   |      20 N | Applied periodic force     |
| Natural frequency | 1.1254 Hz | Undamped natural frequency |

The fundamental equation is:

$$
m\ddot{x}+c\dot{x}+kx=F(t)
$$

where:

* `m` = mass
* `c` = damping
* `k` = spring stiffness
* `x` = displacement
* `F(t)` = external force

---

# 10. Viewing the Graphs

When a graph window appears, study the shape of the curve.

For example, in the resonance graph:

* horizontal axis = forcing frequency
* vertical axis = displacement amplitude

A large peak indicates a strong vibration response.

In the damping study, compare the heights of the three resonance peaks.

In the phase-response graph, observe how the phase angle changes as the forcing frequency increases.

---

# 11. Important: Closing Graph Windows

Matplotlib graph windows are interactive.

When a graph is displayed, the Python program normally waits until the graph window is closed.

Therefore:

1. Examine the graph.
2. Close the graph window.
3. Return to PowerShell.
4. Run the next Python program.

For example:

```powershell
python damping_study.py
```

After examining the graph, close it before running:

```powershell
python phase_response.py
```

---

# 12. If PowerShell Appears Stuck

Normally this is simply because a Matplotlib graph is still open.

First check whether a Python graph window is open and close it.

If a Python process remains after the graph has been closed, you can check:

```powershell
Get-Process python
```

If necessary, stop the Python processes with:

```powershell
Stop-Process -Name python -Force
```

Then verify:

```powershell
Get-Process python
```

If no Python process is listed, the project is ready to run again.

---

# 13. Changing the Mechanical System

The Python files contain the mechanical parameters near the beginning of the programs.

For example:

```python
mass = 10.0
spring_stiffness = 500.0
damping = 20.0
```

The values can be changed to study another mechanical system.

For example, changing:

```python
mass = 20.0
```

changes the mass from 10 kg to 20 kg.

Changing:

```python
spring_stiffness = 1000.0
```

changes the spring stiffness from 500 N/m to 1000 N/m.

After changing a parameter, save the file and run the program again.

---

# 14. Important Unit Rule

Use consistent SI units.

Recommended units are:

```text
Mass              kg
Spring stiffness  N/m
Damping           N*s/m
Force             N
Displacement      m
Velocity          m/s
Acceleration      m/s²
Frequency         Hz
Angular frequency rad/s
```

Do not enter centimetres where metres are expected.

For example:

```text
10 cm = 0.10 m
```

---

# 15. Python Environment

The project has its own Python virtual environment.

It is located at:

```text
C:\dev1\mechanical-vibration\.venv
```

Always activate it before running the project:

```powershell
cd C:\dev1\mechanical-vibration
.\.venv\Scripts\Activate.ps1
```

The prompt should show:

```text
(.venv)
```

---

# 16. Quick Reference

For normal use:

```powershell
cd C:\dev1\mechanical-vibration
.\.venv\Scripts\Activate.ps1
```

Then choose one:

```powershell
python vibration_basic.py
```

```powershell
python resonance_analysis.py
```

```powershell
python resonance_validation.py
```

```powershell
python damping_study.py
```

```powershell
python phase_response.py
```

---

# 17. Recommended Order

For someone learning the project for the first time, run the programs in this order:

### 1. Basic vibration

```powershell
python vibration_basic.py
```

### 2. Resonance

```powershell
python resonance_analysis.py
```

### 3. Numerical validation

```powershell
python resonance_validation.py
```

### 4. Damping

```powershell
python damping_study.py
```

### 5. Phase

```powershell
python phase_response.py
```

This order follows the development of the mechanical-vibration model.

---

# 18. Project Completion

The project is completed through **Step 10**.

The completed analyzer demonstrates the essential behavior of a damped single-degree-of-freedom mechanical vibration system.

The project can be used as a foundation for future engineering studies involving:

* different masses
* different springs
* different damping coefficients
* different forcing forces
* different forcing frequencies
* vibration isolation
* machinery vibration
* structural vibration
* resonance control

**Status: PROJECT COMPLETED — STEP 10**
