
print("What components do you have? Enter your components in the form: '2 pipe 1 gear 3 sheet'")

user_input = input()

l = user_input.split(' ')

quantity = []
component_name = []

# Insert even positions into quantity[]
for i in range(len(l))[0:len(l):2]:
    quantity.append(l[i])

# Insert odd positions into component_name[]
for i in range(len(l))[1:len(l):2]:
    component_name.append(l[i])

pairs = []

# Insert quantity[i] and component_name[i] into pairs[]
for i in range(len(quantity)):
    # concatenate quantity and component
    pair = quantity[i] + " " + component_name[i]
    pairs.append(pair)
    
inventory = pairs
print(inventory)

# Dictionary for components and their material values
components = {
    'cctv': {'scrap': 0, 'hqm': 2, 'metal': 0, 'cloth': 0, 'tech_trash': 2, 'rope': 0},
    'computer': {'scrap': 0, 'hqm': 1, 'metal': 50, 'cloth': 0, 'tech_trash': 3, 'rope': 0},
    'tech_trash': {'scrap': 20, 'hqm': 1, 'metal': 0, 'cloth': 0, 'tech_trash': 0, 'rope': 0},
    'tank': {'scrap': 1, 'hqm': 0, 'metal': 50, 'cloth': 0, 'tech_trash': 0, 'rope': 0},
    'blade': {'scrap': 2, 'hqm': 0, 'metal': 15, 'cloth': 0, 'tech_trash': 0, 'rope': 0},
    'roadsign': {'scrap': 5, 'hqm': 1, 'metal': 0, 'cloth': 0, 'tech_trash': 0, 'rope': 0},
    'pipe': {'scrap': 5, 'hqm': 1, 'metal': 0, 'cloth': 0, 'tech_trash': 0, 'rope': 0},
    'sheet': {'scrap': 8, 'hqm': 1, 'metal': 100, 'cloth': 0, 'tech_trash': 0, 'rope': 0},
    'spring': {'scrap': 12, 'hqm': 2, 'metal': 0, 'cloth': 0, 'tech_trash': 0, 'rope': 0},
    'gear': {'scrap': 10, 'hqm': 0, 'metal': 13, 'cloth': 0, 'tech_trash': 0, 'rope': 0},
    'sr_body': {'scrap': 15, 'hqm': 2, 'metal': 75, 'cloth': 0, 'tech_trash': 0, 'rope': 0},
    'smg_body': {'scrap': 15, 'hqm': 2, 'metal': 0, 'cloth': 0, 'tech_trash': 0, 'rope': 0},
    'rifle_body': {'scrap': 25, 'hqm': 2, 'metal': 0, 'cloth': 0, 'tech_trash': 0, 'rope': 0},
    'rope': {'scrap': 0, 'hqm': 0, 'metal': 0, 'cloth': 15, 'tech_trash': 0, 'rope': 0},
    'tarp': {'scrap': 0, 'hqm': 0, 'metal': 0, 'cloth': 50, 'tech_trash': 0, 'rope': 0},
    'sewing_kit': {'scrap': 0, 'hqm': 0, 'metal': 0, 'cloth': 10, 'tech_trash': 0, 'rope': 2},
    'tech_trash': {'scrap': 20, 'hqm': 1, 'metal': 0, 'cloth': 0, 'tech_trash': 0, 'rope': 0}
}

# Assign starting values for totals
# All int()
total_scrap = 0
total_hqm = 0
total_metal = 0
total_cloth = 0
total_tech_trash = 0
total_rope = 0

# 1. Find out how much each component is worth
# 2. Multiply the value * quantity in the same position
for c in range(len(component_name)):
    scrap = components[component_name[c]] ['scrap']
    hqm = components[component_name[c]] ['hqm']
    metal = components[component_name[c]] ['metal']
    cloth = components[component_name[c]] ['cloth']
    tech_trash = components[component_name[c]] ['tech_trash']
    rope = components[component_name[c]] ['rope']
    
    # Cast int(scrap) and int(quantity) so they can be multiplied
    total_scrap = total_scrap + (int(scrap) * int(quantity[c]))
    total_hqm = total_hqm + (int(hqm) * int(quantity[c]))
    total_metal = total_metal + (int(metal) * int(quantity[c]))
    total_cloth = total_cloth + (int(cloth) * int(quantity[c]))
    total_tech_trash = total_tech_trash + (int(tech_trash) * int(quantity[c]))
    total_rope = total_rope + (int(rope) * int(quantity[c]))

# Print total values at the end of the loop for grand totals
# Cast totals to str() so they can be printed
materials = str(total_scrap) + " scrap, " + str(total_hqm) + " hqm, " + str(total_metal) + " metal, " + str(total_cloth) + " cloth, " + str(total_tech_trash) + " tech trash, " + str(total_rope) + " rope"         
print(materials)


# Future ideas:
# 1. "I want x scrap and I have y components, what combination of components will yield x scrap?"
# 2. Recycle all remainders (ex. computers give tech_trash -> recycle remaining tech_trash,
#       sewing kits give rope -> recycle remaining rope) and add to the materials grand total
# 3. Connect program to database of component material values instead of a dictionary