import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# ============================================================
# MECHANICAL SYSTEM
# ============================================================

mass = 10.0                  # kg
spring_stiffness = 500.0     # N/m
damping = 20.0               # N*s/m


# ============================================================
# INITIAL CONDITIONS
# ============================================================

initial_displacement = 0.10  # m
initial_velocity = 0.0       # m/s


# ============================================================
# EXTERNAL FORCE
# ============================================================

force_amplitude = 20.0       # N
forcing_frequency = 1.0      # Hz

forcing_omega = 2 * math.pi * forcing_frequency


# ============================================================
# SIMULATION SETTINGS
# ============================================================

simulation_time = 10.0       # seconds
number_of_points = 2000


# ============================================================
# BASIC VIBRATION PARAMETERS
# ============================================================

# Natural angular frequency
omega_n = math.sqrt(spring_stiffness / mass)

# Natural frequency in Hz
frequency_n = omega_n / (2 * math.pi)

# Natural period
period_n = 1 / frequency_n


# ============================================================
# DAMPING
# ============================================================

# Damping ratio
damping_ratio = damping / (
    2 * math.sqrt(spring_stiffness * mass)
)


# Determine system type
if damping_ratio < 1:
    damping_type = "Underdamped"
elif math.isclose(damping_ratio, 1.0):
    damping_type = "Critically damped"
else:
    damping_type = "Overdamped"


# ============================================================
# EXTERNAL FORCE FUNCTION
# ============================================================

def external_force(time):
    """
    External sinusoidal force F(t) in Newtons.
    """

    return force_amplitude * math.sin(
        forcing_omega * time
    )


# ============================================================
# EQUATION OF MOTION
# ============================================================

def vibration_equation(time, state):
    """
    Differential equation for the forced
    mass-spring-damper system.

    State:
        state[0] = displacement x
        state[1] = velocity v

    Mechanical equation:

        m*a + c*v + k*x = F(t)

    Therefore:

        a = (F(t) - c*v - k*x) / m
    """

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


# ============================================================
# TIME VALUES
# ============================================================

time_values = np.linspace(
    0,
    simulation_time,
    number_of_points
)


# ============================================================
# INITIAL STATE
# ============================================================

initial_state = [
    initial_displacement,
    initial_velocity
]


# ============================================================
# NUMERICAL SOLUTION
# ============================================================

solution = solve_ivp(
    vibration_equation,
    [0, simulation_time],
    initial_state,
    t_eval=time_values,
    method="RK45"
)


# Check whether the solver succeeded
if not solution.success:
    print("ERROR: Numerical solution failed.")
    print(solution.message)
    raise SystemExit


# ============================================================
# EXTRACT RESULTS
# ============================================================

displacement_values = solution.y[0]

velocity_values = solution.y[1]


# ============================================================
# CALCULATE ACCELERATION
# ============================================================

force_values = np.array([
    external_force(t)
    for t in time_values
])

acceleration_values = (
    force_values
    - damping * velocity_values
    - spring_stiffness * displacement_values
) / mass


# ============================================================
# PRINT RESULTS
# ============================================================

print()
print("==========================================")
print("     FORCED MECHANICAL VIBRATION")
print("==========================================")
print()
print("MECHANICAL SYSTEM")
print("------------------------------------------")
print(f"Mass:                 {mass:.2f} kg")
print(f"Spring stiffness:     {spring_stiffness:.2f} N/m")
print(f"Damping:              {damping:.2f} N*s/m")
print()
print("NATURAL VIBRATION")
print("------------------------------------------")
print(f"Natural frequency:    {omega_n:.4f} rad/s")
print(f"Natural frequency:    {frequency_n:.4f} Hz")
print(f"Natural period:       {period_n:.4f} s")
print(f"Damping ratio:        {damping_ratio:.4f}")
print(f"System type:          {damping_type}")
print()
print("EXTERNAL FORCE")
print("------------------------------------------")
print(f"Force amplitude:      {force_amplitude:.2f} N")
print(f"Forcing frequency:    {forcing_frequency:.4f} Hz")
print(f"Forcing frequency:    {forcing_omega:.4f} rad/s")
print()
print("NUMERICAL SOLUTION")
print("------------------------------------------")
print(f"Solver:               RK45")
print(f"Solver successful:    {solution.success}")
print(f"Number of points:     {number_of_points}")
print()
print("Selected simulation values:")
print("------------------------------------------")

for t in [0.0, 0.25, 0.50, 0.75, 1.00, 2.00, 5.00, 10.00]:

    index = np.argmin(
        np.abs(time_values - t)
    )

    print(
        f"t = {time_values[index]:5.2f} s   "
        f"F = {force_values[index]:8.3f} N   "
        f"x = {displacement_values[index]:9.5f} m   "
        f"v = {velocity_values[index]:9.5f} m/s   "
        f"a = {acceleration_values[index]:9.5f} m/s^2"
    )

print("==========================================")
print()


# ============================================================
# DISPLACEMENT GRAPH
# ============================================================

plt.figure(figsize=(10, 5))

plt.plot(
    time_values,
    displacement_values
)

plt.axhline(0, linewidth=1)

plt.title("Forced Mechanical Vibration - Displacement")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.grid(True)
plt.tight_layout()


# ============================================================
# VELOCITY GRAPH
# ============================================================

plt.figure(figsize=(10, 5))

plt.plot(
    time_values,
    velocity_values
)

plt.axhline(0, linewidth=1)

plt.title("Forced Mechanical Vibration - Velocity")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)
plt.tight_layout()


# ============================================================
# ACCELERATION GRAPH
# ============================================================

plt.figure(figsize=(10, 5))

plt.plot(
    time_values,
    acceleration_values
)

plt.axhline(0, linewidth=1)

plt.title("Forced Mechanical Vibration - Acceleration")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s^2)")
plt.grid(True)
plt.tight_layout()


# ============================================================
# EXTERNAL FORCE GRAPH
# ============================================================

plt.figure(figsize=(10, 5))

plt.plot(
    time_values,
    force_values
)

plt.axhline(0, linewidth=1)

plt.title("External Applied Force")
plt.xlabel("Time (s)")
plt.ylabel("Force (N)")
plt.grid(True)
plt.tight_layout()


# ============================================================
# SHOW ALL GRAPHS
# ============================================================

plt.show()