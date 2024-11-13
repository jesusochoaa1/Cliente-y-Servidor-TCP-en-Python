import socket
import logging

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ClienteTCP:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.socket_cliente = None

    def conectar(self):
        """Establece la conexión con el servidor."""
        try:
            # Crear el socket TCP
            self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Conectar al servidor
            self.socket_cliente.connect((self.host, self.port))
            logging.info(f"Conectado al servidor en {self.host}:{self.port}")
            
            return True
        except Exception as e:
            logging.error(f"Error al conectar con el servidor: {e}")
            return False

    def enviar_mensaje(self, mensaje):
        """Envía un mensaje al servidor y recibe la respuesta."""
        try:
            # Enviar mensaje
            self.socket_cliente.send(mensaje.encode('utf-8'))
            logging.info(f"Mensaje enviado: {mensaje}")
            
            # Si es mensaje de desconexión, no esperar respuesta
            if mensaje.strip() == "DESCONEXION":
                return None
            
            # Recibir respuesta
            respuesta = self.socket_cliente.recv(1024).decode('utf-8')
            logging.info(f"Respuesta recibida: {respuesta}")
            
            return respuesta
        except Exception as e:
            logging.error(f"Error en la comunicación: {e}")
            return None

    def cerrar(self):
        """Cierra la conexión con el servidor."""
        if self.socket_cliente:
            self.socket_cliente.close()
            logging.info("Conexión cerrada")

    def iniciar_interfaz(self):
        """Inicia la interfaz de usuario para enviar mensajes."""
        if not self.conectar():
            return

        try:
            while True:
                # Solicitar mensaje al usuario
                mensaje = input("\nIngrese mensaje (o 'DESCONEXION' para salir): ")
                
                # Enviar mensaje y recibir respuesta
                respuesta = self.enviar_mensaje(mensaje)
                
                # Si es mensaje de desconexión, terminar
                if mensaje.strip() == "DESCONEXION":
                    break
                
                # Mostrar respuesta
                if respuesta:
                    print(f"Servidor responde: {respuesta}")
                
        except KeyboardInterrupt:
            logging.info("Cliente detenido por el usuario")
        finally:
            self.cerrar()

if __name__ == "__main__":
    cliente = ClienteTCP()
    cliente.iniciar_interfaz()