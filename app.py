import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from signal_generator import SignalGenerator
from noise_adder import NoiseAdder
from signal_evaluator import SignalEvaluator

# Title
st.title("Signal Generator with Noise and Evaluation")

# Sidebar Inputs
st.sidebar.header("Signal Parameters")
signal_type = st.sidebar.selectbox("Signal Type", ["sine", "square", "triangle"])
frequency = st.sidebar.slider("Frequency (Hz)", 1, 100, 10)
amplitude = st.sidebar.slider("Amplitude", 0.1, 5.0, 1.0)
duration = st.sidebar.slider("Duration (s)", 0.1, 5.0, 1.0)
sample_rate = st.sidebar.slider("Sample Rate (Hz)", 100, 5000, 1000)

st.sidebar.header("Noise Parameters")
noise_type = st.sidebar.selectbox("Noise Type", ["gaussian", "uniform"])
noise_level = st.sidebar.slider("Noise Level", 0.0, 1.0, 0.1)

# Generate original signal
generator = SignalGenerator(signal_type, frequency, amplitude, duration, sample_rate)
original_signal = generator.generate()
time = generator.get_time_axis()

# Add noise
noise_adder = NoiseAdder(noise_type, noise_level)
noisy_signal = noise_adder.add_noise(original_signal)

# Evaluate
evaluator = SignalEvaluator(original_signal, noisy_signal)
evaluator.evaluate()
difference_signal = original_signal - noisy_signal
metrics = evaluator.get_report()

# Plot
st.subheader("Generated Signal Visualization")
fig, ax = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
ax[0].plot(time, original_signal, label="Original Signal")
ax[0].set_ylabel("Amplitude")
ax[0].set_title("Original Signal")
ax[0].legend()

ax[1].plot(time, noisy_signal, label="Noisy Signal", color='orange')
ax[1].set_ylabel("Amplitude")
ax[1].set_title("Noisy Signal")
ax[1].legend()

ax[2].plot(time, difference_signal, label="Difference", color='red')
ax[2].set_xlabel("Time (s)")
ax[2].set_ylabel("Amplitude")
ax[2].set_title("Difference (Original - Noisy)")
ax[2].legend()

st.pyplot(fig)

# Evaluation Report
st.subheader("Evaluation Report")
st.write(metrics)


