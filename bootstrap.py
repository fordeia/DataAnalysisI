import numpy as np

def bootstrap_diff_means_ci(data1, data2, n_resamples=10000, confidence=0.95):
    """
    Calculates the bootstrap confidence interval for the difference of means between two samples.

    Args:
        data1 (array-like): First sample data.
        data2 (array-like): Second sample data.
        n_resamples (int, optional): Number of bootstrap resamples. Defaults to 10000.
        confidence (float, optional): Confidence level for the interval. Defaults to 0.95.

    Returns:
        tuple: Lower and upper bounds of the confidence interval.
    """
    diff_means = []

    for _ in range(n_resamples):
        # Resample with replacement
        resample_data1 = np.random.choice(data1, size=len(data1), replace=True)
        resample_data2 = np.random.choice(data2, size=len(data2), replace=True)
        # Calculate the difference of means for the resampled data
        diff_means.append(np.mean(resample_data1) - np.mean(resample_data2))

    # Calculate the confidence interval
    alpha = 1 - confidence
    lower_bound = np.percentile(diff_means, alpha/2 * 100)
    upper_bound = np.percentile(diff_means, (1 - alpha/2) * 100)
    return lower_bound, upper_bound


if __name__ == '__main__':
    # Example usage
    data_group1 = [38.9, 61.2, 73.3, 21.8, 63.4, 64.6, 48.4, 48.8, 48.5]
    data_group2 = [67.8, 60, 63.4, 76, 89.4, 73.3, 67.3, 61.3, 62.4]

    ci = bootstrap_diff_means_ci(data_group1, data_group2)
    print(f"Bootstrap Confidence Interval for the difference of means: {ci}")
