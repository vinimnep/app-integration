import tkinter as tk
from tkinter import PhotoImage
import threading
import requests
from io import BytesIO
from datetime import datetime, time
import time

# Variáveis
url_deals = "https://crm.rdstation.com/api/v1/deals?token=****************************"
url_webhook = "https://webhook.zapcloud.com.br/webhook/**********************"
custom_field_id = "*********************"
execution_times = [time(9, 0), time(14, 0)]

def close_window():
    window.destroy()

def check_time():
    now = datetime.now().time()
    return now in execution_times

def your_utility_code():
    while True:
        if check_time():
            response_deals = requests.get(url_deals, headers={"accept": "application/json"})
            
            if response_deals.status_code == 200:
                data = response_deals.json()
    
                for deal in data["deals"]:
                    custom_fields = deal["custom_fields"]
                    
                    def find_custom_field(field_id):
                        for field in custom_fields:
                            if field["id"] == field_id and field["visible"]:
                                return True
                        return False
                    
                    if find_custom_field(custom_field_id):
                        name = deal["name"]
                        phone = deal["contacts"][0]["phones"][0]["phone"]
                        payload = {"leads": [{"name": name, "mobile_phone": phone}]}
                        
                        response_webhook = requests.post(url_webhook, json=payload)
                        
                        if response_webhook.status_code == 200:
                            result.set("Webhook enviado para: " + url_webhook)
                        else:
                            result.set("Erro ao enviar webhook: " + str(response_webhook.status_code))
        else:
            result.set("Aguardando horários de envio...")
            time.sleep(60)  # Espera 1 min pra checar denovo

# Cria a Janela
window = tk.Tk()
window.title("Custom Automation")
window.geometry("400x300")  

# Carrega a imagem
url = "https://spotmkt.com.br/wp-content/uploads/2023/05/Logo-SPOT-MKT-300x70.png"
response = requests.get(url)
image_bytes = BytesIO(response.content)
image = PhotoImage(data=image_bytes.getvalue())

# Cria o label para a imagem
image_label = tk.Label(window, image=image)
image_label.pack(pady=20)


result = tk.StringVar()
result_label = tk.Label(window, textvariable=result, font=("Helvetica", 10), wraplength=300)
result_label.pack(pady=20)

# Butão para fechar a janela
close_button = tk.Button(window, text="Close", command=close_window)
close_button.pack()


window.wm_attributes("-transparentcolor", "white")
window.overrideredirect(True) 

# Executa a requisição
thread_utility = threading.Thread(target=your_utility_code)
thread_utility.start()

window.mainloop()
