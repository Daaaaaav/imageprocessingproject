from matplotlib.pyplot import gray
import numpy as np
from scipy.signal import convolve2d
from PIL import Image

def wiener_filter(noisy_image, kernel_size=5, noise_var=25, signal_var=100):
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size * kernel_size)
    blurred_image = convolve2d(noisy_image, kernel, mode='same', boundary='symm')
    noise_est = noise_var
    signal_est = signal_var
    ratio = signal_est / (signal_est + noise_est)
    filtered_image = blurred_image * ratio
    return np.clip(filtered_image, 0, 255).astype(np.uint8)

result = wiener_filter(gray)
output_image = Image.fromarray(result)