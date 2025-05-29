import numpy as np

class NoiseAdder:
    def __init__(self, noise_type='gaussian', noise_level=0.1):
        self.noise_type = noise_type
        self.noise_level = noise_level

    def add_noise(self, signal: np.ndarray) -> np.ndarray:
        if self.noise_type == 'gaussian':
            noise = np.random.normal(loc=0.0, scale=self.noise_level, size=signal.shape)
        elif self.noise_type == 'uniform':
            noise = np.random.uniform(low=-self.noise_level, high=self.noise_level, size=signal.shape)
        else:
            raise ValueError("Unknown noise type. Use 'gaussian' or 'uniform'.")

        return signal + noise

    def __str__(self):
        return f"NoiseAdder(noise_type={self.noise_type}, noise_level={self.noise_level})"

    def __eq__(self, other):
        return isinstance(other, NoiseAdder) and \
            self.noise_type == other.noise_type and \
            self.noise_level == other.noise_level