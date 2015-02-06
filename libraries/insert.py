from sqlalchemy.sql import text

event = text(
    "INSERT INTO events "
    "(user_id, title, location, event_datetime, info) "
    "VALUES "
    "(:user_id, :title, :location, :event_datetime, "
    "COLUMN_CREATE('description', :description AS CHAR));"
)

newuser = text(
    "INSERT INTO users "
    "(id, email, pbkdf2, emailverified, info) "
    "VALUES "
    "(:username, :email, :pbkdf2, 0, "
    "COLUMN_CREATE('avatar', NULL AS CHAR));"
)

avatar = text(
    "UPDATE users SET "
    "info = COLUMN_ADD(info, "
    "'usecustomavatar', :usecustomavatar AS INTEGER, "
    "'customavatarurl', :customavatarurl AS CHAR"
    ") "
    "WHERE id=:username"
    ";"
)

contactemail = text(
    "UPDATE users SET "
    "info = COLUMN_ADD(info, "
    "'contactemail', :contactemail AS CHAR, "
    "'pgpmirror', :pgpmirror AS CHAR,"
    "'pgpfingerprint', :pgpfingerprint AS CHAR"
    ") "
    "WHERE id=:username"
    ";"
)

github = text(
    "UPDATE users SET "
    "info = COLUMN_ADD(info, "
    "'github', :githubname AS CHAR"
    ") "
    "WHERE id=:username"
    ";"
)

twitter = text(
    "UPDATE users SET "
    "info = COLUMN_ADD(info, "
    "'twitter', :twittername AS CHAR"
    ") "
    "WHERE id=:username"
    ";"
)

location = text(
    "UPDATE users SET "
    "info = COLUMN_ADD(info, "
    "'location', :location AS CHAR"
    ") "
    "WHERE id=:username"
    ";"
)

website = text(
    "UPDATE users SET "
    "info = COLUMN_ADD(info, "
    "'website', :websiteurl AS CHAR"
    ") "
    "WHERE id=:username"
    ";"
)

name = text(
    "UPDATE users SET "
    "info = COLUMN_ADD(info, "
    "'name', :name AS CHAR"
    ") "
    "WHERE id=:username"
    ";"
)

imgoodat = text(
    "UPDATE users SET "
    "info = COLUMN_ADD(info, "
    "'imgoodat', :description AS CHAR"
    ") "
    "WHERE id=:username"
    ";"
)

icareabout = text(
    "UPDATE users SET "
    "info = COLUMN_ADD(info, "
    "'icareabout', :description AS CHAR"
    ") "
    "WHERE id=:username"
    ";"
)

contactme = text(
    "UPDATE users SET "
    "info = COLUMN_ADD(info, "
    "'contactme', :description AS CHAR"
    ") "
    "WHERE id=:username"
    ";"
)
