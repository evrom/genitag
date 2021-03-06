from sqlalchemy.sql import text

avatar = text(
    "UPDATE users SET "
    "info = COLUMN_DELETE(info, "
    "'usecustomavatar', "
    "'customavatarurl'"
    ") "
    "WHERE id=:username"
    ";"
)


contactemail = text(
    "UPDATE users SET "
    "info = COLUMN_DELETE(info, "
    "'contactemail', "
    "'pgpmirror', "
    "'pgpfingerprint' "
    ") "
    "WHERE id=:username"
    ";"
)

github = text(
    "UPDATE users SET "
    "info = COLUMN_DELETE(info, "
    "'github'"
    ") "
    "WHERE id=:username"
    ";"
)

twitter = text(
    "UPDATE users SET "
    "info = COLUMN_DELETE(info, "
    "'twitter'"
    ") "
    "WHERE id=:username"
    ";"
)

location = text(
    "UPDATE users SET "
    "info = COLUMN_DELETE(info, "
    "'location'"
    ") "
    "WHERE id=:username"
    ";"
)

website = text(
    "UPDATE users SET "
    "info = COLUMN_DELETE(info, "
    "'website'"
    ") "
    "WHERE id=:username"
    ";"
)

name = text(
    "UPDATE users SET "
    "info = COLUMN_DELETE(info, "
    "'name'"
    ") "
    "WHERE id=:username"
    ";"
)

imgoodat = text(
    "UPDATE users SET "
    "info = COLUMN_DELETE(info, "
    "'imgoodat'"
    ") "
    "WHERE id=:username"
    ";"
)

icareabout = text(
    "UPDATE users SET "
    "info = COLUMN_DELETE(info, "
    "'icareabout'"
    ") "
    "WHERE id=:username"
    ";"
)

contactme = text(
    "UPDATE users SET "
    "info = COLUMN_DELETE(info, "
    "'contactme'"
    ") "
    "WHERE id=:username"
    ";"
)
