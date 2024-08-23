# Multilanguage Invoice Extractor

## Overview
The **Multilanguage Invoice Extractor** is a powerful application designed to automate the process of extracting specific data from invoices in various languages. Utilizing the capabilities of Gemini 1.5 flash and Natural Language Processing (NLP), this tool identifies and retrieves key details from scanned or uploaded invoice images, providing accurate and fast results.

## Features
- **Multi-Language Support**: Supports invoices in multiple languages, ensuring broad usability across different regions.
- **Custom Prompt Query**: Allows users to input specific queries (e.g., "What is the price of idly?") and receive precise answers based on the invoice content.
- **Easy Integration**: Provides seamless integration with Streamlit for an intuitive and interactive user interface.

## Screenshot
Below is a screenshot of the Multilanguage Invoice Extractor in action:

![Multilanguage Invoice Extractor](./Screenshot%202024-08-23%20112457.png)

*In this example, the user queries the price of "idly" from a Tamil invoice, and the app responds with the correct price.*


## Requirements
The application relies on several Python libraries, which are listed in the `requirements.txt` file. Below is a list of the key dependencies:

- `streamlit`
- `python-dotenv`
- `google-generativeai`
- `pyPDF2`
- `chromadb`
- `langchain`

To install the dependencies, run:

```bash
pip install -r requirements.txt
```

## Installation and Setup
## Prerequisites

- Python 3.x installed on your system.
- Ensure that you have pip installed for managing Python packages.
-Set up the environment variables as required by the application.

## Clone the Repository

``` bash 
git clone https://github.com/your-username/multilanguage-invoice-extractor.git
cd multilanguage-invoice-extractor
``` 

## Environment Variables

The application uses environment variables stored in a `.env` file. Ensure that you have a `.env` file with the necessary API keys and configurations.

## Running the Application
Once everything is set up, you can run the application using Streamlit:

``` bash 
streamlit run app.py
```

## Usage
**Upload Invoice Image:** Drag and drop or browse to upload an image of the invoice.
**Input Prompt:** Enter a specific query, such as "What is the price of idly?".
**Get Response:** The application processes the image, extracts the relevant data, and displays the answer to your query.

## Gitignore
The project includes a .gitignore file to exclude unnecessary files from the repository. Key exclusions might include:

-`.env` (to avoid exposing sensitive API keys and configurations)
-`__pycache__/` (Python cache files)
-`*.pyc` (Compiled Python files)
-`.DS_Store` (macOS directory metadata)

Ensure that your `.gitignore` file is appropriately configured to exclude any other files specific to your development environment.

## License
This project is licensed under the Apache License 2.0. See the `LICENSE` file for more details.

## Apache License 2.0 Summary:
- You may use, distribute, and modify the software as long as you include the original copyright and license notice.
- The software is provided "as-is" without warranty of any kind.

## Contribution
Contributions are welcome! Please fork this repository and submit a pull request with your changes.


