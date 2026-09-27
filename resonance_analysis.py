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

omega_n = math.sqrt(spring_stiffness / mass)
frequency_n = omega_n / (2 * math.pi)

damping_ratio = damping / (
    2 * math.sqrt(spring_stiffness * mass)
)


# ============================================================
# FREQUENCY RANGE FOR ANALYSIS
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
# SIMULATION SETTINGS
# ============================================================

simulation_time = 20.0
number_of_time_points = 4000

time_values = np.linspace(
    0.0,
    simulation_time,
    number_of_time_points
)


# ============================================================
# FORCED VIBRATION EQUATION
# ============================================================

def calculate_response(forcing_frequency):

    forcing_omega = 2.0 * math.pi * forcing_frequency

    def external_force(time):
        return force_amplitude * math.sin(
            forcing_omega * time
        )

    def vibration_equation(time, state):

        displacement = state[0]
        velocity = state[1]

        force = external_force(time)

        acceleration = (
            force
            - damping * velocity
            - spring_stiffness * displacement
        ) / mass

        return [velocity, acceleration]

    initial_state = [0.0, 0.0]

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
    # We use the final 25% of the simulation.
    # --------------------------------------------------------

    start_index = int(
        len(displacement) * 0.75
    )

    steady_state_displacement = displacement[
        start_index:
    ]

    # Peak amplitude during steady state
    amplitude = (
        np.max(np.abs(steady_state_displacement))
    )

    return amplitude


# ============================================================
# FREQUENCY RESPONSE CALCULATION
# ============================================================

amplitude_values = []


print()
print("=" * 60)
print("       MECHANICAL RESONANCE ANALYSIS")
print("=" * 60)

print()
print("MECHANICAL SYSTEM")
print("-" * 60)

print(f"Mass:                 {mass:.2f} kg")
print(f"Spring stiffness:     {spring_stiffness:.2f} N/m")
print(f"Damping:              {damping:.2f} N*s/m")
print(f"Force amplitude:      {force_amplitude:.2f} N")

print()
print("NATURAL FREQUENCY")
print("-" * 60)

print(f"Natural frequency:    {frequency_n:.4f} Hz")
print(f"Natural frequency:    {omega_n:.4f} rad/s")
print(f"Damping ratio:        {damping_ratio:.4f}")

print()
print("CALCULATING FREQUENCY RESPONSE")
print("-" * 60)


for frequency in frequency_values:

    amplitude = calculate_response(
        frequency
    )

    amplitude_values.append(amplitude)


amplitude_values = np.array(
    amplitude_values
)


# ============================================================
# FIND MAXIMUM RESPONSE
# ============================================================

maximum_index = np.argmax(
    amplitude_values
)

peak_frequency = frequency_values[
    maximum_index
]

peak_amplitude = amplitude_values[
    maximum_index
]


# ============================================================
# RESULTS
# ============================================================

print()
print("RESONANCE RESULT")
print("-" * 60)

print(
    f"Peak response frequency: "
    f"{peak_frequency:.4f} Hz"
)

print(
    f"Peak displacement amplitude: "
    f"{peak_amplitude:.6f} m"
)

print(
    f"Natural frequency: "
    f"{frequency_n:.4f} Hz"
)

print()
print(
    "The frequency response has been calculated."
)

print("=" * 60)


# ============================================================
# PLOT FREQUENCY RESPONSE
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    frequency_values,
    amplitude_values
)

plt.axvline(
    frequency_n,
    linestyle="--",
    linewidth=1,
    label="Natural frequency"
)

plt.axvline(
    peak_frequency,
    linestyle=":",
    linewidth=1,
    label="Peak response"
)

plt.title(
    "Mechanical Vibration - Frequency Response"
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