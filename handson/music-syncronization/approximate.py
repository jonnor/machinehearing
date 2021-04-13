
import math

def next_power_of_2(x):
    return 2**(math.ceil(math.log(x, 2)))

def params_for_fps(fps=30, sr=16000):

    frame_seconds=1.0/fps
    frame_hop = round(frame_seconds*sr) # in samples
    frame_fft = next_power_of_2(2*frame_hop)
    rel_error = (frame_hop-(frame_seconds*sr))/frame_hop
    
    return frame_hop, frame_fft, rel_error


seconds = 10*60
fps = 15
sr = 16000
frame_hop, frame_fft, frame_err = params_for_fps(fps=fps, sr=sr)
print(f"Frame timestep error {frame_err*100:.2f} %")
drift = frame_err * seconds
print(f"Drift over {seconds} seconds: {drift:.2f} seconds. {drift*fps:.2f} frames")
