import os

# Installs everything we  need to install
# os.system('cmd /c "pip install pandas"')
# os.system('cmd /c "pip install plotly"')
# os.system('cmd /c "pip install numpy==1.19.3"')

# Changes path with real path

with open("Visualisation.bas") as f:
    newText=f.read().replace('adequatePath', os.path.dirname(os.path.abspath(__file__)))

with open("Visualisation.bas", "w") as f:
    f.write(newText)

# Opens Excel for excel setup

os.system('start excel '+ os.path.dirname(os.path.abspath(__file__)) + '/setup.xlsx')
