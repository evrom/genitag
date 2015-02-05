from bottle import Bottle
from gravatar import Gravatar
from urllib.parse import urlparse
from sqlalchemy.sql import select
from libraries.database import engine as db
from libraries.database import skill_index, user_skills
from libraries.regex import username_string
from libraries.template import view
from libraries.status import Status
from libraries.profile.select import profile as profile_select
app = Bottle()


@app.route('/profile/<username:re:'+username_string+'>', method='GET')
@view('profile/user.html')
def profile(username):
    status = Status()
    conn = db.engine.connect()
    result = conn.execute(profile_select,
                          username=username)
    your_skills = conn.execute(
        select([
            skill_index.c.en,
            skill_index.c.id,
            user_skills.c.description]).select_from(
                user_skills.join(
                    skill_index,
                    user_skills.c.skill_id == skill_index.c.id)).where(
                        user_skills.c.user_id == username))
    conn.close()
    row = result.fetchone()
    if bool(row['usecustomavatar']):
        avatar_url = row['customavatarurl']+'?size=large'
    else:
        avatar_url = Gravatar(row['email'], size=96).thumb
    pgpmirror_url = urlparse(row['pgpmirror'])
    pgpmirror_netloc = pgpmirror_url.netloc
    result = dict(
        username=username,
        imgoodat=row['imgoodat'],
        icareabout=row['icareabout'],
        contactme=row['contactme'],
        twittername=row['twittername'],
        githubname=row['githubname'],
        pgpmirror=row['pgpmirror'],
        pgpmirror_netloc=pgpmirror_netloc,
        pgpfingerprint=row['pgpfingerprint'],
        avatar_url=avatar_url,
        location=row['location'],
        website_url=row['websiteurl'],
        hide_email=bool(row['hide']),
        contactemail=row['contactemail'],
        name=row['name']
    )
    return dict(status=status,
                result=result,
                your_skills=your_skills)
