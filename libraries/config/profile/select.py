from sqlalchemy.sql import text

avatar = text(
    "SELECT "
    "COLUMN_GET(info, 'customavatarurl' AS CHAR) AS customavatarurl, "
    "COLUMN_GET(info, 'usecustomavatar' AS INTEGER) AS usecustomavatar, "
    "email AS email "
    "FROM users "
    "WHERE id=:username"
    ";"
)

contactemail = text(
    "SELECT "
    "COLUMN_GET(info, 'contactemail' AS CHAR) as contactemail, "
    "COLUMN_GET(info, 'pgpmirror' AS CHAR) as pgpmirror, "
    "COLUMN_GET(info, 'pgpfingerprint' AS CHAR) as pgpfingerprint "
    "FROM users "
    "WHERE id=:username"
    ";"
)

github = text(
    "SELECT "
    "COLUMN_GET(info, 'github' AS CHAR) as githubname "
    "FROM users "
    "WHERE id=:username"
    ";"
)

twitter = text(
    "SELECT "
    "COLUMN_GET(info, 'twitter' AS CHAR) as twittername "
    "FROM users "
    "WHERE id=:username"
    ";"
)

location = text(
    "SELECT "
    "COLUMN_GET(info, 'location' AS CHAR) as location "
    "FROM users "
    "WHERE id=:username"
    ";"
)

website = text(
    "SELECT "
    "COLUMN_GET(info, 'website' AS CHAR) as websiteurl "
    "FROM users "
    "WHERE id=:username"
    ";"
)

name = text(
    "SELECT "
    "COLUMN_GET(info, 'name' AS CHAR) as name "
    "FROM users "
    "WHERE id=:username"
    ";"
)

imgoodat = text(
    "SELECT "
    "COLUMN_GET(info, 'imgoodat' AS CHAR) as description "
    "FROM users "
    "WHERE id=:username"
    ";"
)

icareabout = text(
    "SELECT "
    "COLUMN_GET(info, 'icareabout' AS CHAR) as description "
    "FROM users "
    "WHERE id=:username"
    ";"
)

contactme = text(
    "SELECT "
    "COLUMN_GET(info, 'contactme' AS CHAR) as description "
    "FROM users "
    "WHERE id=:username"
    ";"
)

profile = text(
    "SELECT "
    "COLUMN_GET(info, 'contactemail' AS CHAR) as contactemail, "
    "COLUMN_GET(info, 'imgoodat' AS CHAR) as imgoodat, "
    "COLUMN_GET(info, 'pgpmirror' AS CHAR) as pgpmirror, "
    "COLUMN_GET(info, 'pgpfingerprint' AS CHAR) as pgpfingerprint, "
    "COLUMN_GET(info, 'customavatarurl' AS CHAR) AS customavatarurl, "
    "COLUMN_GET(info, 'usecustomavatar' AS INTEGER) AS usecustomavatar, "
    "COLUMN_GET(info, 'github' AS CHAR) as githubname, "
    "COLUMN_GET(info, 'location' AS CHAR) as location, "
    "COLUMN_GET(info, 'twitter' AS CHAR) as twittername, "
    "COLUMN_GET(info, 'website' AS CHAR) as websiteurl, "
    "COLUMN_GET(info, 'name' AS CHAR) as name, "
    "email AS email "
    "FROM users "
    "WHERE id=:username"
    ";"
)
