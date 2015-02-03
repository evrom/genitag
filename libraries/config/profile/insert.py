from sqlalchemy.sql import text

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
