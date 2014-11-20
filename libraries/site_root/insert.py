from sqlalchemy.sql import text

newuser = text(
    "INSERT INTO users "
    "(id, email, pbkdf2, emailverified, info) "
    "VALUES "
    "(:username, :email, :pbkdf2, 0, "
    "COLUMN_CREATE('avatar', NULL AS CHAR));"
)
