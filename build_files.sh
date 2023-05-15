# build_files.sh
pip install --root-user-action=ignore -r requirements.txt
python3.9 manage.py collectstatic