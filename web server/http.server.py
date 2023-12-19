from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import mimetypes

HOST_NAME = "localhost"
SERVER_PORT = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # récupéré le chemin du fichier demandé
        file_path = self.path.strip("/")

        # si le chemin est vide, renvoyer index.html par défaut
        if not file_path:
            file_path = "BeStream.html"

        file_path = os.path.join(os.path.dirname(__file__), file_path)

        # vérifier si le fichier existe
        if os.path.exists(file_path):
            with open(file_path, "rb") as file:
                content = file.read()

            # obtenir le type mime du fichier
            mime_type, _ = mimetypes.guess_type(file_path)

            # envoyer la réponse avec le contenu du fichier et le type MIME
            self.send_response(200)
            self.send_header("Content-type", mime_type)
            self.end_headers()
            self.wfile.write(content)
        else:

            # si le fichier n'existe pas => erreur 404
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>404 Not Found</title></head>", "utf-8"))
            self.wfile.write(bytes("<body><p>404 Not Found</p></body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((HOST_NAME, SERVER_PORT), MyServer)
    print("Server started http://%s:%s" % (HOST_NAME, SERVER_PORT))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
