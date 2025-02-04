echo "Running unit tests for urls..."
python3 manage.py test pokemon.tests.test_urls
echo "Running unit tests for views..."
python3 manage.py test pokemon.tests.test_views
echo "Finished unit tests..."