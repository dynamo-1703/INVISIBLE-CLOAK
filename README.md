# 🧥 Invisible Cloak using Python & OpenCV

> Ever wanted to disappear like Harry Potter? Well... now you can — with code! 🪄

This project uses **Computer Vision** to make a red-colored cloak (or any red cloth) appear invisible in real-time, by replacing it with the captured background. It’s built using Python, OpenCV, and NumPy — and of course, a little bit of *wizardry*.

---

## 🎥 Demo

https://user-uploaded-video-link-here (replace this with your actual video link if uploading to GitHub or YouTube)

---

## 🛠️ Tech Stack
- **Python**
- **OpenCV**
- **NumPy**

---

## 💡 How It Works

1. **Background Capture**:  
   Captures 50 frames to get a stable background using median filtering.

2. **Color Detection**:  
   Detects red color using HSV color space.

3. **Masking & Blending**:  
   - Masks the red region from the frame.  
   - Replaces the masked region with the background using feathered Gaussian masks for smooth edges.

4. **Live Output**:  
   Displays the final frame with red regions replaced by the background — giving the illusion of invisibility!

---

## 📂 How to Run

```bash
git clone https://github.com/your-username/invisible-cloak
cd invisible-cloak
pip install -r requirements.txt
python invisible_cloak.py
