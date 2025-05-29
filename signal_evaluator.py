import numpy as np

class SignalEvaluator:
    def __init__(self, original_signal: np.ndarray, noisy_signal: np.ndarray):
        self.original_signal = original_signal
        self.noisy_signal = noisy_signal
        self.mean_difference = None
        self.std_difference = None
        self.snr = None

    def evaluate(self):
        difference = self.original_signal - self.noisy_signal

        self.mean_difference = np.mean(difference)

        self.std_difference = np.std(difference)

        noise_power = np.mean((self.original_signal - self.noisy_signal) ** 2)
        signal_power = np.mean(self.original_signal ** 2)
        self.snr = 10 * np.log10(signal_power / noise_power) if noise_power != 0 else float('inf')

    def get_report(self):
        return {
            "Mean Difference": self.mean_difference,
            "Standard Deviation": self.std_difference,
            "SNR (dB)": self.snr
        }
