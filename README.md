# Flask Speech Processing Service

This project demonstrates a Flask application that uses Deepgram for converting speech to text and text back to speech, and Groq for processing and answering natural language queries. The application allows users to upload audio files, which are then processed to extract text, generate an answer to the query contained in the speech, and return the answer as spoken text.

## Installation

To set up the project environment and install dependencies, follow these steps:

1. Ensure you have Python 3.8 or higher installed.
2. Clone this repository to your local machine.
3. Navigate to the project directory and create a virtual environment:

```bash
python3 -m venv venv
```

## Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```

On macOS and Linux:
```bash
source venv/bin/activate
```

## Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Configuration
Before running the application, you need to set up the required environment variables. Create a .env file in the root directory of the project with the following content, replacing the placeholders with your actual API keys:

```plaintext
DG_API_KEY=your_deepgram_api_key
GROQ_API_KEY=your_groq_api_key
```

## Running the Application
To run the Flask application locally, use the following command:

```bash
flask run
```

The application will be available at http://127.0.0.1:8080. You can interact with it by navigating to this URL in your web browser.

## Usage
Access the web interface provided by the Flask application.
Use the form to upload an audio file containing speech. The file should be in WAV format.
Submit the form, and the application will process the audio, converting speech to text, generating an answer using Groq, and then converting this answer back to speech.
The application will return the processed audio as an answer to the query contained in the uploaded audio file.

## Contributing
If you'd like to contribute to the project, please fork the repository and submit a pull request with your proposed changes.

## License
This project is open-sourced under the MIT License.# SpeecApp
