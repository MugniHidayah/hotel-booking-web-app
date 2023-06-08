import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash import dash_table
from dash.dependencies import Input, Output
import plotly.express as px 
import plotly.graph_objects as go
from app import app
import folium
from folium.plugins import HeatMap
import pandas as pd

booking = pd.read_csv('hotel_bookings.csv')

layout = html.Div(
    [
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Hotel Bookings Dashboard", style={'margin-bottom': '0px', 'color': 'white'})
                ])
            ],className="one third column", id="title1"),

            html.Div([
                html.P('Hotel', className='title-hotel', style = {'color': 'white'}),
                dcc.RadioItems(id = 'radio_items',
                                labelStyle = {},
                                value = 'Resort Hotel',
                                options = [{'label': i, 'value': i} for i in booking['hotel'].unique()],
                                style = {'color': 'black'}, className = 'radio'),
            ], className = "hotel", id = 'title3', style = {"margin-top": "25px"}),
        ], id = "header", className = "row flex-display box", style = {"margin-bottom": "25px"}),

        html.Div([
            html.Div([
                html.H4('Negara dari sebagian besar tamu yang datang', style = {'color': 'white'}),
                dcc.Graph(id = 'map',
                    config = {'displayModeBar': 'hover'}, style = {'height': '370px', 'width': '470px'}),
            ], className = 'create_container2', style = {'height': '500px', 'width': '500px'}),

            html.Div([
                html.H4('Tamu membayar kamar per malam', style = {'color': 'white', "margin-bottom": "47px"}),
                dcc.Graph(id = 'bar_chart',
                        config = {'displayModeBar': 'hover'}, style = {'height': '370px', 'width': '470px'}),

            ], className = 'create_container2', style = {'height': '500px', 'width': '500px'}),

            html.Div([
                html.H4('Harga hotel per malam selama satu tahun', style = {'color': 'white', "margin-bottom": "47px"}),
                dcc.Graph(id = 'line_chart',
                        config = {'displayModeBar': 'hover'}, style = {'height': '370px', 'width': '470px'}),

            ], className = 'create_container2', style = {'height': '500px', 'width': '500px'}),

            html.Div([
                html.H4('Bulan yang paling banyak pengunjung', style = {'color': 'white'}),
                dcc.Graph(id = 'line-chart-2',
                    config = {'displayModeBar': 'hover'}, style = {'height': '370px', 'width': '470px'}),
            ], className = 'create_container2', style = {'height': '500px', 'width': '500px'}),

            html.Div([
                html.H4('Lama waktu pengunjung tinggal di hotel', style = {'color': 'white'}),
                dcc.Graph(id = 'bar-chart-2',
                    config = {'displayModeBar': 'hover'}, style = {'height': '370px', 'width': '470px'}),
            ], className = 'create_container2', style = {'height': '500px', 'width': '500px'}),
        ], className='container-visualization'),
    ],
    style={"overflow": "auto"}
),


@app.callback(Output('map', 'figure'),
            [Input('radio_items', 'value')])
def update_graph(radio_items):
    if radio_items == 'Resort Hotel':
        country_guests = booking[booking['hotel'] == 'Resort Hotel']['country'].value_counts().reset_index()
        country_guests.columns = ['country', 'Guest']
        fig = px.choropleth(country_guests, locations = country_guests['country'],
                        color = country_guests['Guest'], hover_name = country_guests['country'])
        return fig
    
    else:
        country_guests = booking[booking['hotel'] == 'City Hotel']['country'].value_counts().reset_index()
        country_guests.columns = ['country', 'Guest']
        fig = px.choropleth(country_guests, locations = country_guests['country'],
                        color = country_guests['Guest'], hover_name = country_guests['country'])
        
        return fig
    
@app.callback(Output('bar_chart', 'figure'),
            [Input('radio_items', 'value')])
def update_graph(radio_items):
    if radio_items == 'Resort Hotel':
        data = booking[booking['hotel'] == 'Resort Hotel']
        fig = px.histogram(data_frame = data, x = 'reserved_room_type', y = 'adr', color = 'hotel', template = 'plotly')
    else:
        data = booking[booking['hotel'] == 'City Hotel']
        fig = px.histogram(data_frame = data, x = 'reserved_room_type', y = 'adr', color = 'hotel', template = 'plotly')
    return fig

@app.callback(Output('line_chart', 'figure'),
            [Input('radio_items', 'value')])
def update_graph(radio_items):
    if radio_items == 'Resort Hotel':
        data_resort = booking[(booking['hotel'] == 'Resort Hotel') & (booking['is_canceled'] == 0)]
        resort_hotel = data_resort.groupby(['arrival_date_month'])['adr'].mean().reset_index()
        resort_hotel.columns = ['Month', 'Price']
        fig = px.line(resort_hotel, x = 'Month', y = 'Price', template = 'plotly')
    else:
        data_city = booking[(booking['hotel'] == 'City Hotel') & (booking['is_canceled'] == 0)]
        city_hotel=data_city.groupby(['arrival_date_month'])['adr'].mean().reset_index()
        city_hotel.columns = ['Month', 'Price']
        fig = px.line(city_hotel, x = 'Month', y = 'Price', template = 'plotly')
    return fig

@app.callback(Output('line-chart-2', 'figure'),
            [Input('radio_items', 'value')])
def update_graph(radio_items):
    if radio_items == 'Resort Hotel':
        data_resort = booking[(booking['hotel'] == 'Resort Hotel') & (booking['is_canceled'] == 0)]
        resort_guests = data_resort['arrival_date_month'].value_counts().reset_index()
        resort_guests.columns=['Month','Guests']
        fig = px.line(resort_guests, x = 'Month', y = 'Guests', template='plotly')
    else:
        data_city = booking[(booking['hotel'] == 'City Hotel') & (booking['is_canceled'] == 0)]
        city_guests = data_city['arrival_date_month'].value_counts().reset_index()
        city_guests.columns=['Month','Guests']
        fig = px.line(city_guests, x = 'Month', y = 'Guests', template='plotly')
    return fig

@app.callback(Output('bar-chart-2', 'figure'),
            [Input('radio_items', 'value')])
def update_graph_1(radio_items):
    if radio_items == 'Resort Hotel':
        data = booking[booking['hotel'] == 'Resort Hotel']
        fig = px.histogram(data, x = 'stays_in_weekend_nights', y = 'is_canceled', color='hotel', template='plotly')
        fig.update_layout(
            xaxis_title="Total nights",
            yaxis_title="Guests",
        )
    else:
        data = booking[booking['hotel'] == 'City Hotel']
        fig = px.histogram(data, x = 'stays_in_weekend_nights', y = 'is_canceled', color='hotel', template='plotly')
        fig.update_layout(
            xaxis_title="Total nights",
            yaxis_title="Guests",
        )
    return fig