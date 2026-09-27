import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


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

frequency_n = omega_n / (2.0 * math.pi)

damping_ratio = damping / (
    2.0 * math.sqrt(
        spring_stiffness * mass
    )
)


# ============================================================
# FREQUENCY RANGE
# ============================================================

minimum_frequency = 0.1
maximum_frequency = 2.5
number_of_frequencies = 100

frequency_values = np.linspace(
    minimum_frequency,
    maximum_frequency,
    number_of_frequencies
)


# ============================================================
# NUMERICAL SIMULATION SETTINGS
# ============================================================

simulation_time = 20.0
number_of_time_points = 4000

time_values = np.linspace(
    0.0,
    simulation_time,
    number_of_time_points
)


# ============================================================
# NUMERICAL FREQUENCY RESPONSE
# ============================================================

def calculate_numerical_response(
    forcing_frequency
):

    forcing_omega = (
        2.0
        * math.pi
        * forcing_frequency
    )

    def external_force(time):

        return (
            force_amplitude
            * math.sin(
                forcing_omega * time
            )
        )

    def vibration_equation(
        time,
        state
    ):

        displacement = state[0]
        velocity = state[1]

        force = external_force(time)

        acceleration = (
            force
            - damping * velocity
            - spring_stiffness * displacement
        ) / mass

        return [
            velocity,
            acceleration
        ]

    initial_state = [
        0.0,
        0.0
    ]

    solution = solve_ivp(
        vibration_equation,
        [0.0, simulation_time],
        initial_state,
        t_eval=time_values,
        method="RK45"
    )

    if not solution.success:

        raise RuntimeError(
            "Numerical solution failed."
        )

    displacement = solution.y[0]

    # --------------------------------------------------------
    # Ignore the initial transient response.
    # Use the final 25% of the simulation.
    # --------------------------------------------------------

    start_index = int(
        len(displacement) * 0.75
    )

    steady_state_displacement = (
        displacement[start_index:]
    )

    amplitude = np.max(
        np.abs(
            steady_state_displacement
        )
    )

    return amplitude


# ============================================================
# THEORETICAL FREQUENCY RESPONSE
# ============================================================

def calculate_theoretical_response(
    forcing_frequency
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
# CALCULATE BOTH RESPONSES
# ============================================================

numerical_amplitudes = []
theoretical_amplitudes = []


print()
print("=" * 65)
print("       FREQUENCY RESPONSE VALIDATION")
print("=" * 65)

print()
print("MECHANICAL SYSTEM")
print("-" * 65)

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
    f"Force amplitude:      "
    f"{force_amplitude:.2f} N"
)

print()
print("NATURAL FREQUENCY")
print("-" * 65)

print(
    f"Natural frequency:    "
    f"{frequency_n:.4f} Hz"
)

print(
    f"Natural frequency:    "
    f"{omega_n:.4f} rad/s"
)

print(
    f"Damping ratio:        "
    f"{damping_ratio:.4f}"
)

print()
print("CALCULATING RESPONSES")
print("-" * 65)


for frequency in frequency_values:

    numerical_amplitude = (
        calculate_numerical_response(
            frequency
        )
    )

    theoretical_amplitude = (
        calculate_theoretical_response(
            frequency
        )
    )

    numerical_amplitudes.append(
        numerical_amplitude
    )

    theoretical_amplitudes.append(
        theoretical_amplitude
    )


numerical_amplitudes = np.array(
    numerical_amplitudes
)

theoretical_amplitudes = np.array(
    theoretical_amplitudes
)


# ============================================================
# FIND PEAKS
# ============================================================

numerical_peak_index = np.argmax(
    numerical_amplitudes
)

theoretical_peak_index = np.argmax(
    theoretical_amplitudes
)


numerical_peak_frequency = (
    frequency_values[
        numerical_peak_index
    ]
)

theoretical_peak_frequency = (
    frequency_values[
        theoretical_peak_index
    ]
)


numerical_peak_amplitude = (
    numerical_amplitudes[
        numerical_peak_index
    ]
)

theoretical_peak_amplitude = (
    theoretical_amplitudes[
        theoretical_peak_index
    ]
)


# ============================================================
# VALIDATION ERROR
# ============================================================

absolute_difference = np.abs(
    numerical_amplitudes
    - theoretical_amplitudes
)

maximum_difference = np.max(
    absolute_difference
)

maximum_theoretical_amplitude = np.max(
    theoretical_amplitudes
)

relative_error_percent = (
    maximum_difference
    / maximum_theoretical_amplitude
    * 100.0
)


# ============================================================
# PRINT RESULTS
# ============================================================

print()
print("NUMERICAL RESULT")
print("-" * 65)

print(
    f"Peak frequency:      "
    f"{numerical_peak_frequency:.4f} Hz"
)

print(
    f"Peak amplitude:      "
    f"{numerical_peak_amplitude:.6f} m"
)


print()
print("THEORETICAL RESULT")
print("-" * 65)

print(
    f"Peak frequency:      "
    f"{theoretical_peak_frequency:.4f} Hz"
)

print(
    f"Peak amplitude:      "
    f"{theoretical_peak_amplitude:.6f} m"
)


print()
print("VALIDATION")
print("-" * 65)

print(
    f"Maximum difference:   "
    f"{maximum_difference:.6f} m"
)

print(
    f"Maximum relative error:"
    f" {relative_error_percent:.3f} %"
)

print()
print(
    "Numerical and theoretical "
    "responses have been compared."
)

print("=" * 65)


# ============================================================
# COMPARISON GRAPH
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    frequency_values,
    numerical_amplitudes,
    label="Numerical - RK45"
)

plt.plot(
    frequency_values,
    theoretical_amplitudes,
    linestyle="--",
    label="Theoretical"
)

plt.axvline(
    frequency_n,
    linestyle=":",
    linewidth=1,
    label="Natural frequency"
)

plt.title(
    "Mechanical Vibration - "
    "Numerical vs Theoretical Response"
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

plt.show()