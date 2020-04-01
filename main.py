#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_daq as daq

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
            html.Div([dcc.Dropdown(id = 'platform-input', options=[
                {'label': 'Amazon', 'value': 'amazon'},
                {'label': 'Facebook', 'value': 'facebook'},
                {'label': 'Twitter', 'value': 'twitter'}],
                                   value = 'amazon', style = {'color': colors['text']}),
                      html.Button('Submit', id = 'button'),
                      html.Div(id = 'platform-output', style = {'color': colors['text']})])
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

@siaApp.callback(Output('platform-output', 'children'),
                 [Input('button', 'n_clicks')],
                 [State('platform-input', 'value')])
def update_output(n_clicks, value):
    return 'The selected Platform is "{}" with keyword "" & No. of Pages are ""             and the button has been clicked {} times'.format(value, n_clicks)


# In[ ]:


if __name__ == '__main__':
    siaApp.run_server()

