# pip install qiskit

import qiskit as q

circuit = q.QuantumCircuit(2, 2)

# 0 0
circuit.x(0)

# 1 0
circuit.cx(0, 1)

# 1 1
circuit.measure([0, 1], [0, 1])

circuit.draw()
