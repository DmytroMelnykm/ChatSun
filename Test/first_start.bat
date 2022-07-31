cd ..
python -m venv venv
call .\venv\Scripts\activate.bat
pip install -r requirements.txt

cd Test
python .\manage.py migrate
python .\manage.py createsuperuser
python .\manage.py runserver