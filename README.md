# Streamlit Image Enhancer

This project is a Streamlit application that enhances images using various image processing techniques. The main functionalities include histogram equalization, CLAHE (Contrast Limited Adaptive Histogram Equalization), and image sharpening.

## Project Structure

```
streamlit_image_enhancer
├── enhance.py          # Main functionality for processing images
├── requirements.txt    # Dependencies required for the project
└── README.md           # Documentation for the project
```

## Installation

To run this project, you need to have Python installed on your machine. Follow these steps to set up the project:

1. Clone the repository or download the project files.
2. Navigate to the project directory in your terminal.
3. Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you have your input images ready in the specified input folder.
2. Run the Streamlit application with the following command:

   ```
   streamlit run enhance.py
   ```

3. Open your web browser and go to the URL provided in the terminal (usually `http://localhost:8501`).

4. Follow the on-screen instructions to upload images and apply the enhancements.

## Features

- **Histogram Equalization**: Improves the contrast of the image.
- **CLAHE**: Applies adaptive histogram equalization to enhance local contrast.
- **Image Sharpening**: Enhances the edges in the image for better clarity.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.