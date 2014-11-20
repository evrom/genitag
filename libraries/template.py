import functools
from bottle import request
import jinja2
import os
from libraries.session import open_session


file_directory = os.path.dirname(__file__)
template_directory = os.path.join(file_directory, '../templates/')

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_directory),
    autoescape=True,
)

# view = functools.partial(jinja2_view, template_lookup=[filename])


def render_template(template_name, **kwargs):
    template = env.get_or_select_template(template_name)
    try:
        session = open_session(request)
    except:
        session = None
    context = kwargs
    context['session'] = session
    return template.render(context)


def view(template_name):
    def decorator(view_func):
        @functools.wraps(view_func)
        def wrapper(*args, **kwargs):
            response = view_func(*args, **kwargs)

            if isinstance(response, dict):
                template = env.get_or_select_template(template_name)
                try:
                    session = open_session()
                except:
                    session = None
                context = dict(**response)
                context['session'] = session
                return template.render(context)
            else:
                return response

        return wrapper

    return decorator
