import socket
import logging

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ServidorTCP:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.socket_servidor = None

    def iniciar(self):
        """Inicia el servidor TCP y escucha conexiones entrantes."""
        try:
            # Crear el socket TCP
            self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Permite reutilizar la dirección
            self.socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # Vincular el socket al host y puerto
            self.socket_servidor.bind((self.host, self.port))
            
            # Escuchar conexiones entrantes
            self.socket_servidor.listen(1)
            logging.info(f"Servidor escuchando en {self.host}:{self.port}")
            
            self.aceptar_conexiones()
            
        except Exception as e:
            logging.error(f"Error al iniciar el servidor: {e}")
            self.cerrar()

    def aceptar_conexiones(self):
        """Acepta conexiones entrantes y maneja la comunicación con los clientes."""
        while True:
            try:
                # Aceptar nueva conexión
                socket_cliente, direccion = self.socket_servidor.accept()
                logging.info(f"Nueva conexión aceptada desde {direccion}")
                
                self.manejar_cliente(socket_cliente)
                
            except Exception as e:
                logging.error(f"Error al aceptar conexión: {e}")
                break

    def manejar_cliente(self, socket_cliente):
        """Maneja la comunicación con un cliente específico."""
        while True:
            try:
                # Recibir mensaje del cliente
                mensaje = socket_cliente.recv(1024).decode('utf-8')
                
                if not mensaje:
                    break
                
                logging.info(f"Mensaje recibido: {mensaje}")
                
                # Verificar si es mensaje de desconexión
                if mensaje.strip() == "DESCONEXION":
                    logging.info("Cliente solicitó desconexión")
                    break
                
                # Enviar respuesta en mayúsculas
                respuesta = mensaje.upper()
                socket_cliente.send(respuesta.encode('utf-8'))
                logging.info(f"Respuesta enviada: {respuesta}")
                
            except Exception as e:
                logging.error(f"Error en la comunicación con el cliente: {e}")
                break
        
        # Cerrar conexión con el cliente
        socket_cliente.close()
        logging.info("Conexión con el cliente cerrada")

    def cerrar(self):
        """Cierra el socket del servidor."""
        if self.socket_servidor:
            self.socket_servidor.close()
            logging.info("Servidor cerrado")

if __name__ == "__main__":
    servidor = ServidorTCP()
    try:
        servidor.iniciar()
    except KeyboardInterrupt:
        logging.info("Servidor detenido por el usuario")
        servidor.cerrar()