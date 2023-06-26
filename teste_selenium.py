from msedge.selenium_tools import Edge, EdgeOptions

# Configurar o caminho do driver do Microsoft Edge
driver_path = 'C:/Users/User/Downloads/edgedriver_win64/msedgedriver.exe'

# Configurar as opções do navegador
options = EdgeOptions()

# Inicializar o driver do Microsoft Edge
driver = Edge(executable_path=driver_path, options=options)

# Abre o navegador e acessa a página do aplicativo web
driver.get('http://localhost:5000')

# Localiza elementos na página pelo nome, classe, ID, etc., e interage com eles
username_input = driver.find_element_by_name('username')
username_input.send_keys('meu_usuario')

password_input = driver.find_element_by_name('password')
password_input.send_keys('minha_senha')

submit_button = driver.find_element_by_id('submit-btn')
submit_button.click()

# Verifica se a página após o login possui um elemento específico
welcome_message = driver.find_element_by_id('welcome-message')
assert welcome_message.text == 'Bem-vindo, meu_usuario!'

# Realiza outras interações no aplicativo, como clicar em links, preencher formulários, etc.

# Fecha o navegador
driver.quit()
