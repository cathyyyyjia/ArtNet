import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import style_transfer


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


styles = {
    "Aoyama - Detective Conan": "Aoyama - Detective Conan",
    "Gao Jianfu - Cotton Roses and Mandarin Ducks": "Gao Jianfu - Cotton Roses and Mandarin Ducks",
    "Hokusai - The Great Wave off Kanagawa": "Hokusai - The Great Wave off Kanagawa",
    "Monet - Camille Monet On Her Deathbed": "Monet - Camille Monet On Her Deathbed",
    "Monet - Haystack": "Monet - Haystack",
    "Picasso - The Dream": "Picasso - The Dream",
    "Qi Baishi - Lotus Flowers and Wild Duck": "Qi Baishi - Lotus Flowers and Wild Duck",
    "Rousseau - Myself": "Rousseau - Myself",
    "van Gogh - Starry Night": "van Gogh - Starry Night"
}


app.layout = html.Div([
    html.H1('ArtNet: Artistic Style Transfer Network', style={'textAlign': 'center'}),
    html.H3('Mengying Bi (mybi), Cathy Jia (cathyjia), Geoffrey Li (geoffli)', style={'textAlign': 'center'}),
    html.Hr(),

    # drag or upload input image
    html.Div(
        children=[
            dcc.Upload(
                id='input-image',
                children=html.Div(['Drag and Drop or ', html.Button('Select a File')]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'backgroundColor': '#F7F3E3'
                },
                accept='image/*'
            )
        ],
        style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}
    ),

    # style options
    html.Div(
        children=[
            html.Label([
                "Choose a Style",
                dcc.Dropdown(
                    id='choose-style',
                    options=[
                        {'label': label, 'value': value} for (label, value) in styles.items()
                    ],
                    value="Hokusai - The Great Wave off Kanagawa",  # initial value
                )
            ]),
            html.Label([
                "Preserve Color",
                dcc.RadioItems(
                    id='preserve-color',
                    options=[
                        {'label': 'Yes', 'value': 'True'},
                        {'label': 'No', 'value': 'False'},
                    ],
                    labelStyle={'display': 'inline-block', 'text-align': 'justify'},
                    value='False'
                )
            ]),
        ],
        style={'width': '48%', 'display': 'inline-block', 'marginLeft': '30px', 'verticalAlign': 'top'}
    ),

    html.Hr(),

    # display input image
    html.Div(
        id='display-input-image',
        style={'width': '50%', 'display': 'inline-block'}
    ),

    # display output image
    html.Div(
        style={'width': '50%', 'display': 'inline-block', 'verticalAlign': 'top'},
        id='display-output-image'
    ),

], style={'padding': '10px'})


@app.callback(Output('display-input-image', 'children'),
              [Input('input-image', 'contents')],
              [State('input-image', 'filename')])
def display_input(contents, filename):
    if contents is not None:
        children = [
            html.H5('Input Image: ' + filename),
            html.Img(src=contents, style={'width': '100%'}),
        ]
        return children


@app.callback(Output('display-output-image', 'children'),
              [Input('input-image', 'filename'),
               Input('choose-style', 'value'),
               Input('preserve-color', 'value')])
def display_output(input_image_name, style, color):
    if input_image_name is not None:
        output_image = style_transfer.transfer(input_image_name, style, color)
        children = [
            html.H5('Output Image (' + style + ')'),
            html.Img(
                src='data:image/png;base64,{}'.format(output_image.decode()),
                style={'width': '100%'}
            ),
        ]
        return children


if __name__ == '__main__':
    app.run_server(debug=False)
