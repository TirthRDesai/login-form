# build_files.sh
python manage.py makemigrations
python manage.py collectstatic
pip install -r requirements.txt
python3 manage.py runserver