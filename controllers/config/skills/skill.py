from bottle import Bottle, request, redirect
from sqlalchemy.sql import select
from sqlalchemy import and_, exc
from libraries.template import view
from libraries.authentication import login_required
from libraries.status import Status
from libraries.database import engine as db
from libraries.database import skill_index, user_skills
from libraries.config.skills.forms import Skill as Form
from libraries.forms import Blank as BlankForm
from libraries.session import open_session
from libraries.replace import skill as skill_replace
app = Bottle()


@app.route('/config/skills/skill', method=['GET', 'POST'])
@view('/config/skills/skill.html')
@login_required
def index_page():
    form = Form(request.forms)
    status = Status()
    username = open_session()['u']
    skill_id = int(request.query['id'])
    if request.method == 'POST' and\
       request.query['action'] == 'update':
        if form.validate():
            try:
                conn = db.engine.connect()
                conn.execute(skill_replace,
                             user_id=username,
                             skill_id=skill_id,
                             description=form.description.data)
                conn.close()
                status.success = "Updated skill"
            except exc.SQLAlchemyError as message:
                status.danger = message
    if request.method == 'POST' and\
       request.query['action'] == 'delete':
        blank_form = BlankForm(request.forms)
        if blank_form.validate():
            try:
                conn = db.engine.connect()
                conn.execute(
                    user_skills.delete().where(
                        and_(
                            (user_skills.c.skill_id == skill_id),
                            (user_skills.c.user_id == username))))
                conn.close()
                status.success = "Removed skill"
            except exc.SQLAlchemyError as message:
                status.danger = message
            else:
                return redirect('/config/skills')
    conn = db.engine.connect()
    result = conn.execute(
        select([
            skill_index.c.en,
            user_skills.c.description]).select_from(
                skill_index.outerjoin(
                    user_skills,
                    and_(
                        (skill_index.c.id == user_skills.c.skill_id),
                        (user_skills.c.user_id == username)))).where(
                            skill_index.c.id == skill_id))
    your_skills = conn.execute(
        select([
            skill_index.c.en,
            skill_index.c.id]).select_from(
                user_skills.join(
                    skill_index,
                    user_skills.c.skill_id == skill_index.c.id)).where(
                        user_skills.c.user_id == username))
    conn.close()
    row = result.fetchone()
    form.description.data = row['description']
    return dict(status=status,
                form=form,
                skill_id=skill_id,
                skill_name=row['en'],
                your_skills=your_skills)
