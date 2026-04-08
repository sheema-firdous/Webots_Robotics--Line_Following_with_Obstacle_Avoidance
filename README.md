# 🤖 Line Follower Robot with Obstacle Avoidance (Webots Simulation)

This project simulates an intelligent mobile robot in Webots that follows a black line on a white surface and avoids obstacles using proximity sensors.

---

## 📌 Features

- **Line Following**: Uses ground sensors to detect and follow a black line.
- **Obstacle Avoidance**: Uses 8 distance sensors (`ps0` to `ps7`) to detect and avoid obstacles dynamically.
- **Behavior Switching**: Switches between line-following and obstacle-avoidance modes based on sensor input.
- **Stateful Avoidance**: Multi-step obstacle avoidance maneuver (diagonal right → forward → diagonal left).

---

## 🚀 Implementation Specifications

- [Webots](https://cyberbotics.com/) Simulator
- Python Controller (Webots API)

---


---

## 🧠 How It Works

### 🖤 Line Following Logic
- Uses two ground sensors (`gs0` and `gs2`).
- Sensor readings are used to detect whether the sensor is on black (line) or white (background).
- Based on the readings:
  - **Both black** → move forward.
  - **Left white, Right black** → turn right.
  - **Left black, Right white** → turn left.
  - **Both white** → slow forward to relocate the line.

### 🧱 Obstacle Avoidance Logic
- Uses front-facing distance sensors (`ps0`, `ps1`, `ps2`) to detect obstacles.
- When an obstacle is detected:
  - Performs a three-step maneuver:
    1. Diagonal right
    2. Straight forward
    3. Diagonal left
- After clearing the obstacle, resumes line following.

---

## 🧪 How to Run

1. **Open Webots**, and load the project directory.
2. Navigate to the world file under `worlds/` and open it.
3. Run the simulation using the green play button ▶️.
4. You will see the robot follow the line and avoid obstacles as it navigates.

---

## 🛠️ Customization

- **Line Shape**: You can modify the path in the `.wbt` world file.
- **Obstacle Placement**: Drag and drop new obstacles in Webots GUI.
- **Sensor Thresholds**: Tune sensor thresholds in `my_controller.py` for better performance.

---

## 👩‍💻 Developers Information

Developed by **[Sheema Firdous](https://www.linkedin.com/in/sheema-firdous-67b9b8181/)**  
as a part of **Cognitive Systems and Robotics** module assessment  at **[Sheffield Hallam University](https://www.shu.ac.uk/)**

Supervised by [Dr. Samuele Vinanzi](https://www.linkedin.com/in/samuelevinanzi/)

The implemented project demonstrates the practical application of Reinforcement Learning (Q-learning) in autonomous robotics using Webots and Python.
