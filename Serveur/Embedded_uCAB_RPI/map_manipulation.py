#
# This file contins all methods for map manipulation
#
#@author : mingar
#

import json

class MapManager:
    
    def __init__(self):
        self.map = [{
            "areas": [
                {
                    "name": "Quartier Nord",
                    "map": {
                        "weight": {
                            "w": 1,
                            "h": 1
                        },
                        "vertices": [
                            {
                                "name": "a",
                                "x": 0.5,
                                "y": 0.5
                            },
                            {
                                "name": "b",
                                "x": 0.1,
                                "y": 0.2
                            },
                            {
                                "name": "c",
                                "x": 0.15,
                                "y": 0.6
                            },
                            {
                                "name": "d",
                                "x": 0.7,
                                "y": 0.5
                            },
                            {
                                "name": "e",
                                "x": 0.4,
                                "y": 0.75
                            },
                            {
                                "name": "f",
                                "x": 0.5,
                                "y": 1
                            },
                            {
                                "name": "g",
                                "x": 0.4,
                                "y": 0.2
                            }
                        ],
                        "streets": [
                            {
                                "name": "ba",
                                "path": [
                                    "b",
                                    "a"
                                ],
                                "oneway": False
                            },
                             {
                                "name": "ag",
                                "path": [
                                    "a",
                                    "g"
                                ],
                                "oneway": False
                            },
                            {
                                "name": "bc",
                                "path": [
                                    "b",
                                    "c"
                                ],
                                "oneway": False
                            },
                            {
                                "name": "da",
                                "path": [
                                    "d",
                                    "a"
                                ],
                                "oneway": False
                            },{
                                "name": "ae",
                                "path": [
                                    "a",
                                    "e"
                                ],
                                "oneway": False
                            },{
                                "name": "ce",
                                "path": [
                                    "c",
                                    "e"
                                ],
                                "oneway": False
                            },{
                                "name": "ef",
                                "path": [
                                    "e",
                                    "f"
                                ],
                                "oneway": False
                            }
                        ],
                        "bridges": [
                            {
                                "from": "f",
                                "to": {
                                    "area": "Quartier Sud",
                                    "vertex": "h"
                                },
                                "weight": 2
                            },{
                                "from": "d",
                                "to": {
                                    "area": "Quartier Est",
                                    "vertex": "i"
                                },
                                "weight": 2
                            }
                        ]
                    }
                }, 
                {
                    "name": "Quartier Sud",
                    "map": {
                        "weight": {
                            "w": 1,
                            "h": 1
                        },
                        "vertices": [
                            {
                                "name": "z",
                                "x": 1,
                                "y": 1
                            },
                            {
                                "name": "m",
                                "x": 0,
                                "y": 1
                            },
                            {
                                "name": "h",
                                "x": 0.5,
                                "y": 0
                            }
                        ],
                        "streets": [
                            {
                                "name": "zh",
                                "path": [
                                    "z",
                                    "h"
                                ],
                                "oneway": False
                            },
                            {
                                "name": "mh",
                                "path": [
                                    "m",
                                    "h"
                                ],
                                "oneway": False
                            }
                        ],
                        "bridges": [
                            {
                                "from": "h",
                                "to": {
                                    "area": "Quartier Nord",
                                    "vertex": "f"
                                },
                                "weight": 2
                            }
                        ]
                    }
                },
                {
                    "name": "Quartier Est",
                    "map": {
                        "weight": {
                            "w": 1,
                            "h": 1
                        },
                        "vertices": [
                            {
                                "name": "i",
                                "x": 0.1,
                                "y": 0.5
                            },
                            {
                                "name": "j",
                                "x": 0.55,
                                "y": 1
                            }
                        ],
                        "streets": [
                            {
                                "name": "ji",
                                "path": [
                                    "j",
                                    "i"
                                ],
                                "oneway": False
                            }
                        ],
                        "bridges": [
                            {
                                "from": "i",
                                "to": {
                                    "area": "Quartier Nord",
                                    "vertex": "d"
                                },
                                "weight": 2
                            }
                        ]
                    }
                }
            ]            
        }]
        
        self.cabs = [
                {
                    "available": True,
                    "accepted": True,
                    "position": "a",
                    "target": "a",
                    "travelled": 1
                }]
    
    
    #Convert all json to a string
    def json_to_str_map(self):
        return json.dumps(self.map[0], ensure_ascii=False)

    #Convert only a user json to a string    
    def json_to_str_map(self, id):
        if id > len(self.map[0]['areas']):
            id = len(self.map[0]['areas'])
        return json.dumps(self.map[0]['areas'][id], ensure_ascii=False)

    def set_cab_state(self, id, isAvailable, isMoving, addToQueue, vertice_to_go):
        #update the cab's state 
        self.map[0]['cabs'][id]['available'] = isAvailable
        self.map[0]['cabs'][id]['moving'] = isMoving
        self.map[0]['cabs'][id]['queue'] = self.map[0]['cabs'][id]['queue'] + addToQueue
        #update the traget    
        self.map[0]['cabs'][id]['target']['vertice'] = vertice_to_go

    def set_cab_position(self, id, vertice):
        self.map[0]['cabs'][id]['position']['vertice'] = vertice


    def set_cab_target(self, id, vertice):
        self.map[0]['cabs'][id]['target']['vertice'] = vertice


    def set_cab_travelled(self, id, vertice):
        #set the distance since the last course to 0
        self.map[0]['cabs'][id]['travelled']['vertice'] = vertice


    def print_all_cab(self):
        print '---'
        print self.map[0]['cabs']
        print '---'


    def get_map(self, id):
        newMap = self.map[0]['areas'][id]
        newMap['map']['cabs'] = self.cabs
        return newMap
    
    
    def remove_cab(self, cabId):
        if self.cabs[cabId] in self.cabs: self.cabs.remove(self.cabs[cabId])

        
    def move_cab(self, cabId, newVertex):
        if self.cabs[cabId] in self.cabs:
            self.cabs[cabId]['position'] = newVertex
            