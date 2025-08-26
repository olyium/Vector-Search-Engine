import math

VECTORS = {'dog': [1, 2], 'cat': [1, 2.2], 'mouse': [1, 2.4], 'alien': [2, 2], 'human': [3, 2], 'truck': [4, 2], 'car': [4, 2.2], 'plane': [4.5, 2], 'jet': [4.5, 2.1], 'boat': [4.7, 2], 'house': [5, 2],
         'home': [5, 2], 'apartment': [5, 2.2], 'motel': [5.2, 2], 'hotel': [5.2, 2.4], 'roblox': [6, 2.2], 'fortnite': [6, 2.2], 'gta5': [6.2, 2.4], 'gta6': [6.2, 2.5], 'gta': [6.2, 2], 'game': [6, 2],
         'sword': [7, 2], 'knife': [7, 2.2], 'gun': [7.2, 2], 'ak47': [7.2, 2.2], 'ar15': [7.2, 2.3], 'ar12': [7.2, 2.4], 'm4a1': [7.2, 2.5], 'usa': [6, 2.2], 'france': [6, 2.3], 'country': [6, 2], 'world': [6.2, 2],
         'space': [6.7, 2], 'universe': [6.7, 2.5], 'galaxy': [6.7, 2.7], 'moon': [6.4, 2.6], 'earth': [6.4, 2.1], 'exoplanet': [6.4, 2.2], 'venus': [6.4,2.1], 'mars': [6.4,2.1], 'saturn': [6.4,2.1], 'netune': [6.4,2.1], 'planet': [6.4, 2]}

def GetResults(VECTOR: list, MAX_RESULTS=5):

    RANKINGS = {}
    REVERSE_RANKINGS = {}
    FINALIZED = []

    for VECTOR_ in list(sorted(VECTORS)):
        DISTANCE = math.sqrt((VECTORS[VECTOR_][0]-VECTOR[0])**2 + (VECTORS[VECTOR_][1]-VECTOR[1])**2)
        RANKINGS[VECTOR_] = DISTANCE

    for NAME, VECTOR__ in RANKINGS.items():
        REVERSE_RANKINGS[VECTOR__] = NAME

    if len(REVERSE_RANKINGS) < MAX_RESULTS or MAX_RESULTS < 0:
        MAX_RESULTS = len(REVERSE_RANKINGS)

    for DISTANCE in sorted(REVERSE_RANKINGS)[:MAX_RESULTS]:
        FINALIZED.append(REVERSE_RANKINGS[DISTANCE])

    return FINALIZED

def Vectorize(INPUT: str):

    return VECTORS[INPUT]

print(GetResults([6.7, 2.8]))
