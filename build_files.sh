# build_files.sh
pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic
