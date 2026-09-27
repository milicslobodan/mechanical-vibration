import math
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# MECHANICAL SYSTEM
# ============================================================

mass = 10.0
spring_stiffness = 500.0
damping = 20.0

force_amplitude = 20.0


# ============================================================
# NATURAL FREQUENCY
# ============================================================

omega_n = math.sqrt(
    spring_stiffness / mass
)

frequency_n = (
    omega_n / (2.0 * math.pi)
)


# ============================================================
# FREQUENCY RANGE
# ============================================================

minimum_frequency = 0.1
maximum_frequency = 2.5
number_of_frequencies = 1000

frequency_values = np.linspace(
    minimum_frequency,
    maximum_frequency,
    number_of_frequencies
)


# ============================================================
# CALCULATE PHASE RESPONSE
# ============================================================

phase_values = []


for frequency in frequency_values:

    omega = (
        2.0
        * math.pi
        * frequency
    )

    numerator = (
        damping * omega
    )

    denominator = (
        spring_stiffness
        - mass * omega**2
    )

    phase = math.atan2(
        numerator,
        denominator
    )

    phase_degrees = (
        math.degrees(phase)
    )

    phase_values.append(
        phase_degrees
    )


phase_values = np.array(
    phase_values
)


# ============================================================
# FIND PHASE NEAR NATURAL FREQUENCY
# ============================================================

natural_frequency_index = (
    np.argmin(
        np.abs(
            frequency_values
            - frequency_n
        )
    )
)

phase_at_natural_frequency = (
    phase_values[
        natural_frequency_index
    ]
)

frequency_at_index = (
    frequency_values[
        natural_frequency_index
    ]
)


# ============================================================
# PRINT RESULTS
# ============================================================

print()
print("=" * 70)
print("                  PHASE RESPONSE ANALYSIS")
print("=" * 70)

print()
print("MECHANICAL SYSTEM")
print("-" * 70)

print(
    f"Mass:                 "
    f"{mass:.2f} kg"
)

print(
    f"Spring stiffness:     "
    f"{spring_stiffness:.2f} N/m"
)

print(
    f"Damping:              "
    f"{damping:.2f} N*s/m"
)

print(
    f"Force amplitude:       "
    f"{force_amplitude:.2f} N"
)

print(
    f"Natural frequency:     "
    f"{frequency_n:.4f} Hz"
)


print()
print("PHASE RESULTS")
print("-" * 70)

print(
    f"Frequency examined:    "
    f"{frequency_at_index:.4f} Hz"
)

print(
    f"Phase angle:           "
    f"{phase_at_natural_frequency:.4f} degrees"
)


# ============================================================
# PHASE AT SELECTED FREQUENCIES
# ============================================================

selected_frequencies = [
    0.2,
    0.5,
    1.0,
    1.1,
    1.5,
    2.0
]


print()
print("PHASE AT SELECTED FREQUENCIES")
print("-" * 70)

for frequency in selected_frequencies:

    omega = (
        2.0
        * math.pi
        * frequency
    )

    numerator = (
        damping * omega
    )

    denominator = (
        spring_stiffness
        - mass * omega**2
    )

    phase = math.atan2(
        numerator,
        denominator
    )

    phase_degrees = math.degrees(
        phase
    )

    print(
        f"{frequency:5.2f} Hz"
        f"    "
        f"{phase_degrees:8.3f} degrees"
    )


# ============================================================
# GRAPH
# ============================================================

plt.figure(
    figsize=(10, 6)
)

plt.plot(
    frequency_values,
    phase_values,
    label="Phase response"
)

plt.axvline(
    frequency_n,
    linestyle=":",
    linewidth=1,
    label="Natural frequency"
)

plt.axhline(
    90.0,
    linestyle="--",
    linewidth=1,
    label="90 degrees"
)

plt.title(
    "Mechanical Vibration - Phase Response"
)

plt.xlabel(
    "Forcing frequency (Hz)"
)

plt.ylabel(
    "Phase angle (degrees)"
)

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.show()


# ============================================================
# FINISHED
# ============================================================

print()
print("=" * 70)
print("Phase response analysis completed.")
print("=" * 70)