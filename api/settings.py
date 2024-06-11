import os
# Default password, cambiar a conveniencia.
if "ADMIN_PASS" not in os.environ.keys():
    ADMIN_PASS = "admin"
ADMIN_PASS = os.environ["ADMIN_PASS"]
