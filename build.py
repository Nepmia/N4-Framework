from template_handler import template_builder, templates_lister
import app
from template_registrator import templates_module, templates_exporter, template_registrator
import os




template_registrator()

template_builder(templates_lister())