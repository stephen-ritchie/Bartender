from flask import Blueprint, render_template

from ..models import Pump
from ..bartender import Bartender


main_bp = Blueprint('home', __name__)
bt = Bartender()


@main_bp.route('/', methods=['GET', 'POST'])
def debug(pump_pin=None):

    if pump_pin is not None:
        bt._pour(1, pump_pin)

    pumps = Pump.query.all()

    return render_template('debug.html', pumps=pumps)
