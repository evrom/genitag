from sqlalchemy.sql import text

event = text(
    "SELECT "
    "COLUMN_GET(info, 'description' AS CHAR) as description, "
    "user_id, title, location, event_datetime, timestamp "
    "FROM events "
    "WHERE id=:id;"
)
