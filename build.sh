pip install -r requirements.txt
python3.9 manage.py migrate
mkdir -p staticfiles/dist
python3.9 manage.py collectstatic --noinput