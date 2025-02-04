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

    If you don't have a `requirements.txt`, manually install the dependencies:

    ```bash
    pip install django yt-dlp
    ```

## Setup

### 1. Create the Django Project and App

- Run the following command to create a Django project:

    ```bash
    django-admin startproject video_downloader
    cd video_downloader
    python manage.py startapp downloader
    ```

### 2. Configure Static and Media Directories

In the `settings.py` of your Django project:

- Set the `STATIC_URL` and `MEDIA_URL` variables for serving static and media files.

```python
import os

STATIC_URL = '/static/'

MEDIA_URL = '/downloads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'downloads')
