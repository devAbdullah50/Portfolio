from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["skills"] = [
    {"name": "HTML", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"},
    {"name": "CSS / Tailwind", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg"},
    {"name": "JavaScript", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"},
    {"name": "React.js", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg"},
    {"name": "Node.js", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg"},
    {"name": "Express", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/express/express-original.svg"},
    {"name": "MongoDB", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg"},
    {"name": "Python", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
    {"name": "MySQL", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg"},
    {"name": "C++", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg"},
]


        return context

class About(TemplateView):
    template_name = 'about.html'
class Projects(TemplateView):
    template_name = 'projects.html'
class Services(TemplateView):
    template_name = 'services.html'
class Contact(TemplateView):
    template_name = 'contact.html'