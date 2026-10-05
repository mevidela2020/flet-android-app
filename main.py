import json
import os

import flet as ft


def main(page: ft.Page):
    page.title = "Seguimiento de Musculación - Mariela Videla"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20

    # Los pesos se guardan en un archivo JSON junto al script
    archivo_pesos = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pesos.json")
    try:
        with open(archivo_pesos, "r", encoding="utf-8") as f:
            pesos = json.load(f)
    except (FileNotFoundError, ValueError):
        pesos = {}

    def crear_campo(grupo, ejercicio, unidad):
        clave = f"{grupo}|{ejercicio}"

        def guardar(e):
            pesos[clave] = e.control.value
            try:
                with open(archivo_pesos, "w", encoding="utf-8") as f:
                    json.dump(pesos, f, ensure_ascii=False, indent=2)
            except OSError:
                pass  # si no se puede escribir, el dato queda solo en pantalla

        return ft.TextField(
            label=unidad,
            value=pesos.get(clave, ""),
            width=100,
            dense=True,
            text_size=13,
            keyboard_type=ft.KeyboardType.NUMBER,
            on_change=guardar,
        )

    # Encabezado con información del perfil y gimnasio
    header = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("DON NAPOLEÓN", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                    ft.Text("Socia: Mariela Videla | 50 Años", size=14, weight=ft.FontWeight.W_500),
                    ft.Text("Frecuencia: 3 veces por semana", size=13, color=ft.Colors.GREY_700),
                    ft.Divider(),
                    ft.Text("Observaciones Médicas:", size=13, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_700),
                    ft.Text("• Artritis Reumatoide\n• Dolores Cervicales", size=12, color=ft.Colors.RED_900),
                ]
            ),
            padding=15,
        )
    )

    # Datos estructurados de la rutina según la ficha de entrenamiento
    rutina_data = [
        {
            "grupo": "Abdominales",
            "ejercicios": ["Encogimientos Invertidos", "Toco Talón"],
            "dias": "Días 1, 3",
            "progreso": "15D: 3x12 | 30D: 3x15 | 45D: 4x12 | 60D: 4x15",
        },
        {
            "grupo": "Aductores",
            "ejercicios": ["Sillón Aductores"],
            "dias": "Días 1, 3",
            "progreso": "15D: 3x12 | 30D: 3x15 | 45D: 3x12 | 60D: 4x10",
        },
        {
            "grupo": "Abductores",
            "ejercicios": ["Sillón Abductores"],
            "dias": "Días 1, 3",
            "progreso": "Mismas series que Aductores",
        },
        {
            "grupo": "Glúteos",
            "ejercicios": ["Banco Patada Atrás Parada"],
            "dias": "Día 2",
            "progreso": "Seguir progresión según semanas",
        },
        {
            "grupo": "Cuádriceps",
            "ejercicios": ["Sentadillas Libres c/ Mancuerna", "Sillón de Cuádriceps"],
            "dias": "Días 1, 3 (Sentadillas) | Día 2 (Sillón)",
            "progreso": "Progreso continuo según tolerancia",
        },
        {
            "grupo": "Femorales",
            "ejercicios": ["Camilla Femoral", "Polea"],
            "dias": "Días 1, 3 (Camilla) | Día 2 (Polea)",
            "progreso": "15D: 3x12 | 30D: 3x10 | 45D: 4x12 | 60D: 4x10",
        },
        {
            "grupo": "Pantorrillas",
            "ejercicios": ["Sillón de Coser"],
            "dias": "Día 2",
            "progreso": "15D: 3x12 | 30D: 3x15 | 45D: 4x12 | 60D: 4x15",
        },
        {
            "grupo": "Espinales",
            "ejercicios": [],
            "dias": "Sin asignar",
            "progreso": "Sin datos en la ficha",
        },
        {
            "grupo": "Pectorales",
            "ejercicios": ["Press Máq. Inclinado", "Mariposa"],
            "dias": "Días 1, 3 (Press) | Día 2 (Mariposa)",
            "progreso": "Press: 15D: 3x15 | 30D: 3x12 | 45D: 4x10 | 60D: 4x12\n"
                        "Mariposa: 15D: 3x12 | 30D: 3x10 | 45D: 4x12 | 60D: 4x10",
        },
        {
            "grupo": "Espalda",
            "ejercicios": ["Press Máq. Abierto", "Jalones a 1 Brazo"],
            "dias": "Días 1, 3 (Press) | Día 2 (Jalones)",
            "progreso": "Press: 15D: 3x15 | 30D: 3x12 | 45D: 4x10 | 60D: 4x12\n"
                        "Jalones: 15D: 3x12 | 30D: 3x10 | 45D: 4x12 | 60D: 4x10",
        },
        {
            "grupo": "Hombros",
            "ejercicios": ["Vuelos Frontales c/ Disco", "Arnold c/ Mancuernas"],
            "dias": "Días 1, 3 (Vuelos) | Día 2 (Arnold)",
            "progreso": "15D: 3x12 | 30D: 3x10 | 45D: 4x12 | 60D: 4x10",
        },
        {
            "grupo": "Bíceps",
            "ejercicios": ["Curl Mancuerna Martillo"],
            "dias": "Día 2",
            "progreso": "15D: 3x12 | 30D: 3x10 | 45D: 4x12 | 60D: 4x10",
        },
        {
            "grupo": "Tríceps",
            "ejercicios": ["Extensión Polea c/ Soga"],
            "dias": "Días 1, 3",
            "progreso": "15D: 3x15 | 30D: 3x12 | 45D: 4x10 | 60D: 4x12",
        },
        {
            "grupo": "Antebrazos",
            "ejercicios": [],
            "dias": "Sin asignar",
            "progreso": "Sin datos en la ficha",
        },
        {
            "grupo": "Aeróbicos",
            "ejercicios": ["Aeróbico 1", "Aeróbico 2", "Aeróbico 3"],
            "unidad": "Minutos",
            "dias": "Según ficha",
            "progreso": "Completar los minutos según indicación del profesor",
        },
    ]

    # Renderizado de tarjetas de ejercicios
    tarjetas_ejercicios = []
    for item in rutina_data:
        unidad = item.get("unidad", "Peso (kg)")
        ejercicios_list = [
            ft.Row(
                [
                    ft.Text(f"• {ej}", size=14, weight=ft.FontWeight.W_500, expand=True),
                    crear_campo(item["grupo"], ej, unidad),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
            for ej in item["ejercicios"]
        ]
        if not ejercicios_list:
            ejercicios_list = [
                ft.Text("Sin ejercicios asignados", size=13, italic=True, color=ft.Colors.GREY_500)
            ]

        # Etiqueta de días (reemplaza al ft.Chip sin acción)
        etiqueta_dias = ft.Container(
            content=ft.Text(item["dias"], size=11, color=ft.Colors.BLUE_900),
            bgcolor=ft.Colors.BLUE_50,
            padding=8,
            border_radius=12,
        )

        tarjeta = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text(
                                    item["grupo"],
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.INDIGO_800,
                                    expand=True,
                                ),
                                etiqueta_dias,
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Column(ejercicios_list, spacing=2),
                        ft.Text(
                            f"Progresión: {item['progreso']}",
                            size=12,
                            italic=True,
                            color=ft.Colors.GREY_700,
                        ),
                    ],
                    spacing=8,
                ),
                padding=12,
            )
        )
        tarjetas_ejercicios.append(tarjeta)

    # Estructura principal de la vista
    page.add(
        header,
        ft.Text("Rutina de Entrenamiento", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_900),
        ft.Column(tarjetas_ejercicios),
    )


if __name__ == "__main__":
    # ft.run en Flet 0.80+; ft.app en versiones anteriores
    if hasattr(ft, "run"):
        ft.run(main)
    else:
        ft.app(target=main)
