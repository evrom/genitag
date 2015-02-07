from libraries.regex import username_string
# /
from controllers.site_root.index import index
from controllers.site_root.login import login
from controllers.site_root.logout import logout
from controllers.site_root.newuser import newuser
# /action
from controllers.action.accountverify import accountverify
from controllers.action.changeemail import changeemail
from controllers.action.resend import resend
from controllers.action.reset import reset
from controllers.action.resetpassword import resetpassword
# /config
from controllers.config.index import index as config_index
# /config/account
from controllers.config.account.index import index as config_account_index
from controllers.config.account.password import password \
    as config_account_password
from controllers.config.account.email import email \
    as config_account_email
# /config/profile
from controllers.config.profile.index import index as config_profile_index
from controllers.config.profile.avatar import avatar
from controllers.config.profile.contactemail import contactemail
from controllers.config.profile.contactme import contactme
from controllers.config.profile.github import github
from controllers.config.profile.icareabout import icareabout
from controllers.config.profile.imgoodat import imgoodat
from controllers.config.profile.location import location
from controllers.config.profile.name import name
from controllers.config.profile.twitter import twitter
from controllers.config.profile.website import website
# /config/skills
from controllers.config.skills.index import index as config_skills_index
from controllers.config.skills.skill import skill
from controllers.config.skills.skills_list import skills_list
# /events
from controllers.events.edit import edit as events_edit
from controllers.events.event_page import event_page
from controllers.events.new import new as events_new
from controllers.events.upcoming import upcoming
# /profile
from controllers.profile.profile import profile


def setup_routing(app):
    app.route('/', ['GET'], index)
    app.route('/login', ['GET', 'POST'], login)
    app.route('/exit', ['GET'], logout)
    app.route('/newuser', ['POST', 'GET'], newuser)
    # /action
    app.route('/action/accountverify', ['GET'], accountverify)
    app.route('/action/changeemail', ['GET', 'POST'], changeemail)
    app.route('/action/resend', ['GET', 'POST'], resend)
    app.route('/action/reset', ['GET', 'POST'], reset)
    app.route('/action/resetpassword', ['GET', 'POST'], resetpassword)
    # /config
    app.route('/config', ['GET'], config_index)
    app.route('/config/', ['GET'], config_index)
    # /config/account
    app.route('/config/account', ['GET'], config_account_index)
    app.route('/config/account/', ['GET'], config_account_index)
    app.route('/config/account/password', ['GET', 'POST'],
              config_account_password)
    app.route('/config/account/email', ['GET', 'POST'],
              config_account_email)
    # /config/profile
    app.route('/config/profile', ['GET'], config_profile_index)
    app.route('/config/profile/', ['GET'], config_profile_index)
    app.route('/config/profile/avatar', ['GET', 'POST'], avatar)
    app.route('/config/profile/contactemail', ['GET', 'POST'], contactemail)
    app.route('/config/profile/contactme', ['GET', 'POST'], contactme)
    app.route('/config/profile/github', ['GET', 'POST'], github)
    app.route('/config/profile/icareabout', ['GET', 'POST'], icareabout)
    app.route('/config/profile/imgoodat', ['GET', 'POST'], imgoodat)
    app.route('/config/profile/location', ['GET', 'POST'], location)
    app.route('/config/profile/name', ['GET', 'POST'], name)
    app.route('/config/profile/twitter', ['GET', 'POST'], twitter)
    app.route('/config/profile/website', ['GET', 'POST'], website)
    # /config/skills
    app.route('/config/skills', ['GET'], config_skills_index)
    app.route('/config/skills/', ['GET'], config_skills_index)
    app.route('/config/skills/skill', ['GET', 'POST'], skill)
    app.route('/config/skills/list', ['GET'], skills_list)
    # /events
    app.route('/events/<id:int>/edit/', ['GET', 'POST'], events_edit)
    app.route('/events/<id:int>/<:re>', ['GET'], event_page)
    app.route('/events/<id:int>', ['GET'], event_page)
    app.route('/events/new', ['GET', 'POST'], events_new)
    app.route('/events/upcoming', ['GET'], upcoming)
    # /profile
    app.route('/profile/<username:re:'+username_string+'>',
              ['GET'], profile)
