# Text Extraction App

This Flask application extracts text from PDF, DOCX, and DOC files and saves the extracted text to a SQLite database. It also sends an email notification once the text extraction is complete.

## Setup

1. **Create a Virtual Environment:**
    ```bash
    virtualenv venv
    ```

2. **Activate the Virtual Environment:**
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

3. **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application:**
    ```bash
    flask run
    ```

## Testing with Postman

1. Open Postman and set the request method to POST.

2. Set the request URL to `http://127.0.0.1:5000/extract_text`.

3. In the request body, select the raw option and choose JSON from the dropdown.

4. Pass the following JSON input in the request body:
    ```json
    {
        "email": "example@gmail.com",
        "url": "local_path_or_url"
    }
    ```

5. Click on the Send button to test the endpoint.

## For Docker Setup
# Text Extraction App

This Flask application extracts text from PDF, DOCX, and DOC files and saves the extracted text to a SQLite database. It also sends an email notification once the text extraction is complete.

## Setup

1. **Create a Virtual Environment:**
    ```bash
    virtualenv venv
    ```

2. **Activate the Virtual Environment:**
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

3. **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```

## Running with Flask

1. **Run the Application:**
    ```bash
    flask run
    ```

## Testing with Postman

1. Open Postman and set the request method to POST.

2. Set the request URL to `http://127.0.0.1:5000/extract_text`.

3. In the request body, select the raw option and choose JSON from the dropdown.

4. Pass the following JSON input in the request body:
    ```json
    {
        "email": "example@gmail.com",
        "url": "local_path_or_url"
    }
    ```

5. Click on the Send button to test the endpoint.


## Running with Docker

1. **Build the Docker Image:**
    ```bash
    docker build -t docker_image_name .
    ```

2. **Run the Docker Container:**
    ```bash
    docker run -p 5000:5000 docker_image_name
    ```

3. Open Postman and set the request URL to `http://localhost:5000/extract_text`.

4. Follow steps 3-5 from the "Testing with Postman" section to test the endpoint.
