```mermaid

graph TD

LONG_HANDED_INSERTER(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
IRON_CHEST002(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
IRON_CHEST002(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
INSERTER(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
AUTOMATION_SCIENCE_PACK(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
LAB(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
FAST_INSERTER(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
IRON_GEAR_WHEEL(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
TRANSPORT_BELT(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
IRON_PLATE(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
IRON_CHEST001(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
IRON_CHEST001(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
IRON_ORE(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
COPPER_PLATE(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
IRON_CHEST004(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
IRON_CHEST004(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
STONE_BRICK(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
ELECTRONIC_CIRCUIT(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
STEEL_FURNACE(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
IRON_CHEST005(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
IRON_CHEST005(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
STEEL_PLATE(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
COPPER_ORE(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
LOGISTIC_SCIENCE_PACK(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
IRON_CHEST003(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
IRON_CHEST003(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
STONE(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))
COPPER_CABLE(( <img src='https://wiki.factorio.com/images/thumb/Iron_chest.png/32px-Iron_chest.png' /> ))



INSERTER                                           --> FAST_INSERTER
INSERTER                                           --> LONG_HANDED_INSERTER
INSERTER                                           --> LOGISTIC_SCIENCE_PACK
IRON_ORE                                           --> IRON_PLATE
STONE_BRICK                                        --> STEEL_FURNACE
IRON_GEAR_WHEEL                                    --> IRON_CHEST001
IRON_CHEST001                                      --> TRANSPORT_BELT
IRON_CHEST001                                      --> INSERTER
IRON_CHEST001                                      --> LAB
IRON_GEAR_WHEEL                                    --> IRON_CHEST002
IRON_CHEST002                                      --> LONG_HANDED_INSERTER
IRON_CHEST002                                      --> AUTOMATION_SCIENCE_PACK
IRON_PLATE                                         --> IRON_CHEST003
IRON_CHEST003                                      --> TRANSPORT_BELT
IRON_CHEST003                                      --> STEEL_PLATE
IRON_CHEST003                                      --> FAST_INSERTER
IRON_PLATE                                         --> IRON_CHEST004
IRON_CHEST004                                      --> ELECTRONIC_CIRCUIT
IRON_CHEST004                                      --> INSERTER
IRON_CHEST004                                      --> LONG_HANDED_INSERTER
IRON_PLATE                                         --> IRON_CHEST005
IRON_CHEST005                                      --> IRON_GEAR_WHEEL
COPPER_ORE                                         --> COPPER_PLATE
COPPER_PLATE                                       --> AUTOMATION_SCIENCE_PACK
COPPER_PLATE                                       --> COPPER_CABLE
COPPER_CABLE                                       --> ELECTRONIC_CIRCUIT
ELECTRONIC_CIRCUIT                                 --> FAST_INSERTER
ELECTRONIC_CIRCUIT                                 --> INSERTER
ELECTRONIC_CIRCUIT                                 --> LAB
TRANSPORT_BELT                                     --> LAB
TRANSPORT_BELT                                     --> LOGISTIC_SCIENCE_PACK
STONE                                              --> STONE_BRICK
STEEL_PLATE                                        --> STEEL_FURNACE


```
