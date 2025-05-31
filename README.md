# AI-Powered Gesture Equation Solver

An innovative real-time mathematical equation solver that uses hand gesture recognition and artificial intelligence to solve mathematical problems through intuitive hand movements.

## 🌟 Features

- **Real-time Gesture Recognition**: Detect and interpret hand gestures using computer vision
- **AI-Powered Equation Solving**: Leverage advanced AI models to solve mathematical equations
- **Interactive Interface**: Draw equations in the air using hand gestures
- **Multi-format Support**: Solve various types of mathematical equations (arithmetic, algebraic, etc.)
- **Live Feedback**: Real-time visual feedback and equation display

## 🚀 Technologies Used

- **Python**: Core programming language
- **OpenCV**: Computer vision and image processing
- **MediaPipe**: Hand tracking and gesture recognition
- **TensorFlow/PyTorch**: Deep learning framework for AI model
- **NumPy**: Numerical computations
- **Matplotlib**: Visualization and plotting
- **Streamlit/Tkinter**: User interface (if applicable)

## 📋 Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.8 or higher
- Webcam or camera device

## 🎯 How to Use

1. **Start the Application**: Run the main script to launch the gesture recognition system
   ```
   streamlit run main.py
   ```
3. **Position Your Hand**: Place your hand in front of the camera within the detection area
4. **Draw Equations**: Use specific gestures to write mathematical equations:
   - Index finger extended: Drawing mode
   - Fist: Stop drawing
   - Open palm: Clear screen
   - Specific finger combinations: Numbers and operators
5. **Get Solutions**: The AI will automatically recognize and solve the equation
6. **View Results**: See the solution displayed on screen with step-by-step breakdown

## 🔧 Gesture Commands

| Gesture | Action |
|---------|--------|
| Index finger up | Draw/Write numbers |
| Two fingers up | Select operation mode |
| Fist | Stop current action |
| Open palm | Clear screen |
| Thumbs up | Confirm equation |
| Peace sign | Undo last action |

## 🧠 How It Works

1. **Gesture Detection**: Uses MediaPipe to detect hand landmarks and recognize gestures
2. **Equation Formation**: Converts gesture sequences into mathematical expressions
3. **AI Processing**: Employs machine learning models to interpret and solve equations
4. **Result Display**: Shows the equation and solution with visual feedback

## 🎓 Supported Operations

- Basic arithmetic (+, -, ×, ÷)
- Algebraic equations
- Quadratic equations
- Trigonometric functions
- Logarithmic expressions
- Integration and differentiation (basic)

## 🛡️ Troubleshooting

### Common Issues:

1. **Camera not detected**
   - Ensure your camera is connected and working
   - Check camera permissions
   - Try changing camera index in config.py

2. **Poor gesture recognition**
   - Ensure good lighting conditions
   - Keep hand within the detection area
   - Calibrate hand detection sensitivity

3. **Slow performance**
   - Close other applications using camera
   - Reduce video resolution in settings
   - Check system requirements

## 🖼️ Output
![image](https://github.com/user-attachments/assets/577d0a62-1820-4d9c-bfc6-acb0f82c31f5)

<p align="center"><strong>Made with ❤️ and AI magic</strong></p>
