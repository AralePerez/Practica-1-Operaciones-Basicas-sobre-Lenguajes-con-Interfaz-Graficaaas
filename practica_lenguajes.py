import flet as ft
from itertools import product

# -----------------------------
# FUNCIONES DE LENGUAJES
# -----------------------------

def prefijos(cadena):
    return [cadena[:i] for i in range(len(cadena)+1)]

def sufijos(cadena):
    return [cadena[i:] for i in range(len(cadena)+1)]

def subcadenas(cadena):
    subs = set()
    for i in range(len(cadena)):
        for j in range(i+1, len(cadena)+1):
            subs.add(cadena[i:j])
    subs.add("")
    return sorted(subs)

def kleene(alfabeto, max_len):
    resultado = [""]
    for i in range(1, max_len+1):
        for p in product(alfabeto, repeat=i):
            resultado.append("".join(p))
    return resultado

def positiva(alfabeto, max_len):
    resultado = []
    for i in range(1, max_len+1):
        for p in product(alfabeto, repeat=i):
            resultado.append("".join(p))
    return resultado

# -----------------------------
# INTERFAZ
# -----------------------------

def main(page: ft.Page):

    page.title = "Operaciones sobre Lenguajes"
    page.scroll = "auto"

    cadena_input = ft.TextField(label="Ingrese una cadena")
    resultado = ft.TextField(multiline=True, min_lines=10, max_lines=20)

    alfabeto_input = ft.TextField(label="Ingrese alfabeto (ej: 0,1)")
    longitud_input = ft.TextField(label="Longitud máxima")

    def calcular_sub(event):
        cadena = cadena_input.value

        p = prefijos(cadena)
        s = sufijos(cadena)
        sub = subcadenas(cadena)

        texto = "PREFIJOS:\n"
        texto += str(p) + "\n\n"

        texto += "SUFIJOS:\n"
        texto += str(s) + "\n\n"

        texto += "SUBCADENAS:\n"
        texto += str(sub)

        resultado.value = texto
        page.update()

    def calcular_kleene(event):
        alfabeto = alfabeto_input.value.split(",")
        max_len = int(longitud_input.value)

        k = kleene(alfabeto, max_len)
        p = positiva(alfabeto, max_len)

        texto = "CERRADURA DE KLEENE Σ*:\n"
        texto += str(k) + "\n\n"

        texto += "CERRADURA POSITIVA Σ+:\n"
        texto += str(p)

        resultado.value = texto
        page.update()

    def guardar(event):
        with open("resultado.txt","w",encoding="utf-8") as f:
            f.write(resultado.value)

        page.snack_bar = ft.SnackBar(ft.Text("Archivo guardado como resultado.txt"))
        page.snack_bar.open = True
        page.update()

    page.add(

        ft.Text("Operaciones sobre Lenguajes Formales", size=25, weight="bold"),

        ft.Divider(),

        ft.Text("Subcadenas, Prefijos y Sufijos"),

        cadena_input,

        ft.ElevatedButton("Calcular", on_click=calcular_sub),

        ft.Divider(),

        ft.Text("Cerradura de Kleene y Positiva"),

        alfabeto_input,
        longitud_input,

        ft.ElevatedButton("Generar Lenguaje", on_click=calcular_kleene),

        ft.Divider(),

        resultado,

        ft.ElevatedButton("Guardar en archivo", on_click=guardar)

    )

ft.app(target=main)