To run this simple Django App, follow these steps:
1. Ensure you have python 3 and django installed on the machine.  I added the virtual environment (venv) late due to errors when installing venv. Since Django is already installed on my local machine, the virtual environment would never allow me to install django inside the environment.  This causes django import errors when attempting to run the server using the virtual environment.
2. In a terminal, navigate to the mysite directory inside the git repo directory.  If the original repo name was used this will be `DjangoWebApp/mysite`.
3. To run the server, type the command `python3 manage.py runserver`
4. You will see the server start and display messaging in the terminal.  The default port is 8000, but it won't hurt to verify your setup is using the same port in the server's output.
5. Open a browser.
6. Enter `127.0.0.1:8000/polls/` to see the default message "Hello World!"
7. A custom message can be displayed by adding a path parameter to the URL. An example is `127.0.0.1:8000/polls/Mars`. This will display "Hello Mars!"
