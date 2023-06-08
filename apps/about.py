from dash import html


layout = html.Div([

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Kelompok 7', style={"color": "#0084d6",
                                                'margin-left': '15px',
                                                'margin-top': '15px'}),
                    html.P('Web app ini adalah tugas besar mata kuliah perancangan aplikasi sains data yang dibuat oleh kelompok 7 yang terdiri dari Helmi Muzakki, Mugni Hidayah, dan Wildan Aufa Rafid. Webapp ini dibuat menggunakan dash python dan dash bootstrap. Menggunakan data booking hotel, web app ini menyediakan visualisasi pemesanan untuk hotel kota dan hotel resort, dan mencakup informasi yang lainnya.',
                            style={"color": "#ffffff",
                                    "font-size": "14px",
                                    'margin-left': '15px',
                                    'margin-right': '15px',
                                    'margin-top': '15px',
                                    'margin-bottom': '15px',
                                    'line-height': '1.2',
                                    'text-align': 'justify'
                                    }
                            ),
                    html.Div([
                        html.A(href='https://github.com/MugniHidayah', target='_blank',
                                children=[html.Img(src='/assets/github.png', height="30px",
                                                    style={"margin-top": '15px',
                                                            'margin-left': '15px',
                                                            'margin-bottom': '15px'})]),
                    ])
                ], className='first_text_column'),
                html.Div([
                    html.Img(src='/assets/programmer.gif', className='gif_image')
                ], className='gif_column')
            ], className='gif_row')
        ], className='about_bg eight columns')
    ], className='about_row row')

])
