from dotenv import load_dotenv
import reflex as rx
import os
from supabase import create_client, Client
#from typing import Optional,List
from sqlmodel import Field
import time
from datetime import datetime, timedelta
import pandas as pd
#from io import BytesIO
from io import StringIO
#from starlette.responses import StreamingResponse
from datetime import datetime
import csv
import plotly.express as px
import plotly.graph_objects as go
import asyncio

load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)




class Novedades(rx.Model, table=True):
    No: int
    id: int = Field(default=None, primary_key=True)
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

class Suministros(rx.Model, table=True):
    requests: int = Field(default=None, primary_key=True)
    bodega: str
    estacion: str
    detalle: str
    created_at: str
    URL_PUBLICA: str
    COMENTARIOS: str
    USUARIO: str
    STATUS: str
    COMENTARIO_RECHAZO: str
    FECHA_RECHAZO: str
    




class State(rx.State):
    #print(f"URL: {url}")
    #print(f"Key: {key}")


    email: str = ""
    password: str = ""    


    upload_status: str = ""
    upload_status_sesion: str = ""
    
    codigo_busqueda: str = ""
    estacion_busqueda: str = ""
    codigo_busqueda_devoluciones: str = ""
    
    novedades: list[dict] = []
    suministros: list[dict] = []
    devoluciones: list[dict] = []


    novedad_detalle: dict = {}
    suministro_detalle: dict = {}
    devolucion_detalle: dict = {}

    cargando: bool = False
    error: str = ""

    comentario: str = ""
    comentario_historial: str = ""
    file_url: str = ""
    comentario_rechazo: str = ""

    page_novedades: int = 1
    limit_novedades: int = 10
    total_novedades: int = 0

    page_suministros: int = 1
    limit_suministros: int = 10
    total_suministros: int = 0

    page_devoluciones: int = 1
    limit_devoluciones: int = 10
    total_devoluciones: int = 0

    show_dialog: bool = False

    def open_dialog(self):
        self.show_dialog = True

    def close_dialog(self):
        self.show_dialog = False
    
    
    async def cargar_novedad(self):
        self.cargando = True
        self.error = ""
        self.upload_status: str = ""
        self.comentario: str = ""
        self.comentario_historial: str = ""
        #self.novedad_detalle = {}
        # Obtener el secuencial de la URL
        secuencial = self.router.page.params.get("secuencial", "")
        #print(f"Secuencial: {secuencial}")
        try:
            response = supabase.table("Novedades")\
                            .select("*")\
                            .eq("SECUENCIAL", secuencial)\
                            .execute()
            
            if response.data:
                self.novedad_detalle = response.data[0]
                self.comentario_historial = self.novedad_detalle.get("COMENTARIOS") or ""
                self.file_url = self.novedad_detalle.get("URL_PUBLICA") or ""
                self.comentario_rechazo = self.novedad_detalle.get("COMENTARIO_RECHAZO") or ""
                #print(f"Novedad cargada: {self.novedad_detalle}")

            else:
                self.error = f"No se encontró novedad con secuencial {secuencial}"

        except Exception as e:
            self.error = f"Error al consultar: {str(e)}"
        finally:
            self.cargando = False

    async def cargar_suministro(self):
        self.suministro_detalle = {}
        self.cargando = True
        self.error = ""
        self.upload_status: str = ""
        self.comentario: str = ""
        self.comentario_historial: str = ""
        # Obtener el secuencial de la URL
        request = self.router.page.params.get("request", "")
        try:
            if not request:
                #self.error = "No se proporcionó secuencial"
                return
            # Consulta a Supabase con filtro
            response = supabase.table("Suministros")\
                            .select("*")\
                            .eq("requests", request)\
                            .execute()
            
            if response.data:
                self.suministro_detalle = response.data[0]
                self.comentario_historial = self.novedad_detalle.get("COMENTARIOS") or ""
                self.comentario = self.suministro_detalle.get("COMENTARIOS") or ""
                self.file_url = self.suministro_detalle.get("URL_PUBLICA") or ""
                self.comentario_rechazo = self.suministro_detalle.get("COMENTARIO_RECHAZO") or ""
                #print(f"Novedad cargada: {self.suministro_detalle}")

            else:
                self.error = f"No se encontró novedad con secuencial {request}"

        except Exception as e:
            print(f"Error al consultar: {str(e)}")
            self.error = f"Error al consultar: {str(e)}"
        finally:
            self.cargando = False

    async def cargar_devolucion(self):
        self.cargando = True
        self.error = ""
        self.upload_status: str = ""
        self.devolucion_detalle = {}
        self.comentario: str = ""
        self.comentario_historial: str = ""
        # Obtener el secuencial de la URL
        secuencial = self.router.page.params.get("secuencial", "")
        #print(f"Secuencial: {secuencial}")
        try:
            if not secuencial:
                self.error = "No se proporcionó secuencial"
                return

            # Consulta a Supabase con filtro
            response = supabase.table("Devoluciones")\
                            .select("*")\
                            .eq("SECUENCIAL", secuencial)\
                            .execute()
            
            if response.data:
                self.devolucion_detalle = response.data[0]
                self.comentario_historial = self.novedad_detalle.get("COMENTARIOS") or ""
                self.comentario = self.devolucion_detalle.get("COMENTARIOS") or ""
                self.file_url = self.devolucion_detalle.get("URL_PUBLICA") or ""
                self.comentario_rechazo = self.devolucion_detalle.get("COMENTARIO_RECHAZO") or ""
                #print(f"Novedad cargada: {self.devolucion_detalle}")

            else:
                self.error = f"No se encontró novedad con secuencial {secuencial}"

        except Exception as e:
            self.error = f"Error al consultar: {str(e)}"
        finally:
            self.cargando = False



    @rx.event
    def set_page_novedades(self, new_page: int):
        if new_page < 1:
            return
        self.page_novedades = new_page
        self.load_entries()

    @rx.event
    def set_page_suministros(self, new_page: int):
        if new_page < 1:
            return
        self.page_suministros = new_page
        self.load_suministros()

    @rx.event
    def set_page_devoluciones(self, new_page: int):
        if new_page < 1:
            return
        self.page_devoluciones = new_page
        self.load_devoluciones()
    
    @rx.event
    def load_entries(self,status_filtro: str = None):
        session = supabase.auth.get_session()
        if not session or session.expires_at < time.time():
            self.logout()
        start = (self.page_novedades - 1) * self.limit_novedades
        end = start + self.limit_novedades - 1
        query = supabase.table("Novedades").select("*").order("created_at", desc=True)
        if status_filtro in ["Pendiente", "Finalizado", "Rechazado"]:
            query = query.eq("STATUS", status_filtro)
        response = query.range(start, end).execute()
        if response.data:
            self.novedades = response.data
        else:
            self.novedades = []
    
    @rx.event
    def load_suministros(self,status_filtro: str = None):
        session = supabase.auth.get_session()
        if not session or session.expires_at < time.time():
            self.logout()
        start = (self.page_suministros - 1) * self.limit_suministros
        end = start + self.limit_suministros - 1
        query = supabase.table("Suministros").select("*").order("created_at", desc=True)
        if status_filtro in ["Pendiente", "Finalizado", "Rechazado"]:
            query = query.eq("STATUS", status_filtro)
        response = query.range(start, end).execute()
        if response.data:
            self.suministros = response.data
        else:
            self.suministros = []

    @rx.event
    def load_devoluciones(self,status_filtro: str = None):
        session = supabase.auth.get_session()
        if not session or session.expires_at < time.time():
            self.logout()
        start = (self.page_devoluciones - 1) * self.limit_devoluciones
        end = start + self.limit_devoluciones - 1
        query = supabase.table("Devoluciones").select("*").order("created_at", desc=True)
        if status_filtro in ["Pendiente", "Finalizado", "Rechazado"]:
            query = query.eq("STATUS", status_filtro)
        response = query.range(start, end).execute()
        if response.data:
            self.devoluciones = response.data
        else:
            self.devoluciones = []

    @rx.event
    def verificar_sesion(self):
        if not self.email:
            return rx.redirect("/")
        
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
                self.upload_status_sesion = "Login exitoso"
                return rx.redirect("/data")
                r#eturn response.user
                # Aquí puedes guardar el usuario en el estado si lo deseas
            else:
                self.upload_status_sesion = "Credenciales incorrectas"
            
        except Exception as e:
            self.upload_status_sesion = "Credenciales incorrectas"
            #self.upload_status = f"Error al iniciar sesión: {str(e)}"
            print(f"Error de login: {str(e)}")

    @rx.event
    def logout(self):
        try:
            supabase.auth.sign_out()  # No asumas que retorna algo
            self.upload_status_sesion = "Sesión cerrada exitosamente"
            return rx.redirect("/")
        except Exception as e:
            self.upload_status_sesion = f"Error al cerrar sesión: {str(e)}"
            print(f"Error de logout: {str(e)}")


    @rx.event
    def buscar_por_codigo(self, codigo: str):
        if not codigo:
            self.load_entries()
            return
        response = supabase.table("Novedades").select("*").ilike("SECUENCIAL", f"%{codigo}%").execute()
        self.novedades = response.data if response.data else []
    
    @rx.event
    def buscar_por_codigo_devoluciones(self, codigo: str):
        if not codigo:
            self.load_devoluciones()
            return
        response = supabase.table("Devoluciones").select("*").ilike("SECUENCIAL", f"%{codigo}%").execute()
        self.devoluciones = response.data if response.data else []


    @rx.event
    def buscar_por_estacion(self, codigo: str):
        if not codigo:
            self.load_suministros()
            return
        response = supabase.table("Suministros").select("*").ilike("estacion", f"%{codigo}%").execute()
        self.suministros = response.data if response.data else []

    @rx.event
    def borrar_novedad(self, secuencial: str):
        try:
            supabase.table("Novedades").delete().eq("id", secuencial).execute()
            self.load_entries()
        except Exception as e:
            print(f"Error al borrar novedad: {e}")
    
    @rx.event
    def borrar_suministro(self, id: str):
        try:
            supabase.table("Suministros").delete().eq("requests", id).execute()
            self.load_suministros()
        except Exception as e:
            print(f"Error al borrar el suministro: {e}")
    
    @rx.event
    def borrar_devolucion(self, secuencial: str):
        try:
            supabase.table("Devoluciones").delete().eq("id", secuencial).execute()
            self.load_devoluciones()
        except Exception as e:
            print(f"Error al borrar devolucion: {e}")



    @rx.event
    async def upload_to_supabase_novedades(self, files: list[rx.UploadFile]):
        session = supabase.auth.get_session()
        if not session or session.expires_at < time.time():
            self.logout()  
        secuencial = self.router.page.params.get("secuencial", "")
        #if files:
            #print("Atributos del archivo:", dir(files[0]))
            #print("Archivo:", files[0].name)
        
        if not files:
            self.upload_status = "¡No hay archivo seleccionado!"
            return

        file = files[0]
        if hasattr(file, "read"):
            data_bytes = await file.read()
        else:
            data_bytes = file

        file_name = f"{secuencial}.pdf"
        temp_dir = "./temp_files"
        os.makedirs(temp_dir, exist_ok=True)
        temp_file_path = os.path.join(temp_dir, file_name)

        try:
            supabase.storage.from_("soportes").remove([f"Novedades/{file_name}"])
            supabase.table("Novedades").update({
                "URL_PUBLICA": None,
                "STATUS" : "Pendiente"
            }).eq("SECUENCIAL", secuencial).execute()
        
        except Exception as e:
            print(f"Error al subir archivo: {e}")
            self.upload_status = ""

        try:
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(data_bytes)

            with open(temp_file_path, "rb") as temp_file:
                response = supabase.storage.from_("soportes").upload(
                    f"Novedades/{file_name}", temp_file, {"content-type": "application/pdf"}
                )

            public_url = supabase.storage.from_("soportes").get_public_url(f"Novedades/{file_name}")
            #print(f"Archivo cargado exitosamente: {public_url}")
            self.file_url = public_url
            #self.upload_status = "¡Archivo cargado!"

            actualizacion = supabase.table("Novedades").update({
                "COMENTARIOS": self.comentario,
                "URL_PUBLICA": self.file_url,
                "USUARIO" : self.email,
                "STATUS" : "Finalizado"
            }).eq("SECUENCIAL", secuencial).execute()
            self.comentario = ""
            self.file_url = ""
            self.upload_status = "Carga exitosa"
            #await asyncio.sleep(5)
            #return rx.redirect("/novedades")

        except Exception as e:
            print(f"Error al subir archivo: {e}")
            self.upload_status = "Error"

        finally:
            if temp_file_path and os.path.exists(temp_file_path):
                try:
                    os.remove(temp_file_path)
                except PermissionError as e:
                    print(f"No se pudo eliminar el archivo temporal: {e}")

    @rx.event
    async def upload_to_supabase_suministros(self, files: list[rx.UploadFile]):
        session = supabase.auth.get_session()
        if not session or session.expires_at < time.time():
            self.logout() 
        request = self.router.page.params.get("request", "")
        #self.upload_status: str = ""
        
        if not files:
            self.upload_status = "¡No hay archivo seleccionado!"
            return

        file = files[0]
        if hasattr(file, "read"):
            data_bytes = await file.read()
        else:
            data_bytes = file

        file_name = f"{request}.pdf"
        temp_dir = "./temp_files"
        os.makedirs(temp_dir, exist_ok=True)
        temp_file_path = os.path.join(temp_dir, file_name)

        try:
            supabase.storage.from_("soportes").remove([f"Suministros/{file_name}"])
            actualizacion = supabase.table("Suministros").update({
                "URL_PUBLICA": None,
                "STATUS" : "Pendiente"
            }).eq("SECUENCIAL", request).execute()
        
        except Exception as e:
            print(f"Error al subir archivo: {e}")
            self.upload_status = ""

        try:
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(data_bytes)

            with open(temp_file_path, "rb") as temp_file:
                response = supabase.storage.from_("soportes").upload(
                    f"Suministros/{file_name}", temp_file, {"content-type": "application/pdf"}
                )

            public_url = supabase.storage.from_("soportes").get_public_url(f"Suministros/{file_name}")
            #print(f"Archivo cargado exitosamente: {public_url}")
            self.file_url = public_url
            #self.upload_status = "¡Archivo cargado!"

            actualizacion = supabase.table("Suministros").update({
                "COMENTARIOS": self.comentario,
                "URL_PUBLICA": self.file_url,
                "USUARIO" : self.email,
                "STATUS" : "Finalizado"
            }).eq("requests", request).execute()
            self.comentario = ""
            self.file_url = ""
            self.upload_status = "Carga exitosa"
            #await asyncio.sleep(5)
            #return rx.redirect("/suministros")

        except Exception as e:
            print(f"Error al subir archivo: {e}")
            self.upload_status = "Error"

        finally:
            if temp_file_path and os.path.exists(temp_file_path):
                try:
                    os.remove(temp_file_path)
                except PermissionError as e:
                    print(f"No se pudo eliminar el archivo temporal: {e}")

    @rx.event
    async def upload_to_supabase_devoluciones(self, files: list[rx.UploadFile]):
        session = supabase.auth.get_session()
        if not session or session.expires_at < time.time():
            self.logout() 
        secuencial = self.router.page.params.get("secuencial", "")
        if not files:
            self.upload_status = "¡No hay archivo seleccionado!"
            return

        file = files[0]
        if hasattr(file, "read"):
            data_bytes = await file.read()
        else:
            data_bytes = file

        file_name = f"{secuencial}.pdf"
        temp_dir = "./temp_files"
        os.makedirs(temp_dir, exist_ok=True)
        temp_file_path = os.path.join(temp_dir, file_name)

        try:
            supabase.storage.from_("soportes").remove([f"Devoluciones/{file_name}"])
            actualizacion = supabase.table("Devoluciones").update({
                "URL_PUBLICA": None,
                "STATUS" : "Pendiente"
            }).eq("SECUENCIAL", secuencial).execute()
        
        except Exception as e:
            print(f"Error al subir archivo: {e}")
            self.upload_status = ""

        try:
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(data_bytes)

            with open(temp_file_path, "rb") as temp_file:
                response = supabase.storage.from_("soportes").upload(
                    f"Devoluciones/{file_name}", temp_file, {"content-type": "application/pdf"}
                )

            public_url = supabase.storage.from_("soportes").get_public_url(f"Devoluciones/{file_name}")
            #print(f"Archivo cargado exitosamente: {public_url}")
            self.file_url = public_url
            #self.upload_status = "¡Archivo cargado!"

            actualizacion = supabase.table("Devoluciones").update({
                "COMENTARIOS": self.comentario,
                "URL_PUBLICA": self.file_url,
                "USUARIO" : self.email,
                "STATUS" : "Finalizado"
            }).eq("SECUENCIAL", secuencial).execute()
            self.comentario = ""
            self.file_url = ""
            self.upload_status = "Carga exitosa"
            #await asyncio.sleep(5)
            #return rx.redirect("/devoluciones")

        except Exception as e:
            print(f"Error al subir archivo: {e}")
            self.upload_status = "Error"

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
            response = supabase.table("Novedades").select("No, FECHA, REF, LUGAR, DETALLE, SECUENCIAL, SIGNO, VALOR, DESCRIPCION, STATUS, COMENTARIO_RECHAZO, FECHA_RECHAZO").order("created_at", desc=True).execute()
            data = response.data
            if not data:
                return
        # Crear CSV en memoria
        output = StringIO()
        output.write('\ufeff')
        writer = csv.DictWriter(output, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)
        output.seek(0)
        fecha_actual = datetime.now().strftime("%Y%m%d")
        # Devolver como descarga (versión corregida)
        return rx.download(
            data=output.getvalue(),
            filename=f"Novedades_{fecha_actual}.csv"
        )

    async def descargar_suministros_csv(self):
        data = self.suministros if hasattr(self, 'suministros') and self.suministros else []        
        if not data:
            response = supabase.table("Suministros").select("requests, bodega, estacion, detalle, created_at, STATUS, COMENTARIO_RECHAZO, FECHA_RECHAZO").order("created_at", desc=True).execute()
            data = response.data
            if not data:
                return
        # Crear CSV en memoria
        output = StringIO()
        output.write('\ufeff')
        writer = csv.DictWriter(output, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)
        output.seek(0)
        fecha_actual = datetime.now().strftime("%Y%m%d")
        # Devolver como descarga (versión corregida)
        return rx.download(
            data=output.getvalue(),
            filename=f"Suministros_{fecha_actual}.csv"
        )
    
    async def descargar_devoluciones_csv(self):
        data = self.devoluciones if hasattr(self, 'devoluciones') and self.devoluciones else []        
        if not data:
            response = supabase.table("Devoluciones").select("No, FECHA, REF, LUGAR, DETALLE, SECUENCIAL, SIGNO, VALOR, DESCRIPCION, STATUS, COMENTARIO_RECHAZO, FECHA_RECHAZO").order("created_at", desc=True).execute()
            data = response.data
            if not data:
                return
        # Crear CSV en memoria
        output = StringIO()
        output.write('\ufeff')
        writer = csv.DictWriter(output, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)
        output.seek(0)
        fecha_actual = datetime.now().strftime("%Y%m%d")
        # Devolver como descarga (versión corregida)
        return rx.download(
            data=output.getvalue(),
            filename="Devoluciones_{fecha_actual}.csv"
        )
    


class Statics (rx.State):
    
    @rx.var
    def novedades_semanal(self) -> int:
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
        return resultados
    
    @rx.var
    def quejas_semanal_novedades(self) -> int:
        hoy = datetime.utcnow().date()
        resultados = 0
        for i in range(7):
            dia = hoy - timedelta(days=6 - i)
            dia_siguiente = dia + timedelta(days=1)
            count = supabase.table("Quejas") \
                .select("id_quejas", count="exact") \
                .eq("proceso","Novedades bancarias") \
                .gte("created_at", dia.isoformat()) \
                .lt("created_at", dia_siguiente.isoformat()) \
                .execute().count or 0
            resultados += count
        return resultados
            

    @rx.var
    def total_novedades(self) -> int:
        response = supabase.table("Novedades").select("id",count="exact").execute().count or 0
        return response

    @rx.var
    def total_novedades_pendientes(self) -> int:
        response = supabase.table("Novedades").select("id", count="exact").is_("URL_PUBLICA", None).execute().count or 0
        return response


    @rx.var
    def total_quejas_novedades(self) -> int:
        response = supabase.table("Quejas").select("id_quejas",count="exact").eq("proceso","Novedades bancarias").execute().count or 0
        return response

    @rx.var
    def total_suministros(self) -> int:
        response = supabase.table("Suministros").select("requests",count="exact").execute().count or 0
        return response
    
    @rx.var
    def total_suministros_pendientes(self) -> int:
        response = supabase.table("Suministros").select("requests", count="exact").is_("URL_PUBLICA", None).execute().count or 0
        return response

    @rx.var
    def total_quejas_suministros(self) -> int:
        response = supabase.table("Quejas").select("id_quejas",count="exact").eq("proceso","Suministros").execute().count or 0
        return response
    
    @rx.var
    def suministros_semanal(self) -> int:
        hoy = datetime.utcnow().date()
        resultados = 0
        for i in range(7):
            dia = hoy - timedelta(days=6 - i)
            dia_siguiente = dia + timedelta(days=1)
            count = supabase.table("Suministros") \
                .select("requests", count="exact") \
                .gte("created_at", dia.isoformat()) \
                .lt("created_at", dia_siguiente.isoformat()) \
                .execute().count or 0
            resultados += count
        return resultados
    
    @rx.var
    def quejas_semanal_suministros(self) -> int:
        hoy = datetime.utcnow().date()
        resultados = 0
        for i in range(7):
            dia = hoy - timedelta(days=6 - i)
            dia_siguiente = dia + timedelta(days=1)
            count = supabase.table("Quejas") \
                .select("id_quejas", count="exact") \
                .eq("proceso","Suministros") \
                .gte("created_at", dia.isoformat()) \
                .lt("created_at", dia_siguiente.isoformat()) \
                .execute().count or 0
            resultados += count
        return resultados


    @rx.var
    def devoluciones_semanal(self) -> int:
        hoy = datetime.utcnow().date()
        resultados = 0
        for i in range(7):
            dia = hoy - timedelta(days=6 - i)
            dia_siguiente = dia + timedelta(days=1)
            count = supabase.table("Devoluciones") \
                .select("id", count="exact") \
                .gte("created_at", dia.isoformat()) \
                .lt("created_at", dia_siguiente.isoformat()) \
                .execute().count or 0
            resultados += count
        return resultados
    
    @rx.var
    def quejas_semanal_devoluciones(self) -> int:
        hoy = datetime.utcnow().date()
        resultados = 0
        for i in range(7):
            dia = hoy - timedelta(days=6 - i)
            dia_siguiente = dia + timedelta(days=1)
            count = supabase.table("Quejas") \
                .select("id_quejas", count="exact") \
                .eq("proceso","Devoluciones") \
                .gte("created_at", dia.isoformat()) \
                .lt("created_at", dia_siguiente.isoformat()) \
                .execute().count or 0
            resultados += count
        return resultados
            

    @rx.var
    def total_devoluciones(self) -> int:
        response = supabase.table("Devoluciones").select("id",count="exact").execute().count or 0
        return response

    @rx.var
    def total_devoluciones_pendientes(self) -> int:
        response = supabase.table("Devoluciones").select("id", count="exact").is_("URL_PUBLICA", None).execute().count or 0
        return response


    @rx.var
    def total_quejas_devoluciones(self) -> int:
        response = supabase.table("Quejas").select("id_quejas",count="exact").eq("proceso","Devoluciones").execute().count or 0
        return response


class Graphics (rx.State):

    value_novedades: bool = False
    value_suministros: bool = False
    novedades_line: list[dict] = []
    suministros_line: list[dict] = []

    @rx.event
    def set_novedades(self, value: bool):
        self.value_novedades = value
    
    @rx.event
    def set_suministros(self, value: bool):
        self.value_suministros = value

    @rx.event
    def load_novedades_line(self):
        response = supabase.table("Novedades").select("*").order("created_at", desc=True).execute()
        if response.data:
            self.novedades_line = response.data
        else:
            self.novedades_line = []
    
    @rx.event
    def load_suministros_line(self):
        response = supabase.table("Suministros").select("*").order("created_at", desc=True).execute()
        if response.data:
            self.suministros_line = response.data
        else:
            self.suministros_line = []

    @rx.var(cache=True)
    def novedades_acumuladas(self) -> list[dict]:
        self.load_novedades_line(),
        acumulado = {}
        for novedad in self.novedades_line:
            fecha = novedad["FECHA"][0:5]
            valor = novedad["VALOR"]
            acumulado[fecha] = acumulado.get(fecha, 0) + valor
        # Convertir a lista de dicts ordenada por fecha
        return [
            {"FECHA": fecha, "VALOR": valor}
            for fecha, valor in sorted(acumulado.items())
            ]

    @rx.var(cache=True)
    def novedades_acumuladas_casos(self) -> list[dict]:
        self.load_novedades_line(),
        acumulado = {}
        for novedad in self.novedades_line:
            fecha = novedad["FECHA"][0:5]
            #valor = novedad["VALOR"]
            acumulado[fecha] = acumulado.get(fecha, 0) + 1
        # Convertir a lista de dicts ordenada por fecha
        return [
            {"Fecha": fecha, "Acumulado": acumulado}
            for fecha, acumulado in sorted(acumulado.items())
            ]
    
    @rx.var(cache=True)
    def suministros_acumulados(self) -> list[dict]:
        self.load_suministros_line(),
        acumulado = {}
        for suministro in self.suministros_line:
            fecha_original = suministro.get("created_at")
            fecha_original = datetime.fromisoformat(fecha_original.replace("Z", "+00:00"))
            fecha = fecha_original.strftime("%d/%m/%Y")
            acumulado[fecha] = acumulado.get(fecha, 0) + 1
        # Convertir a lista de dicts ordenada por fecha
        return [
            {"Fecha": fecha, "Acumulado": acumulado}
            for fecha, acumulado in sorted(acumulado.items())
            ]

    @rx.var(cache=True)
    def novedades_acumuladas_estacion(self) -> list[dict]:
        self.load_novedades_line(),
        acumulado = {}
        for novedad in self.novedades_line:
            estacion = novedad.get("EESS")
            #valor = novedad["VALOR"]
            acumulado[estacion] = acumulado.get(estacion, 0) + 1
        # Convertir a lista de dicts ordenada por fecha
        return [
            {"Estacion": estacion, "Total": acumulado}
            for estacion, acumulado in sorted(acumulado.items())
            ]

    @rx.var(cache=True)
    def suministros_acumulados_estacion(self) -> list[dict]:
        self.load_suministros_line(),
        acumulado = {}
        for novedad in self.suministros_line:
            estacion = novedad.get("estacion")
            #valor = novedad["VALOR"]
            acumulado[estacion] = acumulado.get(estacion, 0) + 1
        # Convertir a lista de dicts ordenada por fecha
        return [
            {"Estacion": estacion, "Total": acumulado}
            for estacion, acumulado in sorted(acumulado.items())
            ]

