"""
Aum Desai
Fall 2022
CS152B Final Project

This program calculates and makes the GUI for the user to make a molecules with the directed inputs. 
"""

import tkinter as tk
import simulation as sim



molecules = {

    "C0H2N0O1": "Water",
    "C0H2N0O2": "Hydrogen Peroxide",
    "C1H4N0O0": "Methane",
    "C0H3N1O0": "Ammonia",
    "C1H0N0O2": "Carbon Dioxide",
    "C2H6N0O1": "Ethanol",
    "C6H12N0O6": "Glucose",
    "C6H6N0O0": "Benzene",
}

def print_dic():

    '''
    Prints the dictionary as a hint
    '''

    output_label.config(text=molecules)


def execute(text):

    '''
    This function execute the molecule simulation chosen and created by the user. 
    '''
    molecule_index = {
        "Water": 1,
        "Hydrogen Peroxide": 2,
        "Methane": 3,
        "Ammonia": 4,
        "Carbon Dioxide": 5,
        "Ethanol": 6,
        "Glucose": 7,
        "Benzene": 8,
    }
    molecules = open("molecule.txt").read().splitlines()
    spheres = molecules[molecule_index[text]*3-2]
    lines = molecules[molecule_index[text]*3-1]
    sim.main(spheres,lines,text)
    


# Create the main window
root = tk.Tk()

# Set the title of the window
root.wm_title("Molecule Maker")

# Create the main frames
input_frame = tk.Frame(root)
output_frame = tk.Frame(root)


def create_molecule():

    '''
    Define the create_molecule function. Stores the user input in variables.
    Checks if any of the input fields are blank.
    '''

    carbon_count = carbon_field.get()
    hydrogen_count = hydrogen_field.get()
    nitrogen_count = nitrogen_field.get()
    oxygen_count = oxygen_field.get()
   


    if not carbon_count or not nitrogen_count or not oxygen_count or not hydrogen_count:
        # If any of the input fields are blank, update the output label with a message
        output_label.config(text="Please enter a value for each of the input fields")
        return

    # Use the input
  
    # Use the input variables to create the molecular formula
    molecular_formula = f"C{carbon_count}H{hydrogen_count}N{nitrogen_count}O{oxygen_count}"

    # Check if the molecular formula is in the molecules dictionary
    if molecular_formula in molecules:

        # Create the button with the corresponding molecule name
        molecule_button = tk.Button(output_frame, text=molecules[molecular_formula], command=execute(molecules[molecular_formula]))

        # Pack the button into the output frame
        molecule_button.pack()
    else:
        # Update the output label with a message
        output_label.config(text="Not within molecule database! Try Again :)")
        return
        

    true_molecular_formula = molecular_formula = molecular_formula.replace("C0", "").replace("H0", "").replace("N0", "").replace("O0", "").replace("C1","C").replace("H1","H").replace("N1","N").replace("O1","O")
    # Update the output label with the molecular formula
    output_label.config(text=true_molecular_formula)

# Create the input fields
carbon_label = tk.Label(input_frame, text="Number of carbon atoms:")
carbon_field = tk.Entry(input_frame)

hydrogen_label = tk.Label(input_frame, text="Number of hydrogen atoms:")
hydrogen_field = tk.Entry(input_frame)

nitrogen_label = tk.Label(input_frame, text="Number of nitrogen atoms:")
nitrogen_field = tk.Entry(input_frame)

oxygen_label = tk.Label(input_frame, text="Number of oxygen atoms:")
oxygen_field = tk.Entry(input_frame)


# Create the "Create" button
create_button = tk.Button(input_frame, text="Create", command=create_molecule)

hint_button = tk.Button(input_frame, text="Hints", command=print_dic)

hint_button.pack()

# Create the output label
output_label = tk.Label(output_frame)

# Pack the input fields, label, and button into the input frame
carbon_label.pack()
carbon_field.pack()
hydrogen_label.pack()
hydrogen_field.pack()
nitrogen_label.pack()
nitrogen_field.pack()
oxygen_label.pack()
oxygen_field.pack()

create_button.pack()

# Pack the output label into the output frame
output_label.pack()

# Pack the frames into the main window
input_frame.pack()
output_frame.pack()

# Run the main event loop
root.mainloop()