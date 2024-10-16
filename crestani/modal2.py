import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from modal_streamlit_vmateo import Modal


# Dados de exemplo de notas fiscais
df_notas_fiscais = pd.DataFrame({
    'ID Nota Fiscal': [1001, 1002, 1003, 1004, 1005],
    'Data': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19'],
    'Cliente': ['Cliente A', 'Cliente B', 'Cliente C', 'Cliente D', 'Cliente E'],
    'Valor Total': [1500.00, 2500.00, 3000.00, 4000.00, 1200.00],
    'Status': ['Paga', 'Pendente', 'Paga', 'Paga', 'Pendente']
})

# Dados de exemplo de itens de notas fiscais
itens_notas_fiscais = {
    1001: pd.DataFrame({
        'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E'],
        'Quantidade': [2, 3, 1, 0, 0],
        'Preço Unitário': [500.00, 200.00, 300.00, 0, 0],
        'Desconto': [0, 0, 10, 0, 0],
        'Total': [1000.00, 600.00, 290.00, 0, 0]
    }),
    1002: pd.DataFrame({
        'Produto': ['Produto D', 'Produto E', 'Produto F', 'Produto G', 'Produto H'],
        'Quantidade': [5, 2, 0, 0, 0],
        'Preço Unitário': [500.00, 1000.00, 0, 0, 0],
        'Desconto': [50, 0, 0, 0, 0],
        'Total': [2250.00, 2000.00, 0, 0, 0]
    }),
    1003: pd.DataFrame({
        'Produto': ['Produto F', 'Produto G', 'Produto H', 'Produto I', 'Produto J'],
        'Quantidade': [1, 1, 2, 0, 0],
        'Preço Unitário': [1000.00, 200.00, 700.00, 0, 0],
        'Desconto': [0, 0, 0, 0, 0],
        'Total': [1000.00, 200.00, 1400.00, 0, 0]
    }),
    1004: pd.DataFrame({
        'Produto': ['Produto I', 'Produto J', 'Produto K', 'Produto L', 'Produto M'],
        'Quantidade': [3, 4, 0, 0, 0],
        'Preço Unitário': [800.00, 500.00, 0, 0, 0],
        'Desconto': [0, 0, 0, 0, 0],
        'Total': [2400.00, 2000.00, 0, 0, 0]
    }),
    1005: pd.DataFrame({
        'Produto': ['Produto K', 'Produto L', 'Produto M', 'Produto N', 'Produto O'],
        'Quantidade': [1, 2, 3, 0, 0],
        'Preço Unitário': [1200.00, 1500.00, 200.00, 0, 0],
        'Desconto': [100, 0, 20, 0, 0],
        'Total': [1100.00, 3000.00, 580.00, 0, 0]
    })
}

modal = Modal(
    title="Modal", 
    key="modal",
    padding=20,    # default value
    max_width=1200,  # default value
)

# Título da aplicação
st.title("Tabela de Notas Fiscais")

open_modal = st.button("Abrir Modal")

# Configurar as opções da tabela com AgGrid
# gb = GridOptionsBuilder.from_dataframe(df_notas_fiscais)
# gb.configure_selection(selection_mode="single", use_checkbox=True)  # Permitir seleção única
# grid_options = gb.build()

# # Exibir a tabela de notas fiscais
# response = AgGrid(
#     df_notas_fiscais,
#     gridOptions=grid_options,
#     height=300,
#     # update_mode=,
#     fit_columns_on_grid_load=True,
#     allow_unsafe_jscode=True,  # Permitindo jscode
#     theme='material'  # Tema opcional
# )

# Verificar se uma linha foi selecionada
# selected_rows = response.get('selected_rows', [])

def show_modal():
    modal = Modal(
        title="Demo Modal", 
        key="demo-modal",
        padding=20,    # default value
        max_width=1200,  # default value
    )

    row_select = st.session_state.df.selection.rows[0]

    # if row_select:
    #     modal.open()
    
    # if modal.is_open():
    #     with modal.container():
    #         st.write("Text goes here")
    #         btn_fechar = st.button("Fechar Modal")
    #         if btn_fechar:
    #             modal.close()


response = st.dataframe(
    df_notas_fiscais,
    use_container_width=True,
    selection_mode='single-row',
    on_select=show_modal,
    key="df"
)



# Ajuste para diferentes retornos dependendo da versão do st_aggrid
# if isinstance(selected_rows, pd.DataFrame):
#     if not selected_rows.empty:
#         selected_nota = selected_rows.iloc[0]
#         nota_id = selected_nota['ID Nota Fiscal']
#         encontrada = True
#     else:
#         nota_id = None
#         encontrada = False
# elif isinstance(selected_rows, list):
#     if len(selected_rows) > 0:
#         selected_nota = selected_rows[0]
#         nota_id = selected_nota.get('ID Nota Fiscal')
#         encontrada = True
#     else:
#         nota_id = None
#         encontrada = False
# else:
#     nota_id = None
#     encontrada = False




# st.write(encontrada)
# st.write(open_modal)

# if row_select:
#     modal.open()
#     st.write(modal)
#     st.write('Modal Aberto')
# else:
#     st.write('Modal Fechado')
    # Usar um Expander como modal
    # with st.expander(f"Itens da Nota Fiscal {nota_id}", expanded=True):
    #     st.write(f"### Itens da Nota Fiscal {nota_id}")
    #     st.table(itens_notas_fiscais[nota_id])

# if modal.is_open():
#     with modal.container():
#         st.write("Text goes here")
#         btn_fechar = st.button("Fechar")
#         if btn_fechar:
#             modal.close()
