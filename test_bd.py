from app import app, db
from models import Unit

with app.app_context():
    # Crear 15 unidades
    units = [
        Unit(modelo='Modelo A', año=2015, matricula='ABC123', dueño_id=1),
        Unit(modelo='Modelo B', año=2016, matricula='DEF456', dueño_id=2),
        Unit(modelo='Modelo C', año=2017, matricula='GHI789', dueño_id=3),
        Unit(modelo='Modelo D', año=2018, matricula='JKL012', dueño_id=4),
        Unit(modelo='Modelo E', año=2019, matricula='MNO345', dueño_id=5),
        Unit(modelo='Modelo F', año=2020, matricula='PQR678', dueño_id=6),
        Unit(modelo='Modelo G', año=2021, matricula='STU901', dueño_id=7),
        Unit(modelo='Modelo H', año=2015, matricula='VWX234', dueño_id=1),
        Unit(modelo='Modelo I', año=2016, matricula='YZA567', dueño_id=2),
        Unit(modelo='Modelo J', año=2017, matricula='BCD890', dueño_id=3),
        Unit(modelo='Modelo K', año=2018, matricula='EFG123', dueño_id=4),
        Unit(modelo='Modelo L', año=2019, matricula='HIJ456', dueño_id=5),
        Unit(modelo='Modelo M', año=2020, matricula='KLM789', dueño_id=6),
        Unit(modelo='Modelo N', año=2021, matricula='NOP012', dueño_id=7),
        Unit(modelo='Modelo O', año=2022, matricula='QRS345', dueño_id=1)
    ]

    # Agregar las unidades a la sesión
    db.session.add_all(units)
    db.session.commit()
    print("15 unidades han sido creadas exitosamente.")
