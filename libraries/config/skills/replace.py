from sqlalchemy.sql import text

skill = text(
    "REPLACE INTO user_skills "
    "(user_id, skill_id, description) "
    "VALUES "
    "(:user_id, :skill_id, :description);"
)
