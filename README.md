Creating Random Sampler using the inverse CDF method

This Python script generates histogram for Gaussian distribution using the inverse CDF method. It allows users to specify parameters such as the interval bounds, mean, and standard deviation.

How to Use:

1. Download the python script
2. Ensure you have Python installed on your system. If not, you can download it from python.org.
3. Install required dependencies using pip:
    pip install numpy matplotlib scipy
4. Run the script gaussian_histogram_generator.py:
    python gaussian_histogram_generator.py
5. Follow the prompts to input the required parameters:
   - Lower bound of the interval (a)
   - Upper bound of the interval (b)
   - Mean of the Gaussian distribution (mu)
   - Standard deviation of the Gaussian distribution (sigma)
6. The script will generate two histograms:
   - Histogram of uniform distribution within the specified interval generated using np.random.
   - Histogram of Gaussian distribution with the provided mean and standard deviation.

Additional Notes:

- Ensure that the upper bound (b) is greater than the lower bound (a) for the interval.
- The number of samples is fixed at 1,000,000 for both distributions.