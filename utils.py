import jinja2
import os

# define the template dir and jinja2 environment
cur_dir = os.path.dirname(__file__)
template_dir = os.path.join(cur_dir, 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

# covenient rendering templates
def render_str(template, params):
    t = jinja_env.get_template(template)
    return t.render(params)
    