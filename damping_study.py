import math
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# MECHANICAL SYSTEM
# ============================================================

mass = 10.0
spring_stiffness = 500.0
force_amplitude = 20.0


# ============================================================
# NATURAL FREQUENCY
# ============================================================

omega_n = math.sqrt(
    spring_stiffness / mass
)

frequency_n = omega_n / (2.0 * math.pi)


# ============================================================
# DAMPING VALUES
# ============================================================

damping_values = [
    10.0,
    20.0,
    40.0
]


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
# THEORETICAL FREQUENCY RESPONSE
# ============================================================

def calculate_amplitude(
    forcing_frequency,
    damping
):

    forcing_omega = (
        2.0
        * math.pi
        * forcing_frequency
    )

    denominator = math.sqrt(
        (
            spring_stiffness
            - mass * forcing_omega**2
        )**2
        +
        (
            damping * forcing_omega
        )**2
    )

    amplitude = (
        force_amplitude
        / denominator
    )

    return amplitude


# ============================================================
# PRINT HEADER
# ============================================================

print()
print("=" * 70)
print("             EFFECT OF DAMPING ON RESONANCE")
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
    f"Force amplitude:       "
    f"{force_amplitude:.2f} N"
)

print(
    f"Natural frequency:     "
    f"{frequency_n:.4f} Hz"
)


# ============================================================
# CREATE GRAPH
# ============================================================

plt.figure(
    figsize=(10, 6)
)


# ============================================================
# CALCULATE EACH DAMPING CASE
# ============================================================

for damping in damping_values:

    damping_ratio = (
        damping
        / (
            2.0
            * math.sqrt(
                spring_stiffness * mass
            )
        )
    )

    amplitude_values = np.array([
        calculate_amplitude(
            frequency,
            damping
        )
        for frequency in frequency_values
    ])


    # --------------------------------------------------------
    # Find peak from frequency sweep
    # --------------------------------------------------------

    peak_index = np.argmax(
        amplitude_values
    )

    peak_frequency = (
        frequency_values[
            peak_index
        ]
    )

    peak_amplitude = (
        amplitude_values[
            peak_index
        ]
    )


    # --------------------------------------------------------
    # Theoretical resonance frequency
    # --------------------------------------------------------

    if damping_ratio < 1.0 / math.sqrt(2.0):

        resonance_omega = (
            omega_n
            * math.sqrt(
                1.0
                - 2.0
                * damping_ratio**2
            )
        )

        resonance_frequency = (
            resonance_omega
            / (2.0 * math.pi)
        )

    else:

        resonance_frequency = None


    # --------------------------------------------------------
    # Print results
    # --------------------------------------------------------

    print()
    print(
        f"DAMPING = {damping:.1f} N*s/m"
    )

    print(
        f"Damping ratio:        "
        f"{damping_ratio:.5f}"
    )

    print(
        f"Peak frequency:       "
        f"{peak_frequency:.4f} Hz"
    )

    print(
        f"Peak amplitude:       "
        f"{peak_amplitude:.6f} m"
    )

    if resonance_frequency is not None:

        print(
            f"Theoretical resonance:"
            f" {resonance_frequency:.4f} Hz"
        )


    # --------------------------------------------------------
    # Plot response curve
    # --------------------------------------------------------

    plt.plot(
        frequency_values,
        amplitude_values,
        label=(
            f"c = {damping:.0f} N*s/m"
        )
    )


# ============================================================
# NATURAL FREQUENCY LINE
# ============================================================

plt.axvline(
    frequency_n,
    linestyle=":",
    linewidth=1,
    label="Natural frequency"
)


# ============================================================
# GRAPH FORMATTING
# ============================================================

plt.title(
    "Effect of Damping on Mechanical Resonance"
)

plt.xlabel(
    "Forcing frequency (Hz)"
)

plt.ylabel(
    "Displacement amplitude (m)"
)

plt.grid(True)

plt.legend()

plt.tight_layout()


# ============================================================
# SHOW GRAPH
# ============================================================

plt.show()


# ============================================================
# FINISHED
# ============================================================

print()
print("=" * 70)
print("Damping study completed.")
print("=" * 70)