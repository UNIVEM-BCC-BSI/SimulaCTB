import sqlite3

conn = sqlite3.connect('questionario.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Perguntas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pergunta TEXT,
    opcao_a TEXT,
    opcao_b TEXT,
    opcao_c TEXT,
    opcao_d TEXT,
    resposta_correta TEXT
)
''')

perguntas = [
    ("A atual legislação de trânsito intitula-se:", "A) Código Nacional de Trânsito.", "B) Código de Trânsito.", "C) Código de Trânsito Brasileiro.", "D) Código Brasileiro de Trânsito.", "C"),
    ("O Licenciamento Anual do Veículo vincula-se ao:", "A) Pagamento de exames de avaliação psicológica e aptidão física.", "B) Pagamento do seguro total e DPVAT.", "C) Pagamento de IPVA, Seguro Obrigatório e inexistência de débitos de multas de trânsito.", "D) Pagamento de IPVA e Seguro Obrigatório.", "C"),
    ("O ciclomotor é veículo classificado quanto à espécie como:", "A) Misto.", "B) Tração.", "C) Especial.", "D) Passageiros.", "B"),
    ("São dispensados da placa dianteira, os veículos de:", "A) Quatro rodas.", "B) Mais de quatro rodas.", "C) Duas ou três rodas.", "D) Todos os veículos são obrigados a ter placa dianteira.", "C"),
    ("As placas com as cores verde e amarela da Bandeira Nacional são usadas pelos veículos de representação pessoal do(s):", "A) Governadores.", "B) Presidente e Vice-Presidente da República.", "C) Prefeitos.", "D) Secretários municipais.", "B"),
    ("Ao registrar o veículo automotor, o órgão executivo de trânsito expedirá o documento:", "A) Certificado.", "B) Certificado de Segurança Veicular.", "C) Certificado de Registro de Veículo.", "D) Certificado de Registro e Licenciamento de Veículo.", "C"),
    ("Constitui documento de porte obrigatório:", "A) Certificado de Registro de Veículo.", "B) Autorização, Permissão para Dirigir ou Carteira Nacional de Habilitação.", "C) Comprovante do pagamento do Seguro Obrigatório.", "D) Comprovante do pagamento atualizado do IPVA.", "A"),
    ("A expedição de novo Certificado de Registro de Veículo, dar-se-á quando:", "A) Houver transferência de propriedade.", "B) Houver mudanças nos equipamentos obrigatórios.", "C) De doze em doze meses.", "D) Após o pagamento do I P V A.", "A"),
    ("No caso de transferência de propriedade, o prazo para o proprietário adotar as providências necessárias à efetivação da expedição de novo Certificado de Registro de Veículo é de:", "A) 15 dias.", "B) De imediato.", "C) 30 dias.", "D) A qualquer tempo.", "C"),
    ("A expedição de novo Certificado de Registro de Veículo é obrigatória quando:", "A) O proprietário mudar de endereço no mesmo Município.", "B) Houver mudança de categoria.", "C) O veículo circular acoplado a semirreboque.", "D) O veículo for importado por membro de missão diplomática.", "B"),
    ("O proprietário de veículo irrecuperável ou definitivamente desmontado deverá requerer a baixa do registro, sendo vedada à remontagem do veículo sobre o mesmo ______________, de forma a manter o registro anterior.", "A) Chassi.", "B) Agregados.", "C) Monobloco.", "D) Número de Registro.", "A"),
    
]

for pergunta in perguntas:
    cursor.execute("INSERT INTO Perguntas (pergunta, opcao_a, opcao_b, opcao_c, opcao_d, resposta_correta) VALUES (?, ?, ?, ?, ?, ?)", pergunta)

conn.commit()

cursor.execute("SELECT * FROM Perguntas")
todas_perguntas = cursor.fetchall()
print("Todas as perguntas no banco de dados:", todas_perguntas)

conn.close()
