import flet as ft

def main(page: ft.Page):
    page.title = "Seguimiento de Musculación - Mariela Videla"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20

    # Encabezado con información del perfil y gimnasio
    header = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("VÉLEZ SARSFIELD NORTE", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_900),
                    ft.Text("Socia: Mariela Videla | 50 Años", size=14, weight=ft.FontWeight.W_500),
                    ft.Text("Frecuencia: 3 veces por semana", size=13, color=ft.colors.GREY_700),
                    ft.Divider(),
                    ft.Text("Observaciones Médicas:", size=13, weight=ft.FontWeight.BOLD, color=ft.colors.RED_700),
                    ft.Text("• Artritis Reumatoide\n• Dolores Cervicales", size=12, color=ft.colors.RED_900),
                ]
            ),
            padding=15
        )
    )

    # Datos estructurados de la rutina según la ficha de entrenamiento
    rutina_data = [
        {
            "grupo": "Abdominales",
            "ejercicios": ["Encogimientos Invertidos", "Toco Talón"],
            "dias": "Días 1, 3",
            "progreso": "15D: 3x12 | 30D: 3x15 | 45D: 4x12 | 60D: 4x15"
        },
        {
            "grupo": "Aductores",
            "ejercicios": ["Sillón Aductores"],
            "dias": "Días 1, 3",
            "progreso": "15D: 3x12 | 30D: 3x15 | 45D: 3x12 | 60D: 4x10"
        },
        {
            "grupo": "Abductores",
            "ejercicios": ["Sillón Abductores"],
            "dias": "Días 1, 3",
            "progreso": "Mismas series que Aductores"
        },
        {
            "grupo": "Glúteos",
            "ejercicios": ["Banco Patada Atrás Parada"],
            "dias": "Día 2",
            "progreso": "Seguir progresión según semanas"
        },
        {
            "grupo": "Cuádriceps",
            "ejercicios": ["Sentadillas Libres c/ Mancuerna", "Sillón de Cuádriceps"],
            "dias": "Días 1, 3 (Sentadillas) | Día 2 (Sillón)",
            "progreso": "Progreso continuo según tolerancia"
        },
        {
            "grupo": "Femorales",
            "ejercicios": ["Camilla Femoral", "Polea"],
            "dias": "Días 1, 3 (Camilla) | Día 2 (Polea)",
            "progreso": "15D: 3x12 | 30D: 3x10 | 45D: 4x12 | 60D: 4x10"
        },
        {
            "grupo": "Pantorrillas",
            "ejercicios": ["Sillón de Coser"],
            "dias": "Día 2",
            "progreso": "15D: 3x12 | 30D: 3x15 | 45D: 4x12 | 60D: 4x15"
        }
    ]

    # Renderizado de tarjetas de ejercicios
    tarjetas_ejercicios = []
    for item in rutina_data:
        ejercicios_list = [ft.Text(f"• {ej}", size=14, weight=ft.FontWeight.W_500) for ej in item["ejercicios"]]
        
        tarjeta = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text(item["grupo"], size=16, weight=ft.FontWeight.BOLD, color=ft.colors.INDIGO_800),
                                ft.Chip(label=ft.Text(item["dias"], size=11)),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Column(ejercicios_list),
                        ft.Container(
                            content=ft.Text(f"Progresión: {item['progreso']}", size=12, italic=True, color=ft.colors.GREY_700),
                            margin=ft.margin.only(top=5)
                        )
                    ]
                ),
                padding=12
            )
        )
        tarjetas_ejercicios.append(tarjeta)

    # Estructura principal de la vista
    page.add(
        header,
        ft.Text("Rutina de Entrenamiento", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_GREY_900),
        ft.Column(tarjetas_ejercicios)
    )

if __name__ == "__main__":
    ft.app(target=main)
