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
        return f"IMC = {bmi}.", "Muito abaixo do peso.", "white", "red"
    elif (bmi < 18.5):
        return f"IMC = {bmi}.", "Abaixo do peso.", "white", "orange"
    elif (bmi < 25):
        return f"IMC = {bmi}.", "Peso é Normal.", "white", "green"
    elif (bmi < 30):
        return f"IMC = {bmi}.",  "Acima do peso.", "black", "yellow"
    elif (bmi < 35):
        return f"IMC = {bmi}.", "Obesidade I.", "white", "darkorange"
    elif (bmi < 40):
        return f"IMC = {bmi}.", "Obesidade II (Severa).", "white", "red"
    else:
        return f"IMC = {bmi}.", "Obesidade III (Mórbida).", "white", "darkred"


sg.theme('DarkBlue4')

layout = [
    [sg.Text('Insira a altura em metros (ex.: 1.65):'),
     sg.InputText(key='height')],
    [sg.Text('Insira o peso em quilogramas (ex.: 72):'),
     sg.InputText(key='weight')],
    [sg.Button('Calcular'), sg.Button('Cancelar')],
    [sg.Text('', size=(40, 1), key='output')],
    [sg.Text('Categoria', size=(40, 1), key='category', background_color='white')]
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
            index, category, text_color, bg_color = body_mass_index(
                round(imc, 2))
            window['output'].update(index)
            window['category'].update(
                category, text_color=text_color, background_color=bg_color)
        except ValueError:
            window['output'].update('Por favor, insira valores válidos.')
            window['category'].update('Categoria:', background_color='white')

window.close()
