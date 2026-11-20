from pyscript import display, document

non_metals = {
    "Hydrogen": ("H", 1),
    "Helium": ("He", 2),
    "Lithium": ("Li", 3),
    "Beryllium": ("Be", 4),
    "Boron": ("B", 5),
    "Carbon": ("C", 6),
    "Nitrogen": ("N", 7),
    "Oxygen": ("O", ,)
    "Fluorine": ("F", 9),
    "Neon": ("Ne", 10)
}

def get_element_info(element):

document.getElementById('result').innerHTML = "result"
element1 =  document.getElementById('element-input').value.strip().title()


result = non_metals.get(
    element1,
    ("Element not found", "-", "-", "-")
)

document.getElementById('result').innerHTML = f"""
<b>Symbol:</b> {result[0]}<br>
<b>Element:</b> {result[1]}<br>
<b>Atomic Number:</b> {result[2]}<br>
<b>Atomic Mass:</b> {result[3]}
"""