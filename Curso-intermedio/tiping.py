from typing import Dict, List, Tuple

positives: List[int] = [1, 2, 3, 4, 4]

users: Dict[str, int] = {
    'argentina': 1,
    'mexico': 34,
    'colombia': 45,    
}

coutries: List[Dict[str, str]] = [
    {
        'name': 'Argentina',
        'people': '450000',
    },
    {
        'name': 'México',
        'people': '900000',
    },
    {
        'name': 'Colombia',
        'people': '99999999',
    },
]

numbers: Tuple[int, float, int] = (1 , 0.5, 1)

CoordinaterType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinaterType = [
    {
        'coord1': (1 , 2),
        'coord2': (3 , 5)   
    },
    {
        'coord1': (0 , 1),
        'coord2': (2 , 5)
    },
]