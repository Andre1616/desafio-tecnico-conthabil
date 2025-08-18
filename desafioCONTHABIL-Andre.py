from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import datetime, time, os, re, requests

url ="https://www.natal.rn.gov.br/dom"
navegador = Firefox()
navegador.get(url)

ddMes = navegador.find_element(By.NAME, "mes")
select = Select(ddMes)

hoje = datetime.datetime.now()
mesAnterior = hoje.month - 1 if hoje.month > 1 else 12
ano = hoje.year - 1 if mesAnterior == 12 else hoje.year

select.select_by_value(str(mesAnterior).zfill(2))
btnPesquisar = navegador.find_element(By.XPATH, '/html/body/div[3]/section[2]/div/div/div[1]/div[1]/form/button')

btnPesquisar.click()

time.sleep(1)

ddMostrarRegistros = navegador.find_element(By.XPATH, '/html/body/div[3]/section[2]/div/div/div[1]/div[2]/div/div/div[1]/div[1]/div/label/select')
select = Select(ddMostrarRegistros)
select.select_by_value("100")

nomeDiretorio = "DOMs " + str(mesAnterior) + "-" + str(ano)
os.makedirs(nomeDiretorio, exist_ok=True)

sanit = re.compile(r'[\\/:*?"<>|]')
vistos = set()
arquivosBaixados = []
CHUNK = 1024 * 64


while True:
    links = navegador.find_elements(By.XPATH,'//table[@id="example"]/tbody/tr/td/a')

    for link in links:
        urlArquivo = link.get_attribute("href")
        if not urlArquivo or urlArquivo in vistos:
            continue
        vistos.add(urlArquivo)
        nomeArquivo = sanit.sub("", link.text.strip())
        nomeArquivo = nomeArquivo.replace(" ", "_").replace("/", "-") + ".pdf"
        caminhoArquivo = os.path.join(nomeDiretorio,nomeArquivo)

        try:
            r = requests.get(urlArquivo,stream=True)
            with open(caminhoArquivo, "wb") as f:
                for chunk in r.iter_content(CHUNK):
                    f.write(chunk)
            print(f"Baixado com Sucesso: {nomeArquivo}")
            arquivosBaixados.append(caminhoArquivo)
        except Exception as e:
            print(f"Erro ao baixar {urlArquivo}: {e}")

    btnPaginador = navegador.find_elements(By.XPATH, '//ul[@class="pagination"]/li')
    paginaAtual = None

    for idx, li in enumerate(btnPaginador):
        if "active" in li.get_attribute("class"):
            paginaAtual = idx
            break

    if paginaAtual is None or paginaAtual + 1 >= len(btnPaginador):
        print("Todos os arquivos foram baixados com Sucesso.")
        break

    prox_li = btnPaginador[paginaAtual + 1]
    prox_li.find_element(By.TAG_NAME, "a").click()
    time.sleep(1)

urlUpload = "https://0x0.st"
HEADERS = {"User-Agent": "MeuScriptDOM/1.0"}

for caminhoArquivo in arquivosBaixados:
    try:
        with open(caminhoArquivo, "rb") as f:
            files = {"file": f}

            response = requests.post(urlUpload, files=files, headers=HEADERS)
            response.raise_for_status()

            urlPublica = response.text.strip()
            print(f"Arquivo {os.path.basename(caminhoArquivo)} enviado com sucesso! URL: {urlPublica}")

    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP no upload de {os.path.basename(caminhoArquivo)}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Erro de requisição no upload de {os.path.basename(caminhoArquivo)}: {e}")
