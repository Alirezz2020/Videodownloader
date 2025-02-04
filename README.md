# Django Video Downloader

A simple Django web application that allows users to download videos from various platforms (YouTube, Vimeo, Twitter, etc.). This project utilizes **yt-dlp**, a powerful fork of **youtube-dl**, to download videos from supported sites.

## Features

- Download videos from multiple platforms such as YouTube, Vimeo, Twitter, etc.
- Supports downloading in the best available quality.
- Provides download links after video is downloaded.
- Written in Python using Django.



1. **Clone the repository** or download the code.

2. Clone the Repository: Use the git clone command followed by the repository URL.
    ```bash
    git clone https://github.com/alirezz2020/Videodownloader.git

4. 
5. **Navigate to your project directory**.

    ```bash
    cd path (Videodownloader)
    ```

6. **Create a virtual environment** (recommended):

    ```bash
    python -m venv venv
    ```

7. **Activate the virtual environment**:

    - On Windows:
        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

8. **Install the required dependencies**:

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
