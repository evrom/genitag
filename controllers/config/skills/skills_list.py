from bottle import Bottle
from sqlalchemy.sql import select
from libraries.template import view
from libraries.authentication import login_required
from libraries.status import Status
from libraries.database import engine as db
from libraries.database import skill_index, user_skills
from libraries.session import open_session
app = Bottle()


@app.route('/config/skills/list', method='GET')
@view('/config/skills/list.html')
@login_required
def index_page():
    status = Status()
    username = open_session()['u']
    conn = db.engine.connect()
    your_skills = conn.execute(
        select([
            skill_index.c.en,
            skill_index.c.id]).select_from(
                user_skills.join(
                    skill_index,
                    user_skills.c.skill_id == skill_index.c.id)).where(
                        user_skills.c.user_id == username))
    result = conn.execute(
        select([
            skill_index.c.id,
            skill_index.c.en]))
    conn.close()
    technology = []
    media = []
    language = []
    for row in result:
        if row['id'] >= 1000 and row['id'] < 2000:
            technology.append(row)
        elif row['id'] >= 2000 and row['id'] < 3000:
            media.append(row)
        elif row['id'] >= 3000 and row['id'] < 4000:
            language.append(row)
    return dict(status=status,
                technology=technology,
                media=media,
                language=language,
                your_skills=your_skills)
