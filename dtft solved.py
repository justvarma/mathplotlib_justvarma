import numpy as np
import matplotlib.pyplot as plt

# Input the sequence h
h = []
no = int(input('Size: '))
c = float(input('Coefficient: '))
for i in range(no):
    el = float(input())
    h.append(el * c)
print("Sequence h:", h)

# Function to compute DTFT
def dtft(x):
    sm = 0
    for i in range(no):
        exp = np.exp(-1j * x * i)
        sm += exp * h[i]
    return sm

# Frequency range for DTFT
lm = np.linspace(-3*np.pi, 3*np.pi, 1000)

# Compute DTFT values
dm = []
for k in lm:
    dm.append(dtft(k))

# Magnitude and phase of DTFT
mg = np.abs(dm)
ph = np.angle(dm)

# Plotting
fig, axs = plt.subplots(3, 1, figsize=(9, 9))

# Plot 1: Original sequence h
axs[0].stem(h, use_line_collection=True)
axs[0].set_title('Sequence h')

# Plot 2: Magnitude of DTFT
axs[1].plot(lm, mg)
axs[1].set_title('Magnitude of DTFT')

# Plot 3: Phase of DTFT
axs[2].plot(lm, ph)
axs[2].set_title('Phase of DTFT')

plt.tight_layout()
plt.show()