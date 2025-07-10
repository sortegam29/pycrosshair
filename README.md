# Crosshair Overlay for FPS Gaming

A simple and lightweight crosshair overlay designed to help FPS players align their aim precisely by displaying a centered visual marker on the screen.

---

## 🔧 Features

- Always-on-top transparent window
- Centered crosshair indicator
- No interference with mouse or keyboard input
- Lightweight and easy to run
- Works across games and applications

---

## ⚙️ How It Works

This tool uses **PyQt5** to create a borderless, frameless, and transparent window that sits on top of all other windows. The crosshair is drawn using PyQt's built-in drawing functions and stays at the center of your primary display.

It leverages `QtCore.Qt.WindowTransparentForInput` to ensure that it never captures mouse or keyboard events — making it completely invisible to user interaction, while still being visible as a reference point.

---

## 📦 Requirements

- Python 3.x
- PyQt5

Install dependencies with:

```bash
pip install -r requirements.txt
```
---

## ▶️ Running the App

To run the overlay:

```bash
python crosshair.py
```
To close the app, press ESC.

---

## 🛠️ Future Improvements

- Add configuration file for custom colors, size, offset
- Add multiple crosshair styles (dot, circle, custom image)
- Support multi-monitor setups
- Option to toggle visibility with hotkey
- Auto-start option in settings
- Build as standalone .exe for Windows

---

## 📄 License

This project is licensed under the MIT License . Feel free to fork, modify, and redistribute!
