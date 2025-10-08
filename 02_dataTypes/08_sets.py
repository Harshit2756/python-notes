# normal set(mutable)
spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix id: {spice_mix}")
spice_mix.add("Ginger")
spice_mix.add("cardamom")
spice_mix.add("lemon")
print(f"Initial spice mix id: {spice_mix}")
print(f"After spice mix id: {id(spice_mix)}")

# frozenset example (immutable)
my_frozen = frozenset(spice_mix)
# my_frozen.add("lemon")

print("Frozen set:", my_frozen)

