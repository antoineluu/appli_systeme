import matplotlib.pyplot as plt
import numpy as np

# fig = plt.figure(figsize=(12,10))
fig, axs = plt.subplots(3,1, sharex=True, figsize=(10,7))
[ax1,ax2,ax3]=axs
speckle = [9.9141,9.4697,9.4782,9.4799,9.4624]
gaussian = [9.9141,9.4141,9.8908,9.9884,10.0274]
additive= [9.9141,9.9324,10.3482,10.4155,10.3987]
speckle_x = np.array([201.8175,187.3566,187.2673,187.2739,187.2661])/20
gaussian_x = np.array([201.8175,201.8175,200.3711,201.1495,201.6496])/20
additive_x = np.array([201.8175,202.0960,207.5095,208.0203,207.3894])/20

xs = ["0","1e-1","1","2","1e1"]
ax1.set_title("Speckle")
ax1.plot(xs, speckle, label="focused", color="b")
ax1.plot(xs, speckle_x, label="unfocused", color="b", linestyle="--")
ax1.set_ylabel("entropy")
ax1.legend()

ax2.set_title("Gaussian filtering")
ax2.plot(xs, gaussian, label="focused", color="r")
ax2.set_ylabel("entropy")
ax2.plot(xs, gaussian_x, label="unfocused", color="r", linestyle="--")
ax2.legend()

ax3.set_title("Additive White Noise")
ax3.set_ylabel("entropy")
ax3.plot(xs, additive, label="focused", color="g")
ax3.plot(xs, additive_x, label="unfocused", color="g", linestyle="--")
ax3.legend()
ax1.grid()
ax2.grid()
ax3.grid()
plt.suptitle("Evolution of entropy on different noise sources in function of intensity")
ax3.set_xlabel("Noise variance")
plt.savefig("./noiseplot.png")

plt.show()