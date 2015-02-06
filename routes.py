from controllers.site_root.sitemap import app as sitemap
from controllers.site_root.index import app as index
from controllers.site_root.newuser import app as newuser
from controllers.site_root.login import app as login
from controllers.site_root.logout import app as logout
from controllers.profile.profile import app as profile
from controllers.config.profile.avatar import app as avatar
from controllers.config.profile.contactemail import app as contactemail
from controllers.config.profile.website import app as website
from controllers.config.profile.location import app as location
from controllers.config.profile.twitter import app as twitter
from controllers.config.profile.github import app as github
from controllers.config.profile.name import app as name
from controllers.config.profile.imgoodat import app as imgoodat
from controllers.config.profile.icareabout import app as icareabout
from controllers.config.profile.contactme import app as contactme
from controllers.config.index import app as config_index
from controllers.config.profile.index import app as config_profile_index
from controllers.config.skills.index import app as config_skills_index
from controllers.config.skills.skills_list import app as config_skills_list
from controllers.config.skills.skill import app as config_skill
from controllers.config.account.index import app as config_account_index
from controllers.config.account.email import app as config_account_email
from controllers.config.account.password import app as config_account_password
from controllers.events.new import app as event_new
from controllers.events.event_page import app as event_page
from controllers.events.upcoming import app as upcoming
from controllers.action.accountverify import app as accountverify
from controllers.action.resend import app as resend
from controllers.action.resetpassword import app as resetpassword
from controllers.action.reset import app as reset
from controllers.action.changeemail import app as changeemail
routes = []


routes.append(sitemap)
routes.append(index)
routes.append(newuser)
routes.append(login)
routes.append(logout)
routes.append(avatar)
routes.append(contactemail)
routes.append(website)
routes.append(location)
routes.append(twitter)
routes.append(github)
routes.append(name)
routes.append(config_index)
routes.append(config_profile_index)
routes.append(config_skills_index)
routes.append(config_skills_list)
routes.append(config_skill)
routes.append(config_account_index)
routes.append(config_account_email)
routes.append(config_account_password)
routes.append(event_new)
routes.append(event_page)
routes.append(accountverify)
routes.append(imgoodat)
routes.append(icareabout)
routes.append(contactme)
routes.append(resend)
routes.append(resetpassword)
routes.append(reset)
routes.append(changeemail)
routes.append(profile)
routes.append(upcoming)
