from django.shortcuts import render
import folium

# Create your views here.

init_coordinate = [34.809758971192736, 135.56069280006483]

shrine_coord = [[35.0395  , 135.7285  ], 
                [34.995   , 135.785   ],
                [35.034444, 135.718333],
                [34.980556, 135.747778],
                [35.015963, 135.673772],
                [35.011983, 135.794389],
                [35.026667, 135.798333],
                [35.043889, 135.746111],
                [34.889444, 135.807778],
                [35.031   , 135.7138  ],
                [34.967222, 135.772778],
                [35.038889, 135.7725  ],
                [35.003611, 135.778611],
                [35.045625, 135.741458],
                [35.016667, 135.782222],
                [34.991389, 135.7725  ],
                [35.015833, 135.689167],
                [35.121722, 135.762833],
                [35.059886, 135.634467],
                [34.879667, 135.700056]]
kyoto_peri = [[35.106, 135.63], [35.106, 135.851], [34.871, 135.851], [34.871, 135.63], [35.106, 135.63]]
[35.106, 34.871, 135.63, 135.851]


# def index(request):
    
#     m = folium.Map(location=init_coordinate, zoom_start=15)
#     folium.Marker(get_by_address(), zoom_srat=12).add_to(m)
#     m.location = [get_by_address()]
#     context = {'m' : m._repr_html_()}
#     return render(request, 'index.html', context)

def user(request):
    context = {}
    return render(request, 'user.html', context)

def map(request):
    
    m = folium.Map(width=1200,height=650, location=init_coordinate, zoom_start=12)
    folium.Marker(init_coordinate).add_to(m)
    # for i in range(len(shrine_coord)):
    #     folium.Marker([shrine_coord[i][0], shrine_coord[i][1]], zoom_start=12).add_to(m)
    folium.Marker(get_by_address(), zoom_start=12).add_to(m)
    folium.PolyLine(locations=kyoto_peri, color="#eb3437", weight=3,tooltip="Kyoto Perimeter",).add_to(m)
    
        
    #folium.PolyLine(locations=shrine_coord, color="#2896fc", weight=3,tooltip="From Boston to San Francisco",).add_to(m)
    context = {'m' : m._repr_html_()}
    return render(request, 'map.html', context)

def get_by_address():
    import googlemaps
    GOOGLE_MAPS_API_KEY= "AIzaSyCNqwB4cJfufJ_0Kya6i8I4tqKXTUh6crU"
    import json
    gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
    address = '1 Kinkakujicho, Kita Ward, Kyoto, 603-8361'
    geocode_result = gmaps.geocode(address)
    print(json.dumps(geocode_result,indent=2))
    print(geocode_result[0]['geometry']['location'])
    loc = geocode_result[0]['geometry']['location']
    return [loc['lat'],loc['lng']]

def get_route():
    import googlemaps
    GOOGLE_MAPS_API_KEY= "AIzaSyCNqwB4cJfufJ_0Kya6i8I4tqKXTUh6crU"
    import json
    gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
    address = '1 Kinkakujicho, Kita Ward, Kyoto, 603-8361'
    geocode_result = gmaps.geocode(address)
    print(json.dumps(geocode_result,indent=2))
    print(geocode_result[0]['geometry']['location'])
    loc = geocode_result[0]['geometry']['location']
    return [loc['lat'],loc['lng']]