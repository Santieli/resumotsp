from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import pywhatkit as kt
# import pandas as pd
import requests

app = Flask(__name__)

@app.route('/')
def index():
    h = datetime.now()
    hora = h.strftime('%d'+'/'+'%m'+'/'+'%Y'+' - '+'%H'+':'+'%M'+' hs')
    return render_template('index.html', hora=hora)

@app.route('/send-message', methods=['POST'])
def send_message():
    
    h = datetime.now()
    hora = h.strftime('%d'+'/'+'%m'+'/'+'%Y'+' - '+'%H'+':'+'%M'+' hs')

    grafana = request.form['grafana']
    hw = request.form['hw']
    vandalismo = request.form['vandalismo']
    dl = request.form['dl']
    massivas = request.form['massivas']
    minimassivas = request.form['mini-massivas']
    oportunidade = request.form['oportunidade']

    dl_11 = request.form['dl_11']
    massiva_11 = request.form['massiva_11']
    minimassiva_11 = request.form['minimassiva_11']

    dl_12 = request.form['dl_12']
    massiva_12 = request.form['massiva_12']
    minimassiva_12 = request.form['minimassiva_12']

    dl_13 = request.form['dl_13']
    massiva_13 = request.form['massiva_13']
    minimassiva_13 = request.form['minimassiva_13']

    dl_14 = request.form['dl_14']
    massiva_14 = request.form['massiva_14']
    minimassiva_14 = request.form['minimassiva_14']

    dl_15 = request.form['dl_15']
    massiva_15 = request.form['massiva_15']
    minimassiva_15 = request.form['minimassiva_15']

    dl_16 = request.form['dl_16']
    massiva_16 = request.form['massiva_16']
    minimassiva_16 = request.form['minimassiva_16']

    dl_17 = request.form['dl_17']
    massiva_17 = request.form['massiva_17']
    minimassiva_17 = request.form['minimassiva_17']

    dl_18 = request.form['dl_18']
    massiva_18 = request.form['massiva_18']
    minimassiva_18 = request.form['minimassiva_18']

    dl_19 = request.form['dl_19']
    massiva_19 = request.form['massiva_19']
    minimassiva_19 = request.form['minimassiva_19']


    texto = f'''

*Resumo TSP* - Sites fora  {hora}
					
Afetação (Grafana): {grafana}					
					
*Regional TSP*					
					
*Falhas de HW:* {hw}				
*Vandalismo:* {vandalismo}				
					
*DL:* {dl}				
*Massivas:* {massivas}				
*Mini-Massivas:* {minimassivas}				
*Oportunidade sites:* {oportunidade}				
					
					
	*ANF 11*
    
        *DL(s):*				
            {dl_11}

        *Massivas:*
            {massiva_11}

        *Mini-Massivas:*
            {minimassiva_11}
					
	*ANF 12*

        *DL(s):*				
            {dl_12}

        *Massivas:*
            {massiva_12}

        *Mini-Massivas:*
            {minimassiva_12}	

	*ANF 13*

        *DL(s):*				
            {dl_13}

        *Massivas:*
            {massiva_13}

        *Mini-Massivas:*
            {minimassiva_13}

	*ANF 14*

        *DL(s):*				
            {dl_14}

        *Massivas:*
            {massiva_14}

        *Mini-Massivas:*
            {minimassiva_14}	

	*ANF 15*

        *DL(s):*				
            {dl_15}

        *Massivas:*
            {massiva_15}

        *Mini-Massivas:*
            {minimassiva_15}	

	*ANF 16*

        *DL(s):*				
            {dl_16}

        *Massivas:*
            {massiva_16}

        *Mini-Massivas:*
            {minimassiva_16}

	*ANF 17*

        *DL(s):*				
            {dl_17}

        *Massivas:*
            {massiva_17}

        *Mini-Massivas:*
            {minimassiva_17}

	*ANF 18*

        *DL(s):*				
            {dl_18}

        *Massivas:*
            {massiva_18}

        *Mini-Massivas:*
            {minimassiva_18}

	*ANF 19*

        *DL(s):*				
            {dl_19}

        *Massivas:*
            {massiva_19}

        *Mini-Massivas:*
            {minimassiva_19}


'''
    # df = pd.read_excel("Base_Whatssap.xlsx")

    linha = {'Data':hora, 
             'DL_11':dl_11,'Massiva_11': massiva_11,'Minimassiva_11': minimassiva_11,
             'DL_12':dl_12,'Massiva_12': massiva_12,'Minimassiva_12': minimassiva_12,
             'DL_13':dl_13,'Massiva_13': massiva_13,'Minimassiva_13': minimassiva_13,
             'DL_14':dl_14,'Massiva_14': massiva_14,'Minimassiva_14': minimassiva_14,
             'DL_15':dl_15,'Massiva_15': massiva_15,'Minimassiva_15': minimassiva_15,
             'DL_16':dl_16,'Massiva_16': massiva_16,'Minimassiva_16': minimassiva_16,
             'DL_17':dl_17,'Massiva_17': massiva_17,'Minimassiva_17': minimassiva_17,
             'DL_18':dl_18,'Massiva_18': massiva_18,'Minimassiva_18': minimassiva_18,
             'DL_19':dl_19,'Massiva_19': massiva_19,'Minimassiva_19': minimassiva_19,
             }
    
    # URL da API da SheetDB
    url = "https://sheetdb.io/api/v1/dgix0sg0ab77u"
     
    response = requests.post(url=url, json=linha)
    response.raise_for_status()


    # df = df.append(linha, ignore_index=True)

    # df.to_excel("Base_Whatssap.xlsx", index=False)
  
    kt.sendwhatmsg_instantly("+5511985236850", texto)

    return redirect('http://127.0.0.1:5000/')
    

if __name__ == "__main__":
    app.run(debug=True)