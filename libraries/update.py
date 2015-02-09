from sqlalchemy.sql import text

description = text(
    "UPDATE events SET "
    "info = COLUMN_ADD(info, "
    "'description', :description AS CHAR"
    ") "
    "WHERE id=:id AND user_id=:username"
    ";"
)

flags = text(
    "UPDATE events SET "
    "info = COLUMN_ADD(info, "
    "'datetime_changed', :datetime AS INTEGER, "
    "'location_changed', :location AS INTEGER, "
    "'canceled', :canceled AS INTEGER"
    ") "
    "WHERE id=:id AND user_id=:username"
    ";"
)
