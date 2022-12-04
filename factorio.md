```mermaid
graph TD

COPPER_ORE((                  <img src='https://wiki.factorio.com/images/thumb/Copper_ore.png/32px-Copper_ore.png                           ' /> ))
IRON_ORE((                    <img src='https://wiki.factorio.com/images/thumb/Iron_ore.png/32px-Iron_ore.png                               ' /> ))
STONE((                       <img src='https://wiki.factorio.com/images/thumb/Stone.png/32px-Stone.png                                     ' /> ))
URANIUM_ORE((                 <img src='https://wiki.factorio.com/images/thumb/Uranium_ore.png/32px-Uranium_ore.png                         ' /> ))
WOOD((                        <img src='https://wiki.factorio.com/images/thumb/Wood.png/32px-Wood.png                                       ' /> ))
ASSEMBLING_MACHINE_1((        <img src='https://wiki.factorio.com/images/thumb/Assembling_machine_1.png/32px-Assembling_machine_1.png       ' /> ))
ASSEMBLING_MACHINE_2((        <img src='https://wiki.factorio.com/images/thumb/Assembling_machine_2.png/32px-Assembling_machine_2.png       ' /> ))
AUTOMATION_SCIENCE_PACK((     <img src='https://wiki.factorio.com/images/thumb/Automation_science_pack.png/32px-Automation_science_pack.png ' /> ))
CHEMICAL_PLANT((              <img src='https://wiki.factorio.com/images/thumb/Chemical_plant.png/32px-Chemical_plant.png                   ' /> ))
COPPER_CABLE((                <img src='https://wiki.factorio.com/images/thumb/Copper_cable.png/32px-Copper_cable.png                       ' /> ))
COPPER_PLATE((                <img src='https://wiki.factorio.com/images/thumb/Copper_plate.png/32px-Copper_plate.png                       ' /> ))
ELECTRIC_MINING_DRILL((       <img src='https://wiki.factorio.com/images/thumb/Electric_mining_drill.png/32px-Electric_mining_drill.png     ' /> ))
ELECTRONIC_CIRCUIT((          <img src='https://wiki.factorio.com/images/thumb/Electronic_circuit.png/32px-Electronic_circuit.png           ' /> ))
FAST_INSERTER((               <img src='https://wiki.factorio.com/images/thumb/Fast_inserter.png/32px-Fast_inserter.png                     ' /> ))
INSERTER((                    <img src='https://wiki.factorio.com/images/thumb/Inserter.png/32px-Inserter.png                               ' /> ))
IRON_GEAR_WHEEL((             <img src='https://wiki.factorio.com/images/thumb/Iron_gear_wheel.png/32px-Iron_gear_wheel.png                 ' /> ))
IRON_PLATE((                  <img src='https://wiki.factorio.com/images/thumb/Iron_plate.png/32px-Iron_plate.png                           ' /> ))
LOGISTIC_SCIENCE_PACK((       <img src='https://wiki.factorio.com/images/thumb/Logistic_science_pack.png/32px-Logistic_science_pack.png     ' /> ))
LONG-HANDED_INSERTER((        <img src='https://wiki.factorio.com/images/thumb/Long-handed_inserter.png/32px-Long-handed_inserter.png       ' /> ))
OIL_REFINERY((                <img src='https://wiki.factorio.com/images/thumb/Oil_refinery.png/32px-Oil_refinery.png                       ' /> ))
PIPE((                        <img src='https://wiki.factorio.com/images/thumb/Pipe.png/32px-Pipe.png                                       ' /> ))
PUMPJACK((                    <img src='https://wiki.factorio.com/images/thumb/Pumpjack.png/32px-Pumpjack.png                               ' /> ))
STEEL_FURNACE((               <img src='https://wiki.factorio.com/images/thumb/Steel_furnace.png/32px-Steel_furnace.png                     ' /> ))
STEEL_PLATE((                 <img src='https://wiki.factorio.com/images/thumb/Steel_plate.png/32px-Steel_plate.png                         ' /> ))
STONE_BRICK((                 <img src='https://wiki.factorio.com/images/thumb/Stone_brick.png/32px-Stone_brick.png                         ' /> ))
SMALL_ELECTRIC_POLE((         <img src='https://wiki.factorio.com/images/thumb/Small_electric_pole.png/32px-Small_electric_pole.png         ' /> ))
TRANSPORT_BELT((              <img src='https://wiki.factorio.com/images/thumb/Transport_belt.png/32px-Transport_belt.png                   ' /> ))




ELECTRONIC_CIRCUIT             --> ASSEMBLING_MACHINE_1
IRON_GEAR_WHEEL                --> ASSEMBLING_MACHINE_1
IRON_PLATE                     --> ASSEMBLING_MACHINE_1
ELECTRONIC_CIRCUIT             --> ASSEMBLING_MACHINE_2
IRON_GEAR_WHEEL                --> ASSEMBLING_MACHINE_2
ASSEMBLING_MACHINE_1           --> ASSEMBLING_MACHINE_2
STEEL_PLATE                    --> ASSEMBLING_MACHINE_2
IRON_GEAR_WHEEL                --> AUTOMATION_SCIENCE_PACK
COPPER_PLATE                   --> AUTOMATION_SCIENCE_PACK
ELECTRONIC_CIRCUIT             --> CHEMICAL_PLANT
PIPE                           --> CHEMICAL_PLANT
STEEL_PLATE                    --> CHEMICAL_PLANT
IRON_GEAR_WHEEL                --> CHEMICAL_PLANT
COPPER_PLATE                   --> COPPER_CABLE
COPPER_ORE                     --> COPPER_PLATE
ELECTRONIC_CIRCUIT             --> ELECTRIC_MINING_DRILL
IRON_GEAR_WHEEL                --> ELECTRIC_MINING_DRILL
IRON_PLATE                     --> ELECTRIC_MINING_DRILL
COPPER_CABLE                   --> ELECTRONIC_CIRCUIT
IRON_PLATE                     --> ELECTRONIC_CIRCUIT
ELECTRONIC_CIRCUIT             --> FAST_INSERTER
INSERTER                       --> FAST_INSERTER
IRON_PLATE                     --> FAST_INSERTER
ELECTRONIC_CIRCUIT             --> INSERTER
IRON_GEAR_WHEEL                --> INSERTER
IRON_PLATE                     --> INSERTER
IRON_PLATE                     --> IRON_GEAR_WHEEL
IRON_ORE                       --> IRON_PLATE
INSERTER                       --> LOGISTIC_SCIENCE_PACK
TRANSPORT_BELT                 --> LOGISTIC_SCIENCE_PACK
INSERTER                       --> LONG-HANDED_INSERTER
IRON_GEAR_WHEEL                --> LONG-HANDED_INSERTER
IRON_PLATE                     --> LONG-HANDED_INSERTER
ELECTRONIC_CIRCUIT             --> OIL_REFINERY
PIPE                           --> OIL_REFINERY
STEEL_PLATE                    --> OIL_REFINERY
IRON_GEAR_WHEEL                --> OIL_REFINERY
STONE_BRICK                    --> OIL_REFINERY
IRON_PLATE                     --> PIPE
ELECTRONIC_CIRCUIT             --> PUMPJACK
IRON_GEAR_WHEEL                --> PUMPJACK
PIPE                           --> PUMPJACK
STONE_BRICK                    --> STEEL_FURNACE
STEEL_PLATE                    --> STEEL_FURNACE
IRON_PLATE                     --> STEEL_PLATE
STONE                          --> STONE_BRICK
WOOD                           --> SMALL_ELECTRIC_POLE
COPPER_CABLE                   --> SMALL_ELECTRIC_POLE
IRON_GEAR_WHEEL                --> TRANSPORT_BELT
IRON_PLATE                     --> TRANSPORT_BELT



```
