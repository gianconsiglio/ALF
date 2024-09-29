import PySimpleGUI as sg
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from random import choice
from selenium.webdriver.chrome.options import Options

button_open = 'iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAp0lEQVR4nO3VzQ2DMAyG4XcDBikjEBXKCkgdqiN0H2bpzxBGkXxAbUrrxLlUfJLFIciP7AgB5bkC8qWq5QQ8ayIBeABjLSQAdwWogQQF4qpYI/MPF7dVkzbrdUXDCyxe44TEBK5ItwG4IL0C8RlzTrxzKUG6T5ecimQCt8SK3JCDTnC09LIiDdBae3l+kbIjloj5ICOyI5aI+SAj8v/IXPj7XVfs9ZYF4DxkOdTsdJoAAAAASUVORK5CYII='
button_reboot = 'iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAACXBIWXMAAAsTAAALEwEAmpwYAAABZ0lEQVR4nM3Wu04cQRAF0LMsEAIZYEIyAoeWE0DYCBGBBXwAET9gIhv4AV7mN8hAgMiREx62CXllPEJECAmopUJarXnsLDMSVxqNutRdt6b79q3hHaAB/VjCPi5xhyscYBEDKNVLMIQ/+Isf+IRONKEjxin+LwiHK9Z2v5a8ESs4wmgNxZRi3hl+YQrbrxGsYwMtsqENO7jHdWz1k1gJgrLs+IibIElPz3NncFTHFzziO1bxG+eYVIWGOLwRBaI/lFQolkOOhWIvdF8ortBeNMktmnPOWcZ0ZeAyLCNPdIWUCz2Tz9itDCQ3/ZkzyRzmKwN94bZ5oYRD9FYHU7/4lhPJRBT9n0kO4vgN3vWIVpziixdufr0uLNZtRSd9cdIaNqOiLGgNgrVaiixHhzvBWA3JSxiPLVrKuguDYf+ph8+E7j+EM6R3Gs+GipJovmZJXl1lkvdCXKyLsKD0TuMUTzKt+28lNzwAdclE9SNXl/oAAAAASUVORK5CYII='
button_close = 'iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAi0lEQVR4nO3VMQ6AIAyF4f9ib9E7qVdWD6ExOhgTpLTg5FuY6BdCC/AnkAHoIgU49x91khEwA70TELBY9nshWQEvpFKgFJIXsEKKAjlItYAUpNrAvf9XYLrW6DwlMwLbtTZJ1/okzztQ8GXIAtSGcl2kKGRtU3mh0jlQKeQdNFmh6CTLAn3yM/7hLTtHBjH8yNmtagAAAABJRU5ErkJggg=='
button_back = 'iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAACXBIWXMAAAsTAAALEwEAmpwYAAAARklEQVR4nGNgGAWjYDACDwYGhlO0tuAbAwNDKq0scINakDVqwYAFEQg8Y2BgWMxAY0AXn4CA26hFgzbH063sGgWjgIEgAAAzSRQkbwf3gAAAAABJRU5ErkJggg=='
button_facial = 'iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAACXBIWXMAAAsTAAALEwEAmpwYAAABw0lEQVR4nN3VTYhOURgH8B/e0pCkGUU2opRY+yh2LETZzAJRikIm5aNeRlYaHwubiRILqWFYkpCdWSlJsbBW8jHEWqnR0UPXdY97Rjb863TP83++zrnnOc/hf8REZfTXdLOwCfvQje9m9Nbs+mtxGpPUsRCj+IT7uIAzOI/b+Ih7WF4Y7xdyPd7Fymdmdj8du/AG20qSbKnMl2Ecq5VhKV5jRSZeIx5id0U+imMtPjvCrwhpFy/RqXCP8QxTfuM3DW/jHFuxF5dj3okdPMVNnIpgOdzC1pIkx3ESG/EKD7AAs3EnuLSIEziEnViLqRiOQmnFQZyLYGsa9EuwJxZyETfwHNdwuuDsviGV5JVcCWYwA59xCfsVYBVeTDKJsH/U0C0asRIfcLiSNMnXa3ajwSf7hCMhr8sFTqU5EId2F2Mx70Y7Sav8UuG6IU+E/js3Fv7diPdTySdhMPrS3xqDLffqR++aU/J/0YcN/gBno+5LMBz2k8bcOMhFLXaL8T5204rtDdwBPEFPxqcn9AOF8bL34mo8TL01vi/4pC+Ol0vSicY4jpGonJGQh2rduihJ7o1PmB/NMN2B9J3XYNP6xv/b+ApBP3eJvbpSpgAAAABJRU5ErkJggg=='
button_sec = 'iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA4ElEQVR4nOVVyw3DIAx9rNCs02OmSLpHrkhNJRbixBadpjlRUdHKsswvH6lVn/QOYMcPOwYD/wZPyNeUuhToBmDJBICwptDEFuLMgs/LcJIMTAQZkXcmHYCH4PP50CZsExOZGF0UsZmDyJsRhpCvKftSvJzIGvjSpi50jq/orioRiaj88buKeJLBoSLuaBFDumqViGPUzDd1T6pF+sIdMD9zT85COSaBwU8BGCPV1nKZRHkuAO6Rw1GZjGtFWjJRMfjQUi7pqW+BzYkscdjsgS41tObC+PUNDHGuOx34i/AEfw2v8NdyYggAAAAASUVORK5CYII='
button_interfone = 'iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAACXBIWXMAAAsTAAALEwEAmpwYAAABdklEQVR4nMXVTUuWQRTG8Z9K1iKDlDCQNhYkYiGKSwV1mTuLMoKkDxCK9AGC2ihuRCXa6lasrS+tBAXd9LqsbQr5GWLgLIaH58FHnfKCezFnBv73nHOdM1yQ2jCN0X8FuI9fWMFvDJQGDOEQj2L9BN9wuRTgTvz5cEV8DW9LQV5hsUq8PeB9JSCTWK2x9wwHJSApXX/QXGXvVuwV0Q7Gq8TfYa4MgjF8RVMW6w7HtZaCJH3CVLZ+Gja+UhLSiSPczWKr8TWWBL3Ad7TEOplhAwsKawkfsvq0hI3flIRcwibeoyFiN7AfNyqWuqvYxWxFbCNqlMxwHfM4jpv2ngWUrPs5QA1ZjVbCdYfRRx0xGdIIel2jqU8E7UXq8h6aQE/F2ZtYxxf0nxaU0rSFj7hWx/mJGlO9LjMs4we66jif6vbSOfroKJ7oPH25HuPnecdRJ7Zj1j2seD1HwhD3FNKDmN7Jwik9qYlTLQZLAXLdxnPMxC3/v/4CSA1BuZ4kuwsAAAAASUVORK5CYII='
def Tela_Principal():
    sg.theme('Black')
    layout = [
        [sg.Push(), sg.Text('ALF 1.1.0'), sg.Push()],
        [sg.Push(), sg.Button('', key='ABRIR FACIAL', image_data=button_facial),
         sg.Button('', key='ABRIR INTERFONE', image_data=button_interfone),
         sg.Button('', key='ABRIR SEC', image_data=button_sec),
         sg.Button('', key='SAIR', image_data=button_close), sg.Push()]
    ]
    return sg.Window('', layout=layout, finalize=True, font='Verdana', text_justification='c', no_titlebar=True)

def Tela_Facial():
    sg.theme('Black')
    layout = [
        [sg.Push(), sg.Text('FACIAL'), sg.Push()],
        [sg.Push(), sg.Button('', key='ABRIR FACIAIS', image_data=button_open),
         sg.Button('', key='ABRIR FACIAIS E REINICIAR', image_data=button_reboot),
         sg.Button('', key='VOLTAR', image_data=button_back), sg.Push()]
    ]
    return sg.Window('', layout=layout, finalize=True, font='Verdana', text_justification='c', no_titlebar=True)

def Tela_Interfone():
    sg.theme('Black')
    layout = [
        [sg.Push(), sg.Text('INTERFONE'), sg.Push()],
        [sg.Push(), sg.Button('', key='ABRIR TELEFONES', image_data=button_open),
         sg.Button('', key='ABRIR TELEFONES E REINICIAR', image_data=button_reboot),
         sg.Button('', key='VOLTAR', image_data=button_back), sg.Push()]
    ]
    return sg.Window('', layout=layout, finalize=True, font='Verdana', text_justification='c', no_titlebar=True)

def Tela_Sec():
    sg.theme('Black')
    layout = [
        [sg.Push(), sg.Text('SEC'), sg.Push()],
        [sg.Push(), sg.Button('', key='ABRIR SEC', image_data=button_open),
         sg.Button('', key='ABRIR SEC E REINICIAR', image_data=button_reboot),
         sg.Button('', key='VOLTAR', image_data=button_back), sg.Push()]
    ]
    return sg.Window('', layout=layout, finalize=True, font='Verdana', text_justification='c', no_titlebar=True)

def informacoes():
    global pos, pos2, navegador, qtd, arq
    pos = 0
    pos2 = -1
    options = Options()
    options.add_experimental_option("detach", True)
    #servico = Service(ChromeDriverManager().install())
    #servico =  webdriver.Chrome()
    navegador = webdriver.Chrome(options=options)
    arq = open('ips faciais.txt')
    arq = arq.readlines()
    qtd = len(arq)


def get_facial():
    import pyodbc
    import time
    lista = []
    try:
        dados_conexao = (
            "Driver={SQL Server};"
            "Server=.\SQLEXPRESS;"
            f"Database=database;"
        )

        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()

    except Exception as erro:
        print(erro)
    try:
        cursor.execute('SELECT idtbldispositivo FROM TblDispositivo WHERE inttipo = 1 and intlixeira = 0')
        z = cursor.fetchall()

    except Exception as erro:
        print(erro)
        time.sleep(5)
    else:
        z = z[-1]
        z = str(z)
        z = z.replace(',', '').replace('(', '').replace(')', '')
        total_de_dispositivos = z
    som = 0
    while True:
        som += 1
        if som > int(total_de_dispositivos):
            break
        try:
            cursor.execute(
                f'SELECT strConfiguracao FROM TblDispositivo WHERE inttipo = 1 and intlixeira = 0 and idtbldispositivo = {som}')
            a = cursor.fetchall()
            b = list(a[0][0][98:112])
            b = str(b).replace("'", "").replace(",", "").replace("[", "").replace("]", "").replace(" ", "").replace('"',"")
        except Exception as erro:
            continue
        else:
            lista.append(b)
    arquivo = open('ips faciais.txt', 'w')
    for x in lista:
        arquivo.write(f'{x}\n')


janela = Tela_Principal()
while True:
    window, event, values = sg.read_all_windows()

    if event == 'ABRIR FACIAL':
        janela.close()
        janela = Tela_Facial()
        get_facial()

    elif event == 'ABRIR INTERFONE':
        janela.close()
        janela = Tela_Interfone()
        #get_interfone()

    elif event == 'ABRIR SEC':
        janela.close()
        janela = Tela_Sec()  
        #get_sec      

    elif event == 'VOLTAR':
        janela.close
        janela = Tela_Principal()    

    elif event == 'ABRIR FACIAIS E REINICIAR':
        if sg.PopupYesNo('ABRIR FACIAIS E REINICIAR TODOS?') == 'Yes':
            a = time.time()
            informacoes()
            while True:
                pos += 1
                pos2 += 1
                if pos > qtd:
                    sg.popup(f'Tempo de execução: {time.time() - a}')
                    break
                else:
                    try:
                        navegador.get(f'http://{arq[pos2]}')
                        navegador.find_element(By.XPATH, '//*[@id="username"]').send_keys("admin")
                        navegador.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")
                        navegador.find_element(By.XPATH, '//*[@id="login"]/table/tbody/tr/td[2]/div/div[5]/button').click()
                        time.sleep(2)
                        navegador.get(f'http://{arq[pos2]}/#/home/config/systemMaintain/maintainUpgrade')
                        time.sleep(2)
                        navegador.find_element(By.XPATH, '//*[@id="maintainUpgrade"]/div/div[2]/span[1]/button').click()
                        time.sleep(2)
                        navegador.find_element(By.XPATH, '//*[@id="layui-layer4"]/div[3]/a[1]').click()

                    except Exception as erro:
                        continue


    elif event == 'ABRIR FACIAIS':
        if sg.PopupYesNo('ABRIR TODOS OS FACIAIS?') == 'Yes':
            a = time.time()
            informacoes()
            while True:
                pos += 1
                pos2 += 1
                if pos > qtd:
                    sg.popup(f'Tempo de execução: {time.time() - a}')           
                    break
                else:
                    try:
                        navegador.get(f'http://{arq[pos2]}')
                        navegador.find_element(By.XPATH, '//*[@id="username"]').send_keys("admin")
                        navegador.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")
                        navegador.find_element(By.XPATH, '//*[@id="login"]/table/tbody/tr/td[2]/div/div[5]/button').click()

                    except Exception as erro:
                        continue

                    finally:
                        if qtd == pos:
                            pass
                        else:
                            navegador.execute_script("window.open('');")
                            navegador.switch_to.window(navegador.window_handles[pos])

    elif event == 'SAIR':
        break



