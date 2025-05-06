#Blueprint init for a blank template project
from flask import Blueprint

bp = Blueprint(
    'template-project',                    
    __name__,                  
    template_folder='templates',
    static_folder='static'
)

from . import routes       