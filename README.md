# Django Video Downloader

A simple Django web application that allows users to download videos from various platforms (YouTube, Vimeo, Twitter, etc.). This project utilizes **yt-dlp**, a powerful fork of **youtube-dl**, to download videos from supported sites.

## Features

- Download videos from multiple platforms such as YouTube, Vimeo, Twitter, etc.
- Supports downloading in the best available quality.
- Provides download links after video is downloaded.
- Written in Python using Django.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python (>= 3.6)
- pip (Python package installer)

### Install Python dependencies

To set up the project and install dependencies, follow these steps:

1. **Clone the repository** or download the code.
2. **Navigate to your project directory**.

    ```bash
    cd your_project_directory
    ```

3. **Create a virtual environment** (recommended):

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment**:

    - On Windows:
        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

    

    ```bash
    pip install django yt-dlp
    ```

Run migrations to set up the database:
    python manage.py migrate


Start the development server:
    python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser.
    ```

Contributing
Feel free to fork the project and submit pull requests. Contributions are welcome to add support for additional platforms or enhance the UI/UX.
