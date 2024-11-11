<h1>Automated Email Python</h1>

<p><strong>Descripción:</strong> Este script de Python utiliza la librería <code>yagmail</code> para enviar correos electrónicos a través de una cuenta de Gmail. Está diseñado para ser una solución sencilla y rápida para automatizar el envío de correos electrónicos personalizados, como una bienvenida o una notificación.</p>

<h2>Requisitos</h2>
<ul>
  <li>Python 3</li>
  <li>Librería <code>yagmail</code>: se puede instalar ejecutando <code>pip install yagmail</code></li>
</ul>

<h2>Uso</h2>
<ol>
  <li>Clona el repositorio:
    <pre><code>git clone https://github.com/serranolautaro/automated-email-python.git</code></pre>
  </li>
  <li>Abre el archivo Python en tu editor de código preferido.</li>
  <li>Configura las variables:
    <ul>
      <li><code>email_salida</code>: Ingresa la dirección de correo desde la que se enviarán los emails.</li>
      <li><code>contrasena</code>: Ingresa la contraseña de la aplicación de Gmail (puedes generarla en <a href="https://myaccount.google.com">myaccount.google.com</a>).</li>
      <li><code>destinatarios</code>: Añade las direcciones de correo de los destinatarios.</li>
    </ul>
  </li>
  <li>Ejecuta el script:
    <pre><code>python nombre_del_archivo.py</code></pre>
  </li>
</ol>

<h2>Detalles del Script</h2>
<p>Este script inicializa una conexión SMTP mediante <code>yagmail</code> y envía un correo HTML a la lista de destinatarios. El mensaje incluye un saludo personalizado y está diseñado con un estilo HTML simple.</p>
<h2>Notas</h2>
<p>Recuerda habilitar la autenticación de dos factores y generar una contraseña de aplicación para mantener la seguridad de tu cuenta de Gmail.</p>

<h2>Contribuciones</h2>
<p>Las contribuciones son bienvenidas. Si deseas mejorar o añadir funcionalidades, realiza un fork del repositorio, realiza los cambios y envía un pull request.</p>
