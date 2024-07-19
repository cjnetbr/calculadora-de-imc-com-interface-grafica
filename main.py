import PySimpleGUI as sg

def bmi(height="height", weight="weight"):
  '''
  1st input: enter height in meters e.g: 1.65
  2nd input: enter weight in kilograms e.g: 72
  '''
  bmi = float(weight) / (float(height)**2)
  return bmi


def body_mass_index(bmi):
  '''
  Returns body mass index
  '''
  if (bmi < 17):
    return f"IMC = {bmi} Muito abaixo do peso."
  elif (bmi < 18.5):
    return f"IMC = {bmi} Abaixo do peso."
  elif (bmi < 25):
    return f"IMC = {bmi} Peso é Normal."
  elif (bmi < 30):
    return f"IMC = {bmi} Acima do peso."
  elif (bmi < 35):
    return "IMC = {bmi} Obesidade I."
  elif (bmi < 40):
    return f"IMC = {bmi} Obesidade II (Severa)."
  else:
    return f"IMC = {bmi} Obesidade III (Mórbida)."

#height = input("enter height in meters e.g: 1.65 ")
#weight = input("enter weight in kilograms e.g: 72 ")

#imc = bmi(height, weight)
#index = body_mass_index(round(imc, 2))
#print(index)

sg.theme('DarkAmber')
layout = [
    [sg.Text('Insira a altura em metros (ex.: 1.65):'), sg.InputText(key='height')],
    [sg.Text('Insira o peso em quilogramas (ex.: 72):'), sg.InputText(key='weight')],
    [sg.Button('Calcular'), sg.Button('Cancelar')],
    [sg.Text('', size=(40, 1), key='output')]
]
window = sg.Window('Calculadora de IMC', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        break

    if event == 'Calcular':
        try:
            height = float(values['height'])
            weight = float(values['weight'])
            imc = bmi(height, weight)
            index = body_mass_index(round(imc, 2))
            window['output'].update(index)
        except ValueError:
            window['output'].update('Por favor, insira valores válidos.')

window.close()