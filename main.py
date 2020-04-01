#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_daq as daq
import dash_table

import pandas as pd

from scraper import amzscraper, fbscraper, twscraper


# In[2]:


external_stylesheets = ['htthtml//codepen.io/chriddyp/pen/bWLwgP.css']


# In[3]:


siaApp = dash.Dash(__name__, external_stylesheets=external_stylesheets)
siaApp.config['suppress_callback_exceptions'] = True


# In[4]:


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


# In[5]:


tab_styles = {
    'height': '44px'
}

tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}


# In[6]:


siaApp.layout = html.Div(style = {'backgroundColor': colors['background']}, children = [
    html.H1(children = 'Social Impact Analysis(SIA) Dashboard',
           style = {'textAlign': 'center',
                   'color': colors['text']}
           ),
    
    html.Div(children = 'A Web Application Framework',
            style = {'textAlign': 'center',
                    'color': colors['text']}
            ),
    
    dcc.Tabs(id = "tabs-styled-with-inline", value = 'scraper', children = [
        dcc.Tab(label = 'Scraper', value = 'scraper', style = tab_style, selected_style = tab_selected_style, children = [
            html.Label('Please select Platform from the Dropdown', style = {'color': colors['text']}),
            html.Div([dcc.Dropdown(id = 'platform-input', options=[
                {'label': 'Amazon', 'value': 'amazon'},
                {'label': 'Facebook', 'value': 'facebook'},
                {'label': 'Twitter', 'value': 'twitter'}],
                                   value = 'amazon', style = {'color': colors['text']})]),
            html.Br(),
            
            html.Label('Please enter the Keyword here', style = {'color': colors['text']}),
            html.Div(dcc.Textarea(id = 'keyword-input', placeholder = 'Type here', style = {'width': '100%'})),
            html.Br(),
            
            html.Label('Please enter No. of Pages here', style = {'color': colors['text']}),
            html.Div(daq.NumericInput(id = 'pages-input', min = 1, max = 1000, value = 10, size = 120), 
                     style = {'color': colors['text']}),
            html.Br(),
            html.Div([dbc.Button('Submit', color = "primary", id = 'button', className = "mr-1", block = True),
                      html.Span(id = "button-output", style={"vertical-align": "middle"}),
                     ]),
            html.Br(),
            
            html.Div(id = 'scraper-output', style = {'color': colors['text']})
        ]),
        dcc.Tab(label = 'Preprocessing', value = 'preprocessing', style = tab_style, selected_style = tab_selected_style),
        dcc.Tab(label = 'Features Extraction', value = 'feature_extraction', style = tab_style, selected_style = tab_selected_style),
        dcc.Tab(label = 'Clustering', value = 'clustering', style = tab_style, selected_style = tab_selected_style),
        dcc.Tab(label = 'Visualization', value = 'visualization', style = tab_style, selected_style = tab_selected_style)
    ], style = tab_styles),
    html.Div(id = 'tabs-content-inline', style = {'color': colors['text']})
])

@siaApp.callback(Output('tabs-content-inline', 'children'),
                [Input('tabs-styled-with-inline', 'value')])
def render_content(tab):
    if tab == 'scraper':
        return html.Div([
            html.H3('Platform Text'),
            ])
    elif tab == 'preprocessing':
        return html.Div([
            html.H3('Include Preprocessing here')
        ])
    elif tab == 'feature_extraction':
        return html.Div([
            html.H3('Include Feature Extraction here')
        ])
    elif tab == 'clustering':
        return html.Div([
            html.H3('Include Clustering here')
        ])
    elif tab == 'visualization':
        return html.Div([
            html.H3('Include Visualization here')
        ])

@siaApp.callback([Output('scraper-output', 'children'),Output('button-output', 'children')],
                 [Input('button', 'n_clicks')],
                 [State('platform-input', 'value'),State('keyword-input', 'value'), State('pages-input', 'value')])
def update_output(n_clicks, platform, keyword, pages):
    return 'The selected Platform is "{}" with keyword "{}" & No. of Pages are {}'.format(platform, keyword, pages),             'and the button has been clicked {} times'.format(n_clicks)


# In[7]:


if __name__ == '__main__':
    siaApp.run_server()