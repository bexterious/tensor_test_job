# tensor_test_job
Этот репозиторий — является тестовым заданием IT-компании "Тензор": https://tensor.ru/. Репозиторий был создан с использованием шаблона PageObject с Selenium и PyTest (Python).

Подготовка к запуску:

Скопируйте репозиторий на свой компьютер.

Если вы используете PyCharm, он автоматически запрашивает установку необходимых библиотек.

Если нет - установите требуемые библиотеки в файле requirements.txt.

Измените следующие данные:

В Config/config.py измените путь на (актуальный для вашей ОС и версии вашего браузера) chromedriver и/или geckodriver

для macOS: CHROME_EXECUTABLE_PATH = "/path...to/chromedriver"

для Windows: CHROME_EXECUTABLE_PATH = "C:\path...to\chromedriver.exe"

Чтобы НАЧАТЬ тест:

для запуска всех тестов команда:

для macOS: pytest Tests/* or pytest Tests

для Windows: pytest Tests

Для запуска всех тестов и регистрации результатов в формате html:

for macOS: pytest Tests/* -v --html=./hubSpot.html

for Windows: pytest Tests -v --html=./hubSpot.html

Для запуска одного набора тестов:

pytest Tests/test_File_Name.py
