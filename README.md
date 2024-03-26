# Polls Django App

Welcome to the Polls Django app! This is a beginner-level project aimed at showcasing a basic understanding of the Django framework. This README will guide you through setting up and running the app on your local machine.

## Installation

1. ### Clone the repository

    ```bash
    git clone https://github.com/Mozzie455/polls.git
    ```

2. ### Navigate to the project directory

    ```bash
    cd polls-django-app
    ```

3. ### Create a virtual environment (optional but recommended)

    ```bash
    python -m venv venv
    ```

4. ### Activate the virtual environment

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

5. ### Install the dependencies

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. ### Run database migrations

    ```bash
    python manage.py migrate
    ```

2. ### Create a superuser (admin) account

    ```bash
    python manage.py createsuperuser
    ```

3. ### Start the development server

    ```bash
    python manage.py runserver
    ```

4. ### Access the admin panel

    Open your web browser and go to <http://127.0.0.1:8000/admin>. Log in using the superuser account created earlier.

5. ### Interact with the Polls app

- Visit <http://127.0.0.1:8000/polls> to view the list of available polls and vote on them.
- Navigate to specific poll detail pages by clicking on the respective poll links.
- Admins can manage polls and choices through the admin panel.

## Structure

- mysite/: The main Django app directory.
- **mysite/polls/models.py**: Defines the database models for Polls and Choices.
- **mysite/polls/views.py**: Contains the view functions for rendering templates and handling user requests.
- **mysite/polls/urls.py**: Defines URL patterns for routing requests to the appropriate views.
- **mysite/polls/templates/**: Contains HTML templates for rendering the web pages.
- **mysite/polls/admin.py**: Registers models to be managed via Django's admin interface.
- **mysite/polls/migrations/**: Auto-generated database migration files.
- **mysite/manage.py**: Django's command-line utility for administrative tasks.
- **requirements.txt**: Lists the Python dependencies for the project.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Happy polling! 🗳️🎉
