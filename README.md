# Facial Recognition Attendance System

This repository contains a Python application that utilizes OpenCV for facial recognition to regulate attendance in college. The system captures student faces, recognizes them, and records their attendance in a user-friendly manner.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Real-time facial recognition using OpenCV.
- Attendance tracking and logging.
- User-friendly interface for managing attendance.
- Easy integration with existing databases for storing attendance records.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- colorama
- pyfiglet
- termcolor
- Face Recognition libraries (e.g., dlib)
- Additional libraries: `pandas`, `matplotlib` (for data analysis and visualization)

You can install the required libraries using pip:

```bash
pip install opencv-python numpy face_recognition pandas matplotlib colorama pyfiglet termcolor
```
## Installation
Clone the repository:

```bash
git clone https://github.com/yourusername/facial-recognition-attendance.git
cd facial-recognition-attendance
```
Install the required libraries:

```bash
pip install -r requirements.txt
```
## Usage
Prepare the dataset:

Create a directory called dataset and add images of students. The images should be named with the student’s name.
Run the attendance system:

```bash
python main.py
```
Follow the on-screen instructions to capture attendance.

## Example
Here's a brief example of how to use the system:

- Ensure your webcam is connected.
- Start the script; it will display a window capturing video.
- It will recognize faces and log attendance automatically.
## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository and submit a pull request.

Fork the repository.
Create your feature branch: git checkout -b feature/YourFeature
Commit your changes: git commit -m 'Add some feature'
Push to the branch: git push origin feature/YourFeature
Open a pull request.
## License
This project is licensed under the MIT License - see the LICENSE file for details.
