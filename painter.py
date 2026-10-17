import os
import cv2
import numpy as np

# 1. Configuration
IMAGE_NAME = "kali.jpg"
RECORDING_DELAY = 1  # Adjust up to 2 or 5 if you want the recording to feel slower

if not os.path.exists(IMAGE_NAME):
    print(f"Error: '{IMAGE_NAME}' not found in the directory!")
    exit()

# Load target image
target = cv2.imread(IMAGE_NAME)
orig_h, orig_w, _ = target.shape

# Setup window for clean full-screen recording without grey space clipping
window_name = "Hyper-Detailed Live Painting - REC"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 1280, 720)  # Initial window dimensions (fully resizable)

# Extract edges for precise structural mapping
gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 70, 200)

# Initialize blank dark canvas
canvas = np.ones((orig_h, orig_w, 3), dtype=np.uint8) * 12

print("=== Starting Hyper-Detailed 6-Layer Painting Simulation ===")

edge_y, edge_x = np.where(edges > 0)
edge_points = list(zip(edge_x, edge_y))
np.random.shuffle(edge_points)

step_count = 0

# --- LAYER 1: Deep Background Wash ---
print("Layer 1: Deep background color block...")
for _ in range(5000):
    step_count += 1
    x, y = np.random.randint(0, orig_w), np.random.randint(0, orig_h)
    color = target[y, x].tolist()
    
    length = np.random.randint(35, 65)
    angle = np.random.uniform(0, 2 * np.pi)
    x2 = int(np.clip(x + length * np.cos(angle), 0, orig_w - 1))
    y2 = int(np.clip(y + length * np.sin(angle), 0, orig_h - 1))
    
    cv2.line(canvas, (x, y), (x2, y2), color, thickness=np.random.randint(14, 25), lineType=cv2.LINE_AA)
    
    if step_count % 30 == 0:
        cv2.imshow(window_name, canvas)
        if cv2.waitKey(RECORDING_DELAY) & 0xFF == ord('q'): break

# --- LAYER 2: Broad Form & Mass Shapes ---
print("Layer 2: Mass body, hair, and clothing structures...")
for _ in range(8000):
    step_count += 1
    x, y = np.random.randint(0, orig_w), np.random.randint(0, orig_h)
    color = target[y, x].tolist()
    
    length = np.random.randint(18, 35)
    angle = np.random.uniform(0, 2 * np.pi)
    x2 = int(np.clip(x + length * np.cos(angle), 0, orig_w - 1))
    y2 = int(np.clip(y + length * np.sin(angle), 0, orig_h - 1))
    
    cv2.line(canvas, (x, y), (x2, y2), color, thickness=np.random.randint(8, 15), lineType=cv2.LINE_AA)
    
    if step_count % 30 == 0:
        cv2.imshow(window_name, canvas)
        if cv2.waitKey(RECORDING_DELAY) & 0xFF == ord('q'): break

# --- LAYER 3: Mid-Tone Texture Integration ---
print("Layer 3: Mid-tone blended textures...")
for _ in range(10000):
    step_count += 1
    x, y = np.random.randint(0, orig_w), np.random.randint(0, orig_h)
    color = target[y, x].tolist()
    
    length = np.random.randint(8, 20)
    angle = np.random.uniform(0, 2 * np.pi)
    x2 = int(np.clip(x + length * np.cos(angle), 0, orig_w - 1))
    y2 = int(np.clip(y + length * np.sin(angle), 0, orig_h - 1))
    
    cv2.line(canvas, (x, y), (x2, y2), color, thickness=np.random.randint(3, 8), lineType=cv2.LINE_AA)
    
    if step_count % 35 == 0:
        cv2.imshow(window_name, canvas)
        if cv2.waitKey(RECORDING_DELAY) & 0xFF == ord('q'): break

# --- LAYER 4: Edge-Guided Feature Tracing (Eyes, Lips, Ornaments) ---
print("Layer 4: High-precision edge tracing for features...")
edge_stroke_count = min(15000, len(edge_points))
for i in range(edge_stroke_count):
    step_count += 1
    x, y = edge_points[i]
    
    color = target[np.clip(y + np.random.randint(-1, 2), 0, orig_h - 1), 
                   np.clip(x + np.random.randint(-1, 2), 0, orig_w - 1)].tolist()
    
    length = np.random.randint(4, 12)
    angle = np.random.uniform(0, 2 * np.pi)
    x2 = int(np.clip(x + length * np.cos(angle), 0, orig_w - 1))
    y2 = int(np.clip(y + length * np.sin(angle), 0, orig_h - 1))
    
    cv2.line(canvas, (x, y), (x2, y2), color, thickness=np.random.randint(1, 3), lineType=cv2.LINE_AA)
    
    if step_count % 40 == 0:
        cv2.imshow(window_name, canvas)
        if cv2.waitKey(RECORDING_DELAY) & 0xFF == ord('q'): break

# --- LAYER 5: Micro-Details & Highlights ---
print("Layer 5: Micro-details and highlights...")
for _ in range(8000):
    step_count += 1
    x, y = np.random.randint(0, orig_w), np.random.randint(0, orig_h)
    color = target[y, x].tolist()
    
    length = np.random.randint(2, 6)
    angle = np.random.uniform(0, 2 * np.pi)
    x2 = int(np.clip(x + length * np.cos(angle), 0, orig_w - 1))
    y2 = int(np.clip(y + length * np.sin(angle), 0, orig_h - 1))
    
    cv2.line(canvas, (x, y), (x2, y2), color, thickness=1, lineType=cv2.LINE_AA)
    
    if step_count % 50 == 0:
        cv2.imshow(window_name, canvas)
        if cv2.waitKey(RECORDING_DELAY) & 0xFF == ord('q'): break

# --- LAYER 6: Final Pointillism Polish ---
print("Layer 6: Final pointillism pixel blending...")
for _ in range(8000):
    step_count += 1
    x, y = np.random.randint(0, orig_w), np.random.randint(0, orig_h)
    color = target[y, x].tolist()
    cv2.circle(canvas, (x, y), radius=1, color=color, thickness=-1, lineType=cv2.LINE_AA)
    
    if step_count % 60 == 0:
        cv2.imshow(window_name, canvas)
        if cv2.waitKey(RECORDING_DELAY) & 0xFF == ord('q'): break

print("Hyper-detailed masterpiece fully rendered!")
cv2.imwrite("final_hyper_detailed.jpg", canvas)

# Keep final view open
cv2.imshow(window_name, canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()