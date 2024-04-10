from ConsultoriaemGestaoEmpresarial import database, app
from ConsultoriaemGestaoEmpresarial.models import Usuario, Foto

with app.app_context():
    database.create_all()