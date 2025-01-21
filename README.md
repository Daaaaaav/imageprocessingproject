# Image Processing and Recognition

## Overview
This project is a web-based image processing and recognition tool that integrates a Python backend with a frontend developed using HTML, CSS, and JavaScript. It offers a variety of image manipulation and analysis functionalities, making it an accessible tool for educational purposes, research, and practical applications.

The primary goal of this project is to provide users with an intuitive web platform for performing operations such as image filtering, object detection, and feature extraction, without the need for extensive technical knowledge.

## Features
The system offers various image processing functionalities, including:
- **Greyscale Conversion** – Converts color images to grayscale.
- **Negative Transformation** – Inverts pixel values to create a negative effect.
- **Color Manipulation** – Adjusts image colors, hues, and saturation.
- **Flip Operations** – Horizontal and vertical flipping.
- **Translation** – Moves the image in specified directions.
- **Scaling** – Resizes images with upscaling and downscaling options.
- **Rotation** – Rotates images by a user-defined angle.
- **Cropping** – Extracts a specific portion of an image.
- **Image Blending** – Merges two images with adjustable transparency.
- **Brightness & Contrast Adjustments** – Enhances image brightness and contrast.
- **Color Filtering** – Retains or emphasizes specific colors.
- **Border and Padding Addition** – Adds customizable borders to images.
- **Image Overlay** – Places one image over another.

## System Requirements
### Hardware Requirements
- No specific hardware requirements.

### Software Requirements
- Any operating system with a web browser to access the server.
- Required Python libraries:
  - OpenCV
  - NumPy
  - Flask + Flask_CORS
  - Pillow
  - SciPy

## Installation Instructions
1. **Download the Project:**
   - Clone the repository: `git clone https://github.com/Daaaaaav/imageprocessing.git`
   - Alternatively, download the zip and extract it to a folder.

2. **Set Up the Environment:**
   - Install an IDE such as Visual Studio Code.
   - Install the required Python libraries via the terminal:
     ```
     pip install opencv-python numpy flask flask_cors pillow scipy
     ```

3. **Run the Application:**
   - Open the project folder in the IDE.
   - Run `app.py` to start the backend server.
   - Access the web application using the provided server link.

## User Interface Overview
The web application features a simple and user-friendly interface, with the following key elements:
- **File Picker Button** – Uploads an image for processing.
- **Operation Selector Dropdown** – Selects one of the available processing options.
- **Process Image Button** – Executes the selected operation and displays the result.

Additional interactive elements such as sliders and extra input fields appear dynamically based on the chosen operation.

## How to Use the System
1. **Access the Website:** Open the application in a web browser.
2. **Upload an Image:** Choose an image file (JPG/PNG).
3. **Select an Operation:** Pick the desired image processing function.
4. **Process the Image:** Click the "Process Image" button.
5. **View Results:** The processed image will be displayed on the screen.

## Our Contribution
Each team member contributed to various aspects of the project:
- **Davina:** Basic image operations such as RGB adjustment, greyscale conversion, negative transformation, and color manipulation.
- **Marioe:** Image transformations including flipping, diagonal flipping, translation, and scaling.
- **Nava:** Image operations like rotation, cropping, blending, and brightness adjustment.
- **Ragil:** Contrast adjustments, border addition, and applying filters.
- **Emilia:** Advanced filtering techniques and overlay functionalities.

## Project Team
- Marioe Tri Wardhana (001202300166)
- Ragil Maulana Ilyasha (001202300117)
- Davina Ritzky Amarina (001202300039)
- Emilia Adinda Putri Ginting (001202300155)
- Nava Windah Simanjuntak (001202300154)

---
**University:** President University  
**Year:** 2025  

For more information and the latest updates, visit the [GitHub repository](https://github.com/Daaaaaav/imageprocessing).
