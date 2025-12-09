from flask import Blueprint

api_bp = Blueprint('api', __name__)

# 라우트 모듈 import
from . import health, rooms, beacon, system, dashboard
