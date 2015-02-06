from sqlalchemy.sql import text

event = text(
    "INSERT INTO events "
    "(user_id, title, location, event_datetime, info) "
    "VALUES "
    "(:user_id, :title, :location, :event_datetime, "
    "COLUMN_CREATE('description', :description AS CHAR));"
)
