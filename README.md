# ALX WEB-Stack Portfolio: CoinTrack

![CoinTrack Logo](https://github.com/digreatbrian/CoinTrack/blob/mods/app/static/images/favicon.png)

## 📈 Your Personal Finance Tracker 📊


[Google slides](https://docs.google.com/presentation/d/1yYejh0YsBnIrLruQAICkP3kHjIo-5MG16jAJo5MfBKY/pub?start=false&loop=false&delayms=3000)

## Table of Contents

- [Overview](#overview)
- [Technologies-Used](#technologies-used)
- [Structure](structure)
- [Components](components)
- [Features](features)
- [Installation](installation)
- [Usage](usage)
- [Contribution](contribution)
- [Demo](demo)
- [License](license)

## Overview

**CoinTrack** is a powerful and intuitive personal finance tracker designed to help you manage your income and expenses efficiently. With CoinTrack, you can easily keep track of your financial transactions, categorize your spending, and visualize your financial data through insightful charts.The project demonstrates proficiency in backend development and serves as a showcase of Full Stack Software Engineering skills.

## Technologies-Used

The **CoinTrack** project utilizes the following technologies and tools:

- __Flask__: A lightweight web application framework for Python.
- __Object-Oriented Programming (OOP)__: Utilized for efficient code organization and maintainability.
- __Flask-Login__: A Flask extension for managing user sessions and authentication.
- __Jinja2__: The most popular template engine for Python projects.
- __Bootstrap__: A front-end framework for designing responsive and mobile-first websites.
- __HTML__: The standard markup language for creating web pages and applications.
- __CSS__: Cascading Style Sheets for styling HTML elements and enhancing the visual presentation.
- __Git__: A version control system for tracking changes in the project codebase.
- __GitHub__: A platform for hosting and collaborating on Git repositories.

These technologies collectively enable the development of a ``robust`` and ``user-friendly`` web application for managing notes effectively.

## Structure

Here is the Structure of the **CoinTrack** App:

    ~/CoinTrack master                                                                                                    Ruby 3.3.0 root@DESKTOP-QN4FMQ0 23:20:08 ─╮
    ❯ ls                                                                                                                                                           ─╯
       AUTHORS        README.md          app/                config.py         requirements.txt        tests/
       LICENSE        __pycache__/       cointrack.db        migrations/       run.py                  venv/

    ~/CoinTrack master                                                                                                    Ruby 3.3.0 root@DESKTOP-QN4FMQ0 23:20:09 ─╮
    ❯ tree -I venv
    .
    ├── AUTHORS
    ├── LICENSE
    ├── README.md
    ├── __pycache__
    │   └── config.cpython-310.pyc
    ├── app
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-310.pyc
    │   │   ├── forms.cpython-310.pyc
    │   │   ├── models.cpython-310.pyc
    │   │   ├── routes.cpython-310.pyc
    │   │   ├── setup.cpython-310.pyc
    │   │   └── utils.cpython-310.pyc
    │   ├── forms.py
    │   ├── models.py
    │   ├── routes.py
    │   ├── setup.py
    │   ├── static
    │   │   ├── css
    │   │   │   ├── finance_entry.css
    │   │   │   ├── styles-2.css
    │   │   │   ├── styles.css
    │   │   │   └── styles3.css
    │   │   └── images
    │   │       ├── bg1.jpg
    │   │       ├── bg2.jpg
    │   │       ├── bg3.jpg
    │   │       ├── bg4.jpg
    │   │       ├── coinlogo.jpg
    │   │       ├── cointrack.png
    │   │       └── favicon.png
    │   ├── templates
    │   │   ├── add_expense.html
    │   │   ├── add_income.html
    │   │   ├── base.html
    │   │   ├── dashboard.html
    │   │   ├── edit_expense.html
    │   │   ├── edit_income.html
    │   │   ├── expense_list.html
    │   │   ├── income_list.html
    │   │   ├── index.html
    │   │   ├── login.html
    │   │   └── register.html
    │   ├── utils.py
    │   └── views
    │       ├── __init__.py
    │       ├── __pycache__
    │       │   ├── __init__.cpython-310.pyc
    │       │   ├── dashboard.cpython-310.pyc
    │       │   ├── expense.cpython-310.pyc
    │       │   ├── home.cpython-310.pyc
    │       │   ├── income.cpython-310.pyc
    │       │   ├── login.cpython-310.pyc
    │       │   ├── logout.cpython-310.pyc
    │       │   └── register.cpython-310.pyc
    │       ├── dashboard.py
    │       ├── expense.py
    │       ├── home.py
    │       ├── income.py
    │       ├── login.py
    │       ├── logout.py
    │       └── register.py
    ├── cointrack.db
    ├── config.py
    ├── migrations
    │   ├── README
    │   ├── alembic.ini
    │   ├── env.py
    │   └── script.py.mako
    ├── requirements.txt
    ├── run.py
    └── tests
    └── test_app.py

    11 directories, 63 files

## Components

The project consists of the following components:

- `.idea/`: Project-specific settings and configuration files for the IDE.
    - `app/`: Core application code for CoinTrack.
      - `static/`: Contains static files like CSS, JavaScript, and images.
      - `templates/`: HTML templates for rendering views.
      - `views/`: Contains Python files managing the logic for rendering views and handling requests.
  - `migrations/`: Database migration files to keep track of changes in the database schema.
        - `tests/`: Unit and integration tests for ensuring the correctness of the application.
      - `venv/`: Virtual environment for managing dependencies locally.
        - `.gitignore`: Specifies files and directories Git should ignore.
    - `AUTHORS`: A list of contributors to the project.
        - `LICENSE`: The project's license (MIT License).
    - `README.md`: A file describing the project and its usage.
        - `config.py`: Configuration settings for the application.
    - `requirements.txt`: Lists all dependencies needed to run the project.
    - `run.py`: The main script to start the application.
      
## 🚀 Features

- **Easy Transaction Management**: Quickly add, edit, and delete transactions.
- **Custom Categories**: Organize your spending with customizable categories.
- **Insightful Charts**: Visualize your income and expenses with interactive charts.
- **Secure and Private**: Your data is stored securely and is only accessible to you.

---

## 📦 Installation

To install and run CoinTrack locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/digreatbrian/CoinTrack.git
    ```

2. **Install Dependencies**:
    ```bash
    cd CoinTrack
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    ```bash
    FLASK_APP=__init__.py FLASK_ENV=development flask run
    ```

## 📚 Usage

1. **Sign Up**: Create an account to start tracking your finances.
2. **Add Transactions**: Enter your income and expenses to keep track.
3. **Categorize**: Assign categories to your transactions for better organization.
4. **Analyze**: Use the charts and reports to understand your spending habits.

---
## 🖥️ Demo

[![Watch the video](https://img.youtube.com/vi/3DhNhOTZ5JE/0.jpg)](https://youtu.be/3DhNhOTZ5JE?si=Kx4VPZW1Po3fhMkT)
---

## 🌟 Future Enhancements

        🚧This project is still a work in progress!
        
📍There are still many elements that are under development and we wish to implement them into our CoinTrack project. Stay tuned for more updates coming soon. 🍿📺🍿

- **Budget Tracking**: Set and track your monthly budgets.
- **Expense Forecasting**: Predict future expenses based on historical data.
- **Mobile App**: Access your finances on the go with our upcoming mobile app.

---

## 📝 Contribution

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more details.

---

## AUTHORS✒️

1. Misheck Gogo [Github](https://github.com/MisheckGalx) | [Linkedin](https://www.linkedin.com/in/misheckgogo/) | [Twitter](https://twitter.com/kingboris28)

2. Brian Musakwa [Github](https://github.com/digreatbrian) | [Linkedin](https://www.linkedin.com/in/digreatbrian/) | [Twitter](digreatbrian)

3. Brendon Jeje [Github](https://github.com/Brendon45) | [Linkedin](https://www.linkedin.com/in/brendonjeje/) | [Twitter](https://twitter.com/brendon4545)

---
## License

- This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.
  
## ⭐️ Show Your Support

If you like CoinTrack, please give us a ⭐️ on [GitHub](https://github.com/digreatbrian/CoinTrack.git)!
