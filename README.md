# 🎨 Oil Painting Simulation Engine (Python & OpenCV)

A Python-based programmatic painting generator that simulates physical brush strokes in real-time, building up complex portraits stroke-by-stroke. Designed specifically for live visualization and smooth screen recording, this project evolves from basic random stroke sampling into a hyper-detailed, 6-layer edge-guided rendering pipeline.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🚀 Project Evolution & Iterative Findings

This project was built iteratively to solve visual clarity, detail degradation, and screen-recording constraints. Below is the breakdown of the changes made and the specific results they unlocked:

### 1. Basic Random Stroke Simulation (Initial Draft)
* **What we did:** Initialized a blank white canvas and looped through random coordinates to draw straight colored lines sampled directly from the target image.
* **Findings:** While it created a cool abstract progression, the output lacked recognizable structure, and facial features (like eyes and mouth) were entirely lost in the random noise.

### 2. Multi-Pass Layering & Recording Speed Control
* **What we did:** Split the rendering loop into sequential passes (coarse background blocks $\rightarrow$ mid-tones $\rightarrow$ fine lines) and added an adjustable frame delay (`cv2.waitKey`).
* **Findings:** This gave the visual progression a natural pacing, allowing the background to anchor first before details formed. However, high-contrast lines were still fuzzy.

### 3. Edge-Guided Feature Tracing (Canny Edge Integration)
* **What we did:** Integrated OpenCV's Canny edge detection algorithm to extract structural outlines (eyes, lips, ornaments, and hair borders) and prioritized micro-strokes directly along those paths.
* **Findings:** This was a breakthrough moment. The core facial features and high-contrast lines suddenly popped out cleanly, making the resulting painting instantly recognizable and aesthetically sharp.

### 4. Full-Screen Window Optimization
* **What we did:** Replaced static windows with dynamic scalable windows using `cv2.WINDOW_NORMAL`.
* **Findings:** Maximizing the window previously left a massive gray side panel. Setting up a resizable window container fixed this completely, enabling clean, borderless video framing ideal for OBS Studio or screen recorders.

### 5. Hyper-Detailed 6-Layer Architecture (Final Version)
* **What we did:** Expanded the engine into **6 distinct structural passes** totaling over **46,000+ precision strokes, lines, and pointillism polish dots**.
* **Findings:** This delivered a dense, rich oil-painting texture with incredible depth, smooth color blending, and razor-sharp focal points without sacrificing real-time rendering performance.

---

## 🛠️ Project Structure

```text
oil-painting/
│
├── venv/        # Python virtual environment (recommended)
├── kali.jpg     # Target input image
├── painter.py   # Main 6-layer hyper-detailed rendering script
└── README.md    # Project documentation
```

## 📦 Installation & Setup

Follow these steps to set up the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/projectavsm/oil-painting.git
cd oil-painting
```

### 2. Create and Activate a Virtual Environment

**Windows (Command Prompt):**

```bash
python -m venv venv
venv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required computer vision and array-processing libraries:

```bash
pip install opencv-python numpy
```

## 💻 Running the Script

Ensure your target image is placed in the root directory and named `kali.jpg`, or modify `IMAGE_NAME` in `painter.py`.

Run the painting script:

```bash
python painter.py
```

### Tips for Screen Recording

- Maximize or resize the OpenCV window when it opens to fit your recording software cleanly.
- Adjust `RECORDING_DELAY` inside `painter.py` (for example, from `1` to `5` or `10`) to slow the stroke generation for cinematic video captures.
- Press `q` anytime to safely interrupt or close the rendering window.

## 📜 License

This project is open-source and available under the MIT License.