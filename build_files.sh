# build_files.sh
pip install --root-user-action=ignore -r requirements.txt
python manage.py collectstatic
