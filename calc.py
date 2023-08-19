import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, execute, Aer, QuantumRegister

num_qubits = 1
qreg = QuantumRegister(num_qubits, 'q')

G = 6.67430e-11
h_bar = 1.0545718e-34
speed_of_light = 3.00e8
spin_bh = 0.2

def apply_black_hole_properties(qc, mass, spin):
    qc.rx(2 * np.arcsin(np.sqrt(spin)), qreg[0])
    qc.rz(mass * np.pi, qreg[0])

def calculate_temperature(mass):
    qc = QuantumCircuit(qreg)
    apply_black_hole_properties(qc, mass, spin_bh)
    
    backend = Aer.get_backend('statevector_simulator')
    job = execute(qc, backend)
    result = job.result()
    statevector = result.get_statevector()
    
    avg_energy = np.real(np.vdot(statevector, np.dot(h_bar * speed_of_light**3 / (8 * np.pi * G), statevector)))
    
    temperature = avg_energy / (3.15e7 * mass)  # 3.15e7 is a conversion factor for time
    return temperature


plt.figure(figsize=(8, 6))

while True:
    initial_mass_str = input("Enter the initial mass of the black hole (kg) or type 'exit' to quit: ")
    if initial_mass_str == 'exit':
        break
    
    try:
        initial_mass = float(initial_mass_str)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    
    t_max = 100
    delta_t = 1
    
    time = np.arange(0, t_max, delta_t)
    masses_bh = initial_mass * np.exp(-0.1 * time)

    temperature_data = []

    for i, mass_bh in enumerate(masses_bh):
        temperature = calculate_temperature(mass_bh)
        temperature_data.append(temperature)

    plt.plot(time, temperature_data, label=f"Mass: {initial_mass} kg")

plt.xlabel("Time (quantum time units)")
plt.ylabel("Temperature (K)")
plt.title("Black Hole Temperature vs. Time")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()