# Django Interactive AI Quiz App

A dynamic, web-based quiz application built with Django that leverages AI to generate interactive quizzes. This application allows users to test their knowledge on various topics with questions generated in real-time or pre-curated by administrators.

# Live version of the quiz app: https://felixyustian.pythonanywhere.com/

## 🚀 Features

* **AI-Powered Question Generation**: Automatically generate quiz questions and answers based on topics or uploaded content using AI (e.g., OpenAI/LLM integration).
* **Interactive Quiz Interface**: User-friendly interface for taking quizzes with immediate feedback.
* **User Authentication**: Secure signup, login, and profile management for tracking user progress.
* **Score Tracking & Leaderboard**: Save quiz results and compare scores with other users.
* **Admin Dashboard**: comprehensive backend for managing users, quizzes, and reviewing AI-generated content.
* **Responsive Design**: Fully functional on desktop and mobile devices.

## 🛠️ Technology Stack

* **Backend**: Django (Python)
* **Database**: SQLite (default) / PostgreSQL
* **AI Integration**: OpenAI API (or similar LLM provider)
* **Frontend**: HTML5, CSS3, JavaScript, Bootstrap/Tailwind

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
* [Python 3.8+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)

## 🔧 Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/felixyustian/django_quizapp.git](https://github.com/felixyustian/django_quizapp.git)
    cd django_quizapp
    ```

2.  **Create and activate a virtual environment**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables**
    Create a `.env` file in the root directory and add your configuration:
    ```env
    SECRET_KEY=your_django_secret_key
    DEBUG=True
    OPENAI_API_KEY=your_openai_api_key
    ```

5.  **Run Database Migrations**
    ```bash
    python manage.py migrate
    ```

6.  **Create a Superuser (Admin)**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

    Open your browser and navigate to `http://127.0.0.1:8000/`.

## 📖 Usage

1.  **Register/Login**: Create an account to start saving your scores.
2.  **Generate a Quiz**: Navigate to the "New Quiz" section, enter a topic (e.g., "Python Programming"), and let the AI generate questions.
3.  **Take Quiz**: Answer the questions and receive your score instantly.
4.  **View History**: Check your profile to see past quiz performance.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## 📄 License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.
