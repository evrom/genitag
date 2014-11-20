from bottle import Bottle
from sqlalchemy.sql import select
from libraries.database import engine as db
from libraries.database import skill_index, user_skills
from libraries.template import view
from libraries.authentication import login_required
from libraries.session import open_session
from libraries.status import Status
app = Bottle()


@app.route('/config/skills/', method='GET')
@app.route('/config/skills', method='GET')
@view('/config/skills/index.html')
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
    conn.close()
    return dict(status=status,
                your_skills=your_skills)
