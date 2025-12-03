import os
import base64

def save_graph_to_file(graph):
    """Salva a imagem do grafo em `assets/graph.png`."""

    # obtém os dados da imagem (bytes ou base64 string)
    image_data = graph.get_graph().draw_mermaid_png()

    # garante a pasta `assets`
    assets_dir = 'assets'
    os.makedirs(assets_dir, exist_ok=True)
    out_path = os.path.join(assets_dir, 'graph.png')

    # converte para bytes se necessário
    if isinstance(image_data, bytes):
        data = image_data
    elif isinstance(image_data, str):
        try:
            data = base64.b64decode(image_data)
        except Exception as e:
            raise ValueError('`draw_mermaid_png()` retornou str não-base64 válida') from e
    else:
        raise TypeError(f'Tipo inesperado para image_data: {type(image_data)}')

    # grava o arquivo em modo binário
    with open(out_path, 'wb') as f:
        f.write(data)

