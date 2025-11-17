import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1500x750")
app.title("Interface Modelo")

# --- CORES EXTRAÍDAS DA IMAGEM ---
COR_BG_TOTAL = "#d8d9dd"         # fundo geral
COR_QUADRO = "#cfd0d4"           # quadros internos
COR_CINZA_ESC = "#8f9092"        # áreas cinza escuras
COR_CINZA_MED = "#a0a1a4"        # área central
COR_BOTAO = "#e8e8e8"            # botões 20/03
COR_BOTAO_TXT = "#5a5a5a"
COR_TITULO = "#eeeeee"
COR_ABA_BG = "#d1d2d5"
COR_ABA_SELEC = "#bfc0c4"

# =============================
#   QUADRO PRINCIPAL EXTERNO
# =============================
main = ctk.CTkFrame(app, fg_color=COR_BG_TOTAL, corner_radius=0)
main.pack(fill="both", expand=True)

main.grid_columnconfigure(0, weight=0)
main.grid_columnconfigure(1, weight=1)
main.grid_columnconfigure(2, weight=1)
main.grid_rowconfigure(0, weight=1)

# =============================
#   COLUNA ESQUERDA
# =============================
left = ctk.CTkFrame(main, fg_color=COR_QUADRO, corner_radius=8)
left.grid(row=0, column=0, sticky="nsw", padx=8, pady=8)

# título “ARQUIVOS”
label_title = ctk.CTkLabel(left,
                           text="ARQUIVOS",
                           font=("Segoe UI", 18, "bold"),
                           text_color="#666")
label_title.pack(anchor="w", padx=12, pady=(8, 6))

# scroll da lista
scroll = ctk.CTkScrollableFrame(left,
                                width=150,
                                fg_color=COR_BG_TOTAL,
                                corner_radius=10)
scroll.pack(fill="y", expand=True, padx=8, pady=8)

# botões “20/03”
for i in range(22):
    ctk.CTkButton(scroll,
                  text="20/03",
                  fg_color=COR_BOTAO,
                  hover_color="#dcdcdc",
                  text_color=COR_BOTAO_TXT,
                  corner_radius=5,
                  height=32).pack(fill="x", pady=4, padx=4)

# =============================
#   ÁREA CENTRAL CINZA
# =============================
center = ctk.CTkFrame(main, fg_color=COR_CINZA_MED, corner_radius=10)
center.grid(row=0, column=1, sticky="nsew", padx=8, pady=8)

# =============================
#   PAINEL DIREITO
# =============================
right = ctk.CTkFrame(main, fg_color=COR_QUADRO, corner_radius=8)
right.grid(row=0, column=2, sticky="nsew", padx=8, pady=8)

right.grid_rowconfigure(1, weight=1)
right.grid_columnconfigure(0, weight=1)

# ---------------------------
#   TABS EXATAS DA IMAGEM
# ---------------------------
tab = ctk.CTkTabview(right,
                     fg_color=COR_ABA_BG,
                     segmented_button_fg_color=COR_ABA_BG,
                     segmented_button_selected_color=COR_ABA_SELEC,
                     segmented_button_selected_hover_color=COR_ABA_SELEC,
                     segmented_button_unselected_color=COR_ABA_BG,
                     segmented_button_unselected_hover_color=COR_ABA_BG,
                     corner_radius=10)

tab.grid(row=0, column=0, sticky="ew", padx=10, pady=(5, 2))

tab_ai = tab.add("ANÁLISE COM IA")
tab_info = tab.add("INFORMAÇÕES DO ARQUIVO")

# ---------------------------
#   TÍTULO “NOME ARQUIVO”
# ---------------------------
label_name = ctk.CTkLabel(right,
                          text="NOME ARQUIVO",
                          font=("Segoe UI", 28),
                          text_color=COR_TITULO)
label_name.grid(row=0, column=0, pady=(60, 10))

# ---------------------------
#   QUADRO GRANDE DIREITA
# ---------------------------
right_box = ctk.CTkFrame(right, fg_color=COR_CINZA_ESC, corner_radius=10)
right_box.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

app.mainloop()
