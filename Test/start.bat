cd ..
call .\venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt

cd Test
python .\manage.py migrate
python .\manage.py runserver