### Instructions to Run the Django App

These steps will guide you through setting up and running the Django app that serves the machine learning model for household progress status prediction.

#### Prerequisites:
1. **Python 3.x**: Ensure Python 3.x is installed on your machine. You can check this by running `python --version` in the terminal.
2. **Django**: The app requires Django. Install it using `pip install django`.
3. **Django REST Framework**: The app uses Django REST Framework for creating APIs. Install it with `pip install djangorestframework`.
4. **Required Libraries**: Install additional dependencies like `scikit-learn`, `pandas`, and `numpy`.

#### 1. **Clone the Repository**
If your Django app is hosted on a repository (e.g., GitHub), you can clone it to your local machine:
```bash
git clone https://github.com/jumashafara/rtv_interview.git
```

#### 2. **Navigate to the Project Directory**
Once cloned, navigate to the directory where the Django project is located:
```bash
cd rtv_django_app
```

#### 3. **Create and Activate a Virtual Environment (Optional but Recommended)**
Create a virtual environment to isolate the project’s dependencies:
```bash
python -m venv venv
```
Activate the virtual environment:
- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

#### 4. **Install Required Dependencies**
Install the dependencies from the `requirements.txt` file. This file should include all the necessary packages like Django, Django REST Framework, scikit-learn, etc.:
```bash
pip install -r requirements.txt
```

#### 5. **Set Up the Database**
Run the following command to apply migrations and set up the database:
```bash
python manage.py migrate
```

#### 6. **Run the Django Development Server**
Once the setup is complete, you can start the Django development server:
```bash
python manage.py runserver
```

You should see output indicating that the server is running and accessible at `http://127.0.0.1:8000/`.
