from sqlalchemy.sql import text

profile = text(
    "SELECT "
    "COLUMN_GET(info, 'imgoodat' AS CHAR) as imgoodat, "
    "COLUMN_GET(info, 'icareabout' AS CHAR) as icareabout, "
    "COLUMN_GET(info, 'contactme' AS CHAR) as contactme, "
    "COLUMN_GET(info, 'contactemail' AS CHAR) as contactemail, "
    "COLUMN_GET(info, 'hide' AS INTEGER) as hide, "
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
