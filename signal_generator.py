import numpy as np

class SignalGenerator:
    def __init__(self, signal_type, frequency, amplitude, duration, sample_rate):
        self.signal_type = signal_type
        self.frequency = frequency
        self.amplitude = amplitude
        self.duration = duration
        self.sample_rate = sample_rate

    def generate(self):
        time = self.get_time_axis()
        
        if self.signal_type == 'sine':
            signal = self.amplitude * np.sin(2 * np.pi * self.frequency * time)
        elif self.signal_type == 'square':
            signal = self.amplitude * np.sign(np.sin(2 * np.pi * self.frequency * time))
        elif self.signal_type == 'triangle':
            signal = (2 * self.amplitude / np.pi) * np.arcsin(np.sin(2 * np.pi * self.frequency * time))
        else:
            print(f"Error: Unknown signal type '{self.signal_type}'")
            signal = np.array([]) 
            
        return signal

    def get_time_axis(self):
        num_points = int(self.duration * self.sample_rate)
        time_axis = np.linspace(0, self.duration, num_points, endpoint=False)
        return time_axis

    def __str__(self):
        description = f"SignalGenerator(Type: {self.signal_type}, "
        description += f"Freq: {self.frequency} Hz, Amp: {self.amplitude}, "
        description += f"Dur: {self.duration}s, Rate: {self.sample_rate} Hz)"
        return description

    def __eq__(self, other_object):
        if not isinstance(other_object, SignalGenerator):
            return False 
            
        return (self.signal_type == other_object.signal_type and
                self.frequency == other_object.frequency and
                self.amplitude == other_object.amplitude and
                self.duration == other_object.duration and
                self.sample_rate == other_object.sample_rate)