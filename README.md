# Face Detection and Alarm System

This project is a real-time face detection system that triggers an alarm and sends an SMS notification when a face is detected. It uses OpenCV for face detection, `playsound` for playing an alarm sound, and Twilio for sending SMS notifications.

## Features

- **Real-time Face Detection**: Detects faces using a webcam feed.
- **Alarm Sound**: Plays an alarm sound when a face is detected.
- **SMS Notification**: Sends an SMS to the owner when a face is detected.
- **Simple and Lightweight**: Easy to set up and run on any system with a webcam.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- `playsound` library
- Twilio account (for SMS functionality)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Afreen-khan1/Face-detection.git
   cd Face-detection
   ```

2. **Install the required libraries**:
   ```bash
   pip install opencv-python playsound twilio
   ```

3. **Set up Twilio**:
   - Create a Twilio account at [Twilio](https://www.twilio.com/).
   - Get your `account_sid`, `auth_token`, and Twilio phone number.
   - Replace the placeholders in the script with your Twilio credentials and phone numbers.

4. **Download the Haar Cascade file**:
   - The `haarcascade_frontalface_default.xml` file is required for face detection. You can download it from the [OpenCV GitHub repository](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml).

5. **Add an alarm sound**:
   - Place an alarm sound file named `alarm_sound.mp3` in the project directory.

## Usage

1. **Run the script**:
   ```bash
   python face_detection.py
   ```

2. **Face Detection**:
   - The webcam feed will open, and the system will start detecting faces.
   - When a face is detected, an alarm sound will play, and an SMS will be sent to the owner.

3. **Exit**:
   - Press `q` to stop the program and close the webcam feed.

## Customization

- **Change the alarm sound**: Replace `alarm_sound.mp3` with your preferred sound file.
- **Modify SMS content**: Edit the `send_sms` function to change the SMS message.
- **Adjust face detection sensitivity**: Modify the `scaleFactor` and `minNeighbors` parameters in the `detectMultiScale` function.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenCV for providing the Haar Cascade classifier.
- Twilio for the SMS API.
- `playsound` library for playing audio files.
  
