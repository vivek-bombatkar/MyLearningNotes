
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, State, Output, Event
from datetime import datetime
import blockChain as blockChain
import hashlib as hash

heading_one='Blockchain-backed analytics'
heading_two='Adding blockchain-based quality gates to data science projects'

inputFileHash=''
dataScienceModelHash=''
resultDataHash=''

input_data_set = ''
data_science_model = ''
result_data_set = ''

n_clicks_data_set_cnt=0
n_clicks_model_cnt=0
##### THE DASH PAGE START
app = dash.Dash(name=heading_one)
app.title = heading_one
app.scripts.config.serve_locally = True
app.config['suppress_callback_exceptions']=True

all_options = {
    'Data': [''],
    'model': [''],
    'Result': ['']
}


pre_style = {
    'whiteSpace': 'pre-wrap',
    'wordBreak': 'break-all',
    'whiteSpace': 'normal'
}

tab_style = {
    #'color': '#0074D9',
    'color': '#007dc3',
    'fontSize': '26px',
    'text-decoration': 'underline',
    'margin': '20px',
    'cursor': 'pointer',
    'fontFamily': 'Arial'
}

border_style = {
    'width': '50%',
    'lineHeight': '50px',
    'borderWidth': '1px',
    'borderStyle': 'dashed',
    'borderRadius': '5px',
    'textAlign': 'center',
    'margin': '10px'
}

drag_drop_style = {
    'fontSize': '22px',
    'fontFamily': 'Arial'
}

file_select_style = {
    'text-decoration': 'underline',
    'cursor': 'pointer',
    'fontFamily': 'Arial'
}

add_button_style = {
    'fontSize': '18px',
    'margin': '10px',
    'border-radius': '5px',
    'fontFamily': 'Arial'
}

enter_bc_id_style = {
    'fontSize': '18px',
    'width': '50%',
    'margin': '10px',
    'resize': 'none',
    'fontFamily': 'Arial'
}

hash_bc_id_style = {
    'fontSize': '18px',
    'width':'90%',
    'marginLeft': '5%',
#    'resize': 'none',
    'fontFamily': 'Arial'
}

app.layout = html.Div(children=[
    html.Img(src='https://github.com/vivek-bombatkar/MyLearningNotes/raw/master/blockchain/static/logo-gkf.png',style={'width':'5%', 'marginLeft': '92%', 'marginTop': '3%'}),
    html.H1(children=heading_one, style={'color': '#666666','textAlign': 'center'}),
    #html.Hr(),
    dcc.Location(id='url'),
    dcc.Link('Data', href='/DataBlock', style=tab_style),
    dcc.Link('Model', href='/ModelBlock', style=tab_style),
    dcc.Link('Result', href='/ResultBlock', style=tab_style),
    html.Div([

        # Tab 1
        html.Div(
            id='DataBlock',
            style={'display': 'none'},
            children=[
                html.H3('Data'),
                dcc.Upload(
                    id='upload_input_data_set',
                    children=html.Div([
                        'Train/Input Data Set - Drag and Drop or ',
                        html.A('Click to Select a File', style=file_select_style )
                    ], style=drag_drop_style),
                    style=border_style
                ),
                html.Div(id='input_data_set', style={'margin': '10px'}),
                html.Div(id='file_hash_data_set', style={'margin': '10px'}),
                html.Button(id='button_data_set', children='Add to blockchain', n_clicks=0, style=add_button_style),
                html.Hr(),
                html.Div(id=' '),
            ]
        ),

        # Tab 2
        html.Div(
            id='ModelBlock',
            style={'display': 'none'},
            children=[
                html.H3('Model'),
                dcc.Upload(
                    id='upload_data_science_model',
                    children=html.Div([
                        'Data Science Model - Drag and Drop or ',
                        html.A('Click to Select a File', style=file_select_style)
                    ], style=drag_drop_style),
                    style=border_style
                ),
                html.Div([dcc.Textarea(id='train_data_tx_id', placeholder='Enter Blockchain Transaction ID for Training data...', value='', rows=1, style=enter_bc_id_style)]),
                html.Div(id='data_science_model', style={'margin': '10px'}),
                html.Div(id='file_hash_model', style={'margin': '10px'}),
                html.Button(id='Button_model', children='Add to blockchain', n_clicks=0, style=add_button_style),
                html.Hr(),
                html.Div(id=' '),
            ]
        ),

        # Tab 3
        html.Div(
            id='ResultBlock',
            style={'display': 'none'},
            children=[
                html.H3('Result'),
                dcc.Upload(
                    id='upload_result_data_set',
                    children=html.Div([
                        'Result Data Set - Drag and Drop or ',
                        html.A('Click to Select a File', style=file_select_style)
                    ], style=drag_drop_style),
                    style=border_style
                ),
                html.Div([dcc.Textarea(id='model_tx_id', placeholder='Enter Blockchain Transaction ID for Model...', rows=1, style=enter_bc_id_style)]),
                html.Div([dcc.Textarea(id='input_data_tx_id', placeholder='Enter Blockchain Transaction ID for Input data...',rows=1, style=enter_bc_id_style)]),
                html.Div(id='result_data_set', style={'margin': '10px'}),
                html.Div(id='file_hash_result_data_set', style={'margin': '10px'}),
                html.Button(id='Button_result_data_set', children='Add to blockchain', n_clicks=0, style=add_button_style),
                html.Hr(),
                html.Div(id=' '),
            ]
        ),
    ]),
    html.Label(' '),
    html.Div(id='output_bc'),

    html.Pre(id='output', className='six columns')
],style={'marginLeft': '1%'})
##### THE DASH PAGE ENDS
app.css.append_css({
    "external_url": "https://rawgit.com/vivek-bombatkar/MyLearningNotes/master/blockchain/static/site.css"
})

def generate_display_tab(tab):
    def display_tab(pathname):
        if tab == 'DataBlock' and (pathname is None or pathname == '/'):
            return {'display': 'block'}
        elif pathname == '/{}'.format(tab):
            return {'display': 'block'}
        else:
            return {'display': 'none'}
    return display_tab


for tab in ['DataBlock', 'ModelBlock', 'ResultBlock']:
    app.callback(Output(tab, 'style'), [Input('url', 'pathname')])(
        generate_display_tab(tab)
    )

#show file hash start#
@app.callback(Output('file_hash_data_set', 'children'),
              [Input('upload_input_data_set', 'filename'),Input('upload_input_data_set', 'contents')])
def upload_data_science_model(filename,contents):
    global inputFileHash
    inputFileHash = hash.sha256(contents.encode('ascii')).hexdigest()
    return html.Div([ html.H4(inputFileHash)])

@app.callback(Output('file_hash_model', 'children'),
              [Input('upload_data_science_model', 'filename'),Input('upload_data_science_model', 'contents')])
def upload_data_science_model(filename,contents):
    global dataScienceModelHash
    dataScienceModelHash = hash.sha256(contents.encode('ascii')).hexdigest()
    return html.Div([html.H4(dataScienceModelHash)])

@app.callback(Output('file_hash_result_data_set', 'children'),
              [Input('upload_result_data_set', 'filename'),Input('upload_result_data_set', 'contents')])
def upload_data_science_model(filename,contents):
    global resultDataHash
    resultDataHash = hash.sha256(contents.encode('ascii')).hexdigest()
    return html.Div([html.H4(resultDataHash)])
#show file hash start#
#show file name start#
@app.callback(Output('input_data_set', 'children'),
              [Input('upload_input_data_set', 'filename') , Input('upload_input_data_set', 'contents')])
def upload_input_data_set(filename, contents):
    global input_data_set
    input_data_set = contents
    return html.Div([html.H4(filename)])

@app.callback(Output('data_science_model', 'children'),
              [Input('upload_data_science_model', 'filename'),Input('upload_data_science_model', 'contents')])
def upload_data_science_model(filename,contents):
    global data_science_model
    data_science_model = contents
    return html.Div([html.H4(filename)])

@app.callback(Output('result_data_set', 'children'),
              [Input('upload_result_data_set', 'filename'),Input('upload_result_data_set', 'contents')])
def upload_data_science_model(filename,contents):
    global result_data_set
    result_data_set = contents
    return html.Div([html.H4(filename)])
#show file name#
#add to blockchain
@app.callback(
    Output('output_bc', 'children'),
    [Input('button_data_set', 'n_clicks'), Input('Button_model', 'n_clicks'), Input('Button_result_data_set', 'n_clicks')],
    [State('train_data_tx_id', 'value'),State('model_tx_id', 'value'),State('input_data_tx_id', 'value')])
def add_to_blockchain(n_clicks_data_set,n_clicks_model,n_clicks_result_data_set,value_train_data_tx_id,value_model_tx_id,value_input_data_tx_id):
    global n_clicks_data_set_cnt
    global n_clicks_model_cnt

    if n_clicks_data_set == 0 and n_clicks_model == 0 and n_clicks_result_data_set == 0:
        return ''
    valid_transaction = False
    prev_block = bc[len(bc)-1]

    if n_clicks_data_set_cnt != n_clicks_data_set:
        data = "{{ hash_data: {} }}".format(inputFileHash)
        valid_transaction = True
    elif n_clicks_model_cnt != n_clicks_model:
        data = "{{ hash_model: {}, transaction_id_training_data: {} }}".format(dataScienceModelHash,value_train_data_tx_id)
        valid_train_data_tx_id = blockChain.validateTransactionID(value_train_data_tx_id, bc)
        if valid_train_data_tx_id :
            valid_transaction = True
    else:
        data = "{{ hash_result_data: {}, transaction_id_model: {}, transaction_id_input_data: {} }}".format(resultDataHash,value_model_tx_id,value_input_data_tx_id )
        valid_model_tx_id = blockChain.validateTransactionID(value_model_tx_id, bc)
        valid_input_data_tx_id = blockChain.validateTransactionID(value_input_data_tx_id, bc)
        if valid_model_tx_id and valid_input_data_tx_id:
            valid_transaction = True

    if valid_transaction:
        new_block = blockChain.getNextBlock(prev_block, data)
        bc.append(new_block)

    n_clicks_data_set_cnt = n_clicks_data_set
    n_clicks_model_cnt = n_clicks_model


    return html.Div([
#        html.Div([dcc.Textarea(value="Block added to Transaction_ID {} ".format(str(bc[len(bc)-1].Transaction_ID)) ,id='dynamic-output',style={'width': '100%'})]),
#        html.Div([html.H6("Index : Timestamp, Data", style={'width': '100%'})]),
        html.Div([
            dcc.Textarea(
                value='{} : {} , {} '.format(block.Transaction_ID,block.timestamp.strftime("%Y-%m-%d %H:%M:%S"),block.data),
                id='input-{}'.format(block.Transaction_ID),
                rows=1, spellCheck=False, readOnly=True, style=hash_bc_id_style
            )
            for block in bc
        ]),
        html.Div(id='dynamic-output')
    ])
if __name__ == '__main__':
    #add the very first block to the blockchain
    button_n_clicks = 0
    bc = [blockChain.getGenesisBlock()]
    app.run_server(debug=True)
