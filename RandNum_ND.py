import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
a = float(input("Enter the lower bound of the interval (a): ")) # Lower bound of interval
b = float(input("Enter the upper bound of the interval (b): ")) # Upper bound of interval

if(a >= b):
    raise ValueError("Invalid input: Value of b should be greater than a")

mu = float(input("Enter the mean of the Gaussian distribution (mu): ")) # Mean of Gaussian distribution
sigma = float(input("Enter the standard deviation of the Gaussian distribution (sigma): ")) # Standard deviation of Gaussian distribution

num_samples = 1000000 # Sample size

if(sigma == 0):
    # If sigma is 0, only sample at the mean
    gaussian_samples = np.full(num_samples, mu)
else:
    # Compute the Inverse CDF for the Gaussian distribution
    def inverse_cdf(x):
        return norm.ppf(x, loc=mu, scale=sigma)

    # Generate Uniform Random Numbers
    uniform_samples = np.random.uniform(low=a, high=b, size=num_samples)

    # Apply the Inverse Transform
    gaussian_samples = inverse_cdf((uniform_samples - a) / (b - a))

# Plot Histogram
fig, axs = plt.subplots(1, 2, figsize=(13, 5))

# Plot Uniform Samples
axs[0].hist(uniform_samples, density=True, bins=50, alpha=0.5, color='b')
axs[0].set_title('Uniform Distribution')
axs[0].set_xlabel('Value')
axs[0].set_ylabel('Density')
axs[0].grid(True)

# Plot Gaussian Samples
axs[1].hist(gaussian_samples, bins=50, alpha=0.6, color='g')
axs[1].set_title('Histogram of Gaussian Distribution')
axs[1].set_xlabel('Value')
axs[1].set_ylabel('Frequency')
axs[1].grid(True)

plt.tight_layout()
plt.show()
