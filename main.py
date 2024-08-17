import yagmail
email_salida = "" #desde el correo donde se va a enviar
contrasena = "" #contrasñea de aplicacion generada para este uso, en myaccount.google.com

# Inicializar la conexión SMTP
yag = yagmail.SMTP(user=email_salida, password=contrasena)
# Lista de destinatarios
destinatarios = [''] #añadir los correos electronicos a los que les va a llegar el mail.

# Asunto del correo
asunto = '¡BIENVENIDO!👨‍💻👩‍💻'

# Contenido HTML del correo
cuerpo_html = """
<html>
<head>
<style>
body{background-color: #adff2f; color: #ffffff; font-family: Arial, sans-serif;} h1 {color: #000000;}</style>
</head>
<body>
<h1>BUENAS!💻</h1>
<p>Estimado inter-navegador de github.</p>
<p>Te doy la bienvenida al algoritmo de envio de mail mediante yagmail<p>
</body>
</html>
"""

try:
    # Inicializar la conexión SMTP
    yag = yagmail.SMTP(user=email_salida, password=contrasena)

    # Envío del correo
    yag.send(destinatarios, asunto, cuerpo_html)

    print("Correo enviado exitosamente")

except Exception as e:
    print(f"Error al enviar el correo: {e}")

finally:
    # Cerrar la conexión SMTP
    if 'yag' in locals():
        yag.close()