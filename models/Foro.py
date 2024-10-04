from datetime import datetime

##modelo de objeto foro
class ForoModel:
    def __init__(self, data):
        self.idUsuario = data.get('idUsuario', '')
        self.titulo = data.get('titulo', '')
        self.contenido = data.get('contenido', '')
        self.fechaCreacion = data.get('fechaCreacion', '')
        self.categoria = data.get('categoria', '') ## Ej: "salud", "producción", "general"
        self.Interaciones = data.get('Interaciones', {})
        self.create_at = data.get('create_at', datetime.now())
        self.update_at = data.get('update_at', datetime.now())


###"Interaciones": [
#        {
#            "idUsuario": "ObjectId", // Referencia al usuario que interactuó
#            "tipoInteraccion": "string", // Ej: "like", "dislike", "reportar"
#            "fecha": "Date"
#          }          
#    ]