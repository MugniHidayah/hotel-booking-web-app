import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
from app import app
from datetime import date

layout = html.Div([
    html.Div(
        [
            html.H1(["Harga"], id="harga"),
            html.H3(["Beberapa harga Hotel dan Tipe Kamar."])
        ],
        className="text-center mb-5 text-white mt-5"
    ),
    
    html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(html.Div(
                        dbc.Card(
                            [
                                dbc.CardImg(src="/assets/standard.png", top=True),
                                dbc.CardBody(
                                    [
                                        html.H4("Standard Room", className="card-title text-white"),
                                        html.P(
                                            "Standard Room merupakan kelas kamar terbawah dan hanya memiliki fasilitas yang terbatas,"
                                            " seperti tempat tidur, AC, TV, perlengkapan mandi, dan air minum. "
                                            "Ada yang memberikan kasur model single bed, queen size, atau bahkan king size.",
                                            className="card-text text-white mb-4",
                                        ),
                                        html.P('Rp. 500.000 / Malam', className='text-white mb-4'),
                                        html.Div(
                                            [
                                                dbc.Button("Booking", id="open-centered-1"),
                                                dbc.Modal(
                                                    [
                                                        dbc.ModalHeader(dbc.ModalTitle("Standard Room", className='text-white'), close_button=True),
                                                        dbc.ModalBody(dbc.Row(
                                                                        [
                                                                            dbc.Label("Tanggal Masuk", html_for="dateinput1", width=2),
                                                                            dbc.Col(
                                                                                dcc.DatePickerSingle(
                                                                                    id='my-date-picker-single',
                                                                                    min_date_allowed=date(1995, 8, 5),
                                                                                    max_date_allowed=date(2050, 12, 31),
                                                                                    initial_visible_month=date(2023, 1, 6),
                                                                                    date=date(2023, 1, 6)
                                                                                ),
                                                                                width=10,
                                                                            ),
                                                                            dbc.Label("Tanggal Keluar", html_for="dateoutput1", width=2),
                                                                            dbc.Col(
                                                                                dcc.DatePickerSingle(
                                                                                    id='my-date-picker-single',
                                                                                    min_date_allowed=date(1995, 8, 5),
                                                                                    max_date_allowed=date(2050, 12, 31),
                                                                                    initial_visible_month=date(2023, 1, 6),
                                                                                    date=date(2023, 1, 6)
                                                                                ),
                                                                                width=10,
                                                                            ),
                                                                            dbc.Label("Dewasa", html_for="adult1", width=2),
                                                                            dbc.Col(
                                                                                dbc.Input(
                                                                                    type="number", id="adult1", placeholder="", className="mb-4"
                                                                                ),
                                                                                width=10,
                                                                            ),
                                                                            dbc.Label("Anak-anak", html_for="children1", width=2),
                                                                            dbc.Col(
                                                                                dbc.Input(
                                                                                    type="number", id="children1", placeholder=""
                                                                                ),
                                                                                width=10,
                                                                            ),
                                                                        ],
                                                                        className="mb-3",
                                                                    ), 
                                                                    className='text-white'
                                                                    ),
                                                        dbc.ModalFooter(
                                                            dbc.Button(
                                                                "Booking",
                                                                id="close-centered-1",
                                                                className="ms-auto",
                                                                n_clicks=0,
                                                            )
                                                        ),
                                                    ],
                                                    id="modal-centered-1",
                                                    centered=True,
                                                    is_open=False,
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                            ],
                            style={"width": "25rem"},
                        )
                    )),
                    dbc.Col(html.Div(
                        dbc.Card(
                            [
                                dbc.CardImg(src="/assets/superior.png", top=True),
                                dbc.CardBody(
                                    [
                                        html.H4("Superior Room", className="card-title text-white"),
                                        html.P(
                                            "Superior Room menawarkan ukuran ruangan yang lebih luas "
                                            "layanan dan perlengkapan menginap Superior Room hampir sama dengan Standard Room. "
                                            "Hanya pengunjung akan diberikan opsi memilih kasur ukuran twin bed atau double bed.",
                                            className="card-text text-white mb-4",
                                        ),
                                        html.P('Rp. 1.000.000 / Malam', className='text-white mb-4'),
                                        html.Div(
                                            [
                                                dbc.Button("Booking", id="open-centered-2"),
                                                dbc.Modal(
                                                    [
                                                        dbc.ModalHeader(dbc.ModalTitle("Standard Room", className='text-white'), close_button=True),
                                                        dbc.ModalBody(dbc.Row(
                                                                        [
                                                                            dbc.Label("Tanggal Masuk", html_for="dateinput2", width=2),
                                                                            dbc.Col(
                                                                                dcc.DatePickerSingle(
                                                                                    id='my-date-picker-single',
                                                                                    min_date_allowed=date(1995, 8, 5),
                                                                                    max_date_allowed=date(2050, 12, 31),
                                                                                    initial_visible_month=date(2023, 1, 6),
                                                                                    date=date(2023, 1, 6)
                                                                                ),
                                                                                width=10,
                                                                            ),
                                                                            dbc.Label("Tanggal Keluar", html_for="dateoutput2", width=2),
                                                                            dbc.Col(
                                                                                dcc.DatePickerSingle(
                                                                                    id='my-date-picker-single',
                                                                                    min_date_allowed=date(1995, 8, 5),
                                                                                    max_date_allowed=date(2050, 12, 31),
                                                                                    initial_visible_month=date(2023, 1, 6),
                                                                                    date=date(2023, 1, 6)
                                                                                ),
                                                                                width=10,
                                                                            ),
                                                                            dbc.Label("Dewasa", html_for="adult2", width=2),
                                                                            dbc.Col(
                                                                                dbc.Input(
                                                                                    type="number", id="adult2", placeholder="", className="mb-4"
                                                                                ),
                                                                                width=10,
                                                                            ),
                                                                            dbc.Label("Anak-anak", html_for="children2", width=2),
                                                                            dbc.Col(
                                                                                dbc.Input(
                                                                                    type="number", id="children2", placeholder=""
                                                                                ),
                                                                                width=10,
                                                                            ),
                                                                        ],
                                                                        className="mb-3",
                                                                    ), 
                                                                    className='text-white'
                                                                    ),
                                                        dbc.ModalFooter(
                                                            dbc.Button(
                                                                "Booking",
                                                                id="close-centered-2",
                                                                className="ms-auto",
                                                                n_clicks=0,
                                                            )
                                                        ),
                                                    ],
                                                    id="modal-centered-2",
                                                    centered=True,
                                                    is_open=False,
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                            ],
                            style={"width": "25rem",},
                        )
                    )),
                    dbc.Col(html.Div(
                        dbc.Card(
                            [
                                dbc.CardImg(src="/assets/deluxe.png", top=True),
                                dbc.CardBody(
                                    [
                                        html.H4("Superior Room", className="card-title text-white"),
                                        html.P(
                                            "Superior Room menawarkan ukuran ruangan yang lebih luas "
                                            "layanan dan perlengkapan menginap Superior Room hampir sama dengan Standard Room. "
                                            "Hanya pengunjung akan diberikan opsi memilih kasur ukuran twin bed atau double bed.",
                                            className="card-text text-white mb-4",
                                        ),
                                        html.P('Rp. 2.000.000 / Malam', className='text-white mb-4'),
                                        html.Div(
                                            [
                                                dbc.Button("Booking", id="open-centered-3"),
                                                dbc.Modal(
                                                    [
                                                        dbc.ModalHeader(dbc.ModalTitle("Standard Room", className='text-white'), close_button=True),
                                                        dbc.ModalBody(dbc.Row(
                                                                        [
                                                                            dbc.Label("Tanggal Masuk", html_for="dateinput3", width=2),
                                                                            dbc.Col(
                                                                                dcc.DatePickerSingle(
                                                                                    id='my-date-picker-single',
                                                                                    min_date_allowed=date(1995, 8, 5),
                                                                                    max_date_allowed=date(2050, 12, 31),
                                                                                    initial_visible_month=date(2023, 1, 6),
                                                                                    date=date(2023, 1, 6)
                                                                                ),
                                                                                width=10,
                                                                            ),
                                                                            dbc.Label("Tanggal Keluar", html_for="dateoutput3", width=2),
                                                                            dbc.Col(
                                                                                dcc.DatePickerSingle(
                                                                                    id='my-date-picker-single',
                                                                                    min_date_allowed=date(1995, 8, 5),
                                                                                    max_date_allowed=date(2050, 12, 31),
                                                                                    initial_visible_month=date(2023, 1, 6),
                                                                                    date=date(2023, 1, 6)
                                                                                ),
                                                                                width=10,
                                                                            ),
                                                                            dbc.Label("Dewasa", html_for="adult3", width=2),
                                                                            dbc.Col(
                                                                                dbc.Input(
                                                                                    type="number", id="adult3", placeholder="", className="mb-4"
                                                                                ),
                                                                                width=10,
                                                                            ),
                                                                            dbc.Label("Anak-anak", html_for="children3", width=2),
                                                                            dbc.Col(
                                                                                dbc.Input(
                                                                                    type="number", id="children3", placeholder=""
                                                                                ),
                                                                                width=10,
                                                                            ),
                                                                        ],
                                                                        className="mb-3",
                                                                    ), 
                                                                    className='text-white'
                                                                    ),
                                                        dbc.ModalFooter(
                                                            dbc.Button(
                                                                "Booking",
                                                                id="close-centered-3",
                                                                className="ms-auto",
                                                                n_clicks=0,
                                                            )
                                                        ),
                                                    ],
                                                    id="modal-centered-3",
                                                    centered=True,
                                                    is_open=False,
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                            ],
                            style={"width": "25rem",},
                        )
                    )),
                ]
            ),
        ],
        className="pad-row d-flex justify-content-center align-items-center mb-5",
    )
])

@app.callback(
    Output("modal-centered-1", "is_open"),
    [Input("open-centered-1", "n_clicks"), Input("close-centered-1", "n_clicks")],
    [State("modal-centered-1", "is_open")],
)
@app.callback(
    Output("modal-centered-2", "is_open"),
    [Input("open-centered-2", "n_clicks"), Input("close-centered-2", "n_clicks")],
    [State("modal-centered-2", "is_open")],
)
@app.callback(
    Output("modal-centered-3", "is_open"),
    [Input("open-centered-3", "n_clicks"), Input("close-centered-3", "n_clicks")],
    [State("modal-centered-3", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open