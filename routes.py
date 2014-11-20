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
from controllers.config.index import app as config_index
from controllers.config.profile.index import app as config_profile_index
from controllers.config.skills.index import app as config_skills_index
from controllers.config.skills.skills_list import app as config_skills_list
from controllers.config.skills.skill import app as config_skill
from controllers.config.account.index import app as config_account_index
from controllers.config.account.email import app as config_account_email
from controllers.config.account.password import app as config_account_password
from controllers.event.index import app as event_index
from controllers.event.new import app as event_new
from controllers.event.event_page import app as event_page
routes = []

routes.append(sitemap)
routes.append(index)
routes.append(newuser)
routes.append(login)
routes.append(logout)
routes.append(profile)
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
routes.append(event_index)
routes.append(event_new)
routes.append(event_page)
