class Persona:
    def _init_(self, nombres, apellidos, tipo_doc, documento, telefono, correo, genero, carrera):
        self.nombres = nombres
        self.apellidos = apellidos
        self.tipo_doc = tipo_doc
        self.documento = documento
        self.telefono = telefono
        self.correo = correo
        self.genero = genero
        self.carrera = carrera
    
    def formato_doc(self):
        return{
            'nombres': self.nombres,
            'apellidos': self.apellidos,
            'tipo_doc': self.tipo_doc,
            'documento': self.documento,
            'telefono': self.telefono,
            'correo': self.correo,
            'genero': self.genero,
            'carrera': self.carrera,
        }
