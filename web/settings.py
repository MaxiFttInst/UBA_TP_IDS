import os
if "ADMIN_PASS" not in os.environ.keys():
    API_URL = "https://posadabyteados.pythonanywhere.com"
else:
    API_URL = os.environ["API_URL"]
