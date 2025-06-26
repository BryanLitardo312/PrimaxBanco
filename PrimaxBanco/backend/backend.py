from dotenv import load_dotenv
import reflex as rx
import os
from supabase import create_client, Client
from typing import Optional,List
from sqlmodel import Field
import time
from datetime import datetime, timedelta
import pandas as pd
from io import BytesIO
from io import StringIO
from starlette.responses import StreamingResponse
import csv

load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)




class Novedades(rx.Model, table=True):
    #No: int
    #id: int = Field(default=None, primary_key=True)
    FECHA: str
    REF: str
    LUGAR: str
    DETALLE: str
    SECUENCIAL: str
    SIGNO: str
    VALOR: float
    DESCRIPCION: str
    created_at: str
    EESS: str
    BODEGA: str
    COMENTARIOS: str
    URL_PUBLICA: str
    USUARIO: str
    STATUS: str
    COMENTARIO_RECHAZO: str
    FECHA_RECHAZO: str


    




class State(rx.State):
    print(f"URL: {url}")
    print(f"Key: {key}")

    email: str = ""
    password: str = ""    

    uploading: bool = False
    upload_status: str = ""  # "success", "error"
    current_upload_id: str = ""
    
    codigo_busqueda: str = ""
    
    novedades: list[dict] = []
    directorio: Optional[int] = None


    novedad_detalle: dict = {}
    cargando: bool = False
    error: str = ""

    comentario: str = ""
    file_url: str = ""

    page: int = 1
    limit: int = 10
    total: int = 0

    show_dialog: bool = False

    def open_dialog(self):
        self.show_dialog = True

    def close_dialog(self):
        self.show_dialog = False
    
    async def cargar_novedad(self):
        self.cargando = True
        self.error = ""
        self.novedad_detalle = {}
        # Obtener el secuencial de la URL
        secuencial = self.router.page.params.get("secuencial", "")
        #print(f"Secuencial: {secuencial}")
        try:
            if not secuencial:
                self.error = "No se proporcionó secuencial"
                return

            # Consulta a Supabase con filtro
            response = supabase.table("Novedades")\
                            .select("*")\
                            .eq("SECUENCIAL", secuencial)\
                            .execute()
            
            if response.data:
                self.novedad_detalle = response.data[0]
                self.comentario = self.novedad_detalle.get("COMENTARIOS") or ""
                self.file_url = self.novedad_detalle.get("URL_PUBLICA") or ""
                print(f"Novedad cargada: {self.novedad_detalle}")

            else:
                self.error = f"No se encontró novedad con secuencial {secuencial}"

        except Exception as e:
            self.error = f"Error al consultar: {str(e)}"
        finally:
            self.cargando = False

    @rx.var
    def novedades_diarias(self) -> int:
        hoy = datetime.utcnow().date()
        resultados = 0
        for i in range(7):
            dia = hoy - timedelta(days=6 - i)
            dia_siguiente = dia + timedelta(days=1)
            count = supabase.table("Novedades") \
                .select("id", count="exact") \
                .gte("created_at", dia.isoformat()) \
                .lt("created_at", dia_siguiente.isoformat()) \
                .execute().count or 0
            resultados += count
            #print(resultados)

        return resultados
    
    @rx.var
    def quejas_diarias(self) -> int:
        hoy = datetime.utcnow().date()
        resultados = 0
        for i in range(7):
            dia = hoy - timedelta(days=6 - i)
            dia_siguiente = dia + timedelta(days=1)
            count = supabase.table("Quejas") \
                .select("id_quejas", count="exact") \
                .gte("created_at", dia.isoformat()) \
                .lt("created_at", dia_siguiente.isoformat()) \
                .execute().count or 0
            
            #resultados.append({
                #"fecha": dia.strftime("%Y-%m-%d"),
                #"cantidad": count
            #})
            #print(count)
            resultados += count
            #print(resultados)

        return resultados
            

    @rx.var
    def load_novedades(self) -> int:
        directorio = supabase.table("Novedades").select("*",count="exact").execute()
        if directorio.count is not None:
            return directorio.count
        return 0

    @rx.var
    def load_novedades_pendientes(self) -> int:
        count_null = supabase.table("Novedades").select("*", count="exact").is_("URL_PUBLICA", None).execute().count or 0
        print(f"Count null: {count_null}")
        return count_null

    @rx.var
    def load_suministros(self) -> int:
        # Lógica para cargar los datos de Supabase
        #directorio=supabase.table("Directorio_supa").select("Correo_EDS").eq("BOD", "E102").execute()
        directorio = supabase.table("Suministros").select("*",count="exact").execute()
        if directorio.count is not None:
            return directorio.count
        return 0


    @rx.var
    def load_quejas(self) -> int:
        # Lógica para cargar los datos de Supabase
        #directorio=supabase.table("Directorio_supa").select("Correo_EDS").eq("BOD", "E102").execute()
        directorio = supabase.table("Quejas").select("*",count="exact").eq("proceso","Novedades bancarias").execute()
        if directorio.count is not None:
            return directorio.count
        return 0

    @rx.event
    def set_page(self, new_page: int):
        if new_page < 1:
            return
        self.page = new_page
        self.load_entries()
    #@rx.event
    #def load_entries(self):
        #result = supabase.table("Novedades").select("*").execute()
        #if result.data:
            #self.novedades = [Novedades(**item).dict() for item in result.data]
        #else:
            #self.novedades = []
    
    @rx.event
    def load_entries(self,status_filtro: str = None):
        start = (self.page - 1) * self.limit
        end = start + self.limit - 1
        query = supabase.table("Novedades").select("*").order("created_at", desc=True)
        if status_filtro:
            query = query.eq("STATUS", status_filtro)
        response = query.range(start, end).execute()
        if response.data:
            self.novedades = response.data
        else:
            self.novedades = []

    @rx.event
    def login(self, email: str, password: str):
        try:
            response = supabase.auth.sign_in_with_password(
                {
                    "email": email, 
                    "password": password,
                }
            )
            if response.user:
                self.upload_status = "Login exitoso"
                return rx.redirect("/novedades")
                # Aquí puedes guardar el usuario en el estado si lo deseas
            else:
                self.upload_status = "Credenciales incorrectas"
            
        except Exception as e:
            self.upload_status = f"Error al iniciar sesión: {str(e)}"
            print(f"Error de login: {str(e)}")

    @rx.event
    def logout(self):
        try:
            supabase.auth.sign_out()  # No asumas que retorna algo
            self.upload_status = "Sesión cerrada exitosamente"
            return rx.redirect("/")
        except Exception as e:
            self.upload_status = f"Error al cerrar sesión: {str(e)}"
            print(f"Error de logout: {str(e)}")


    @rx.event
    def buscar_por_codigo(self, codigo: str):
        if not codigo:
            return
        response = supabase.table("Novedades").select("*").ilike("SECUENCIAL", f"%{codigo}%").execute()
        self.novedades = response.data if response.data else []
    
    @rx.event
    def borrar_novedad(self, secuencial: str):
        try:
            supabase.table("Novedades").delete().eq("SECUENCIAL", secuencial).execute()
            # Opcional: recargar la lista de novedades
            self.load_entries()
        except Exception as e:
            print(f"Error al borrar novedad: {e}")


    @rx.event
    async def upload_to_supabase(self, files: list[rx.UploadFile]):
        
        secuencial = self.router.page.params.get("secuencial", "")
        if files:
            #print("Atributos del archivo:", dir(files[0]))
            print("Archivo:", files[0].name)
        
        if not files:
            self.upload_status = "No se seleccionó ningún archivo"
            return

        file = files[0]

        if hasattr(file, "read"):
            data_bytes = await file.read()
        else:
            data_bytes = file

        #file_name = file.name
        file_name = f"{secuencial}.pdf"
        temp_dir = "./temp_files"
        os.makedirs(temp_dir, exist_ok=True)
        temp_file_path = os.path.join(temp_dir, file_name)

        try:
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(data_bytes)

            with open(temp_file_path, "rb") as temp_file:
                response = supabase.storage.from_("soportes").upload(
                    file_name, temp_file, {"content-type": "application/pdf"}
                )

            public_url = supabase.storage.from_("soportes").get_public_url(file_name)
            print(f"Archivo cargado exitosamente: {public_url}")
            self.file_url = public_url
            self.upload_status = "success"

            actualizacion = supabase.table("Novedades").update({
                "COMENTARIOS": self.comentario,
                "URL_PUBLICA": self.file_url,
            }).eq("SECUENCIAL", secuencial).execute()
            self.comentario = ""
            self.file_url = ""

        except Exception as e:
            print(f"Error al subir archivo: {e}")
            self.upload_status = "error"

        finally:
            if temp_file_path and os.path.exists(temp_file_path):
                try:
                    os.remove(temp_file_path)
                except PermissionError as e:
                    print(f"No se pudo eliminar el archivo temporal: {e}")



class Download(rx.State):
    
    async def descargar_novedades_csv(self):

        data = self.novedades if hasattr(self, 'novedades') and self.novedades else []        
        if not data:
            response = supabase.table("Novedades").select("*").order("created_at", desc=True).execute()
            data = response.data
            if not data:
                return
        # Crear CSV en memoria
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)
        output.seek(0)
        # Devolver como descarga (versión corregida)
        return rx.download(
            data=output.getvalue(),
            filename="novedades.csv"
        )