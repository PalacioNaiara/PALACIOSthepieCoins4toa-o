from mailAutomation import EmailSender

# ⚙️ Datos del remitente
usuario = "programacionnai@gmail.com"
contraseña = "bvjw fvwq zpyz vmxv"  # Contraseña de aplicación

# ✉️ Crear objeto y enviar
correo = EmailSender(usuario, contraseña)
correo.enviar_mail(
    destinatario="programacionnai@gmail.com",
    asunto="Prueba desde Python en ProA La Falda",
    mensaje="Hola! Este es un mail de prueba enviado desde un programa en Python 🐍 dia 5/11"
)
