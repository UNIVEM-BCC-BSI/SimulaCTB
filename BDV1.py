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
    ("O trânsito de qualquer natureza nas vias terrestres do território nacional, abertas à circulação, rege-se pelo:", "A) Código de Trânsito Brasileiro.", "B) Código Nacional de Trânsito.", "C) Código Brasileiro de Trânsito.", "D) Código de Trânsito.", "A"),
    ("Considera-se trânsito a utilização das vias por:", "A) Pessoas e animais, isolados ou em grupos.", "B) Pessoas, veículos e animais, isolados ou em grupos, conduzidos ou não.", "C) Veículos conduzidos por condutores habilitados.", "D) Pessoas e veículos, conduzidos ou não.", "B"),
    ("A utilização das vias por pessoas, veículos e animais é para fins de:", "A) Circulação, parada e estacionamento.", "B) Circulação e estacionamento.", "C) Circulação, parada e operação de carga ou descarga.", "D) Circulação, parada, estacionamento e operação de carga ou descarga.", "D"),
    ("São consideradas vias terrestres urbanas e rurais:", "A) Ruas, avenidas e vias internas pertencentes aos condomínios constituídos por unidades autônomas.", "B) Ruas, avenidas, logradouros, caminhos, passagens, estradas, rodovias, praias abertas à circulação pública e as vias internas pertencentes aos condomínios constituídos por unidades autônomas.", "C) Estradas e rodovias.", "D) Praias abertas à circulação pública.", "B"),
    ("As praias abertas à circulação pública e as vias internas pertencentes aos condomínios constituídos por unidades autônomas são, para efeito do Código de Trânsito Brasileiro, consideradas:", "A) Vias terrestres.", "B) Áreas autônomas.", "C) Vias privativas.", "D) Áreas restritas.", "A"),
    ("A Junta Administrativa de Recursos de Infrações é um órgão colegiado componente do:", "A) Conselho Estadual de Trânsito.", "B) Conselho Nacional de Trânsito.", "C) Sistema Nacional de Trânsito.", "D) Departamento Nacional de Trânsito.", "C"),
    ("Ao Departamento de Trânsito (DETRAN), cabe, entre outras, a atribuição de:", "A) Propor a alteração da sinalização.", "B) Organizar estatística de trânsito em todo o país.", "C) Vistoriar, registrar e emplacar veículos.", "D) Emitir carteira internacional.", "C"),
    ("O infrator que julgar improcedente a penalidade de multa que lhe foi aplicada poderá interpor recurso junto:", "A) CETRAN", "B) DENATRAN", "C) CONTRAN", "D) JARI", "D"),
    ("Organizar e manter o Registro Nacional de Carteiras de Habilitação – RENACH, compete ao:", "A) CONTRAN", "B) DENATRAN", "C) DETRAN", "D) CETRAN", "B"),
    ("Organizar e manter o Registro Nacional de Veículos Automotores – RENAVAM, compete ao:", "A) DETRAN", "B) CETRAN", "C) CONTRAN", "D) DENATRAN", "D"),
    ("Os Departamentos de Estradas e Rodagens são órgãos:", "A) Normativos do Sistema Nacional de Trânsito.", "B) Com jurisdição em todo território nacional.", "C) Executivos do Sistema Nacional de Trânsito.", "D) Normativos do Conselho Nacional de Trânsito.", "C"),
    ("Expedir a Permissão para Dirigir, a CNH, os Certificados de Registro e o de Licenciamento Anual, é competência do:", "A) DETRAN", "B) CETRAN", "C) CONTRANDIFE", "D) DENATRAN", "A"),
    ("Realizar, fiscalizar e controlar o processo de formação, aperfeiçoamento, reciclagem e suspensão de condutores, expedir e cassar Licença de Aprendizagem, Permissão para Dirigir e Carteira Nacional de Habilitação, mediante, delegação do órgão federal competente, é de responsabilidade do:", "A) DENATRAN.", "B) DETRAN.", "C) CETRAN.", "D) CONTRAN.", "B"),
    ("É competência da JARI:", "A) Cumprir e fazer cumprir a legislação de trânsito e a execução das normas e diretrizes estabelecidas pelo CONTRAN, no âmbito de suas atribuições.", "B) Administrar fundo de âmbito Nacional destinado à segurança e educação de trânsito.", "C) Julgar os recursos interpostos pelos infratores.", "D) Coletar dados, elaborar estudos sobre acidentes de trânsito e suas causas.", "C")
    ("Vistoriar, inspecionar quanto às condições de segurança veicular, registrar, emplacar, selar a placa, licenciar veículos, expedindo o Certificado de Registro e o Licenciamento Anual, mediante delegação do órgão federal competente, é de responsabilidade:", "A) Órgãos e entidades executivos de trânsito dos Estados e do Distrito Federal, no âmbito de sua circunscrição.", "B) Órgãos e entidades executivos rodoviários da União e dos Estados, no âmbito de sua circunscrição.", "C) Polícias Militares dos Estados e do Distrito Federal.", "D) Departamento Nacional de Infraestrutura de Trânsito.", "A"),
    ("A autorização para conduzir veículos de propulsão humana e de tração animal ficará a cargo do:", "A) Estado", "B) DETRAN", "C) Município", "D) DENATRAN", "C"),
    ("Obedece a legislação municipal do domicílio ou residência de seus proprietários, o registro e o licenciamento dos veículos de:", "A) Somente os ciclomotores e bicicletas.", "B) Propulsão humana e de tração animal.", "C) Reboque, semirreboque e bonde.", "D) Somente os de propulsão humana.", "B"),
    ("Compete aos órgãos e entidades executivos de trânsito dos Municípios, no âmbito de sua circunscrição:", "A) Estabelecer procedimentos sobre a aprendizagem e habilitação de condutores de veículos, a expedição de documentos de condutores, de registro e licenciamento de veículos.", "B) Proceder à supervisão, à coordenação, à correção do órgão delegado, ao controle e à fiscalização da Política Nacional de Trânsito e do Programa Nacional de Trânsito.", "C) Fiscalizar o nível de emissão de poluentes e ruído produzidos pelos veículos automotores ou pela sua carga.", "D) Conceder autorização para conduzir veículos de propulsão humana e de tração animal; registrar e licenciar na forma da legislação, veículos de propulsão humana e de tração animal.", "A"),
    ("A fiscalização da gestão de trânsito poderá ser realizada com a utilização de aparelhos que, quanto ao modo de operação, podem ser classificados em:", "A) Automático e não automático.", "B) Radar e medidor ótico.", "C) Fixo, estático, móvel e portátil.", "D) Eletrônico e audiovisual.", "C"),
    ("Somente poderá transitar pelas vias terrestres o veículo cujo peso e dimensões atenderem aos limites estabelecidos pelo:", "A) DENATRAN.", "B) CONTRAN.", "C) DETRAN.", "D) CONTRANDIFE.", "B"),
    ("Os órgãos técnicos e consultivos destinam-se a realizar estudos e oferecer sugestões sobre assuntos específicos. É chamado de:", "A) Jari", "B) DENATRAN", "C) CETRAN", "D) Câmaras Temáticas", "D"),
    ("A qual órgão abaixo compete criar Câmaras", "A) DENATRAN.", "B) CONTRAN.", "C) DETRAN.", "D) As JARIs.", "B"),
    ("São órgãos recursais", "A) CONTRAN", "B) PRF", "C) JARI’s", "D) CETRAN", "C"),
    ("A função exercida pela PRF com o objetivo de garantir obediência às normas de trânsito é:", "A) Fiscalização.", "B) Operação.", "C) Policiamento.", "D) Patrulhamento.", "C"),
    ("Encaminhar aos órgãos e entidades de trânsito informações sobre problemas apontados em recursos, compete:", "A) As JARIs.", "B) Ao CONTRAN.", "C) Ao DENATRAN.", "D) Ao CETRAN.", "D"),
    ("O Sistema Nacional de Trânsito é integrado por:", "A) Órgãos normativos e executivos;", "B) Órgãos de direção e executivos;", "C) Órgãos executivos;", "D) Órgãos colegiados e temáticos.", "A"),
    ("Realizar, fiscalizar e controlar o processo de habilitação, aperfeiçoamento, reciclagem e suspensão de condutores, é competência:", "A) Dos órgãos executivos de trânsito da União.", "B) Dos órgãos executivos dos Estados.", "C) Dos órgãos executivos rodoviários dos Estados.", "D) Dos órgãos normativos dos Estados.", "A"),
    ("A receita arrecadada com a cobrança das multas de trânsito será aplicada em:", "A) Sinalização.", "B) Engenharia de tráfego.", "C) Policiamento.", "D) Todas as afirmativas acima.", "D")
    ("Para que os veículos destinados à condução coletiva de escolares possam circular nas vias, exige-se:", "A) Cintos de segurança para o condutor e seu auxiliar.", "B) Registro de veículo especial.", "C) Lanternas de luz verde nas extremidades laterais direita e esquerda.", "D) Inspeção semestral para verificação dos equipamentos obrigatórios e de segurança.", "B"),
    ("O candidato para se habilitar para conduzir veículo automotor e elétrico deverá preencher os seguintes requisitos:", "A) Saber ler e escrever.", "B) Saber ler e escrever e possuir documento de identidade.", "C) Saber ler e escrever, ser penalmente imputável e possuir carteira de identidade ou equivalente.", "D) Ser penalmente imputável.", "C"),
    ("A cópia fotostática ou a fotocópia da Carteira Nacional de Habilitação:", "A) Não é válida para substituir documento original.", "B) É válida quando autenticada em cartório.", "C) É válida quando não plastificada.", "D) É válida quando apresentada junto com o documento de identidade do portador.", "D"),
    ("A Licença de Aprendizagem (LADV) suspensa poderá ser obtida novamente após decorridos:", "A) Seis meses.", "B) Três meses.", "C) Doze meses.", "D) Nove meses.", "A"),
    ("O candidato à obtenção da ACC ou da CNH deverá preencher os seguintes requisitos:", "A) Ser maior de 21 anos, possuir CPF, saber ler e escrever.", "B) Somente saber ler e escrever, e possuir documento de identidade.", "C) Ser penalmente imputável, saber ler e escrever, possuir documento de identidade e CPF.", "D) Ser maior de 18 anos, saber ler e escrever, possuir identidade e CPF.", "D"),
    ("A habilitação subordinada às condições estabelecidas em convenções e acordos internacionais e às normas do CONTRAN, é aquela obtida:", "A) No Brasil.", "B) No seu Estado.", "C) No seu Município.", "D) Em outro país.", "D"),
    ("As categorias existentes à habilitação são:", "A) A – B – C – D", "B) B – C – D – E", "C) B – C – D", "D) A – B – C – D – E", "D"),
    ("O condutor para conduzir veículo motorizado de duas ou três rodas, com ou sem carro lateral, deverá habilitar-se na categoria:", "A) A", "B) B", "C) C", "D) D", "A"),
    ("Assinale a alternativa que completa a questão: A categoria_______ habilita o condutor a dirigir veículo motorizado, não abrangido pela categoria A, cujo peso bruto total não exceda a 3.500 quilogramas e cuja lotação não exceda a 8 lugares, excluído o do motorista.", "A) C", "B) B", "C) E", "D) D", "A"),
    ("Assinale a alternativa que completa a questão: A categoria ______habilita o condutor a dirigir veículo motorizado utilizado em transporte de carga, cujo peso bruto total exceda a 3.500 quilogramas.", "A) D", "B) E", "C) C", "D) B", "A"),
    ("Assinale a alternativa que completa a questão: A categoria_______ habilita o condutor a dirigir veículo motorizado utilizado no transporte de passageiros, cuja lotação exceda a 8 lugares, excluído o do motorista:", "A) D", "B) C", "C) E", "D) B", "B"),
    ("A idade mínima para conduzir um veículo automotor com capacidade acima de 20 passageiros é:", "A) 20 anos.", "B) 21 anos.", "C) 18 anos.", "D) 19 anos.", "B"),
    ("No caso de reprovação no exame escrito de legislação de trânsito ou de direção veicular, o candidato poderá repetir o exame:", "A) No 15º dia da divulgação do resultado.", "B) No 16º dia da divulgação do resultado.", "C) No dia seguinte da divulgação do resultado.", "D) Não há período de interstício.", "C"),
    ("O candidato que pretende se habilitar para a categoria “D” deverá realizar o exame de direção veicular no veículo que tenha:", "A) No mínimo, 08 (oito) lugares, sem contar com o do condutor.", "B) No mínimo, 20 (vinte) lugares.", "C) Capacidade para transportar, no mínimo, 6000 (seis mil) quilogramas de carga.", "D) Duas rodas.", "A"),
    ("O trator de roda, o trator de esteira, o trator misto ou o equipamento automotor destinado à movimentação de cargas ou execução de trabalho agrícola, de terraplanagem, de construção ou de pavimentação só podem ser conduzidos na via pública por condutor habilitado na(s) categoria(s):", "A) A ou B", "B) AB", "C) C, D ou E", "D) Somente pela categoria B", "B")
    ("Para habilitar-se na categoria D, o condutor deverá possuir no mínimo:", "A) 1 ano na categoria B, ou 2 anos na categoria C.", "B) 2 anos na categoria B, ou 1 ano na categoria C.", "C) Somente 1 ano na categoria C.", "D) Somente 1 ano na categoria B.", "A"),
    ("Para habilitar-se na categoria E, o condutor deverá possuir no mínimo:", "A) 2 anos na categoria B.", "B) 1 ano na categoria B.", "C) 2 anos na categoria AB.", "D) 1 ano na categoria C.", "C"),
    ("A identificação do documento de habilitação e da autoridade expedidora são registrados no:", "A) RENAVAM", "B) RENACH", "C) RENACOM", "D) CETRAN", "B"),
    ("O condutor habilitado na categoria B que, posteriormente, habilitar-se na categoria A, receberá:", "A) Dois registros no RENACH.", "B) Um único registro no RENACOM.", "C) Um único registro no RENACH.", "D) Dois registros no RENACOM.", "C"),
    ("O candidato poderá requerer simultaneamente:", "A) A habilitação nas categorias A e C.", "B) Categorias A a ACC e habilitação na categoria D.", "C) Categorias A a ACC e habilitação na categoria B, bem como em AB.", "D) As categorias A e E.", "C"),
    ("Assinale a alternativa que completa a questão: O condutor de veículo destinado à condução de escolares deve ter idade superior a ____________ anos e ser habilitado na categoria ____________.", "A) 21, B", "B) 18, D", "C) 18, B", "D) 21, D", "D"),
    ("Do condutor de veículo destinado à condução de escolares, exige-se:", "A) Não ter cometido nenhuma infração de trânsito.", "B) Idade superior a 18 anos.", "C) Apresentação de certificado em curso especializado.", "D) Apresentação do Registro Nacional de Transportadores Urbanos.", "B"),
    ("Quando da renovação da CNH o condutor de veículo automotor deverá ser submetido ao exame de aptidão física e mental, nos seguintes períodos:", "A) De 05 (cinco) em 05 (cinco) anos até completar 60 (sessenta) anos de idade.", "B) De 05 (cinco) em 05 (cinco) anos a partir dos 60 (sessenta) anos de idade.", "C) De 03 (três) em 03 (três) anos a partir dos 40 (quarenta) anos de idade.", "D) De 05 (cinco) em 05 (cinco) anos até completar 65 (sessenta e cinco) anos de idade.", "A"),
    ("O condutor de veículo automotor, após 65 (sessenta e cinco) anos de idade, ao renovar sua CNH deverá ser submetido ao exame de aptidão física e mental, nos seguintes períodos:", "A) De 05 (cinco) em 05 (cinco) anos.", "B) De 02 (dois) em 02 (dois) anos.", "C) De 03 (três) em 03 (três) anos.", "D) De 10 (dez) em 10 (dez) anos.", "A"),
    ("O condutor que tiver a sua Permissão para Dirigir cassada, poderá reiniciar o processo de habilitação, que consiste em prestar exames de:", "A) Aptidão física e mental, avaliação psicológica e legislação de trânsito.", "B) Aptidão física e mental, avaliação psicológica, legislação de trânsito e prática de direção veicular.", "C) Prática de direção veicular.", "D) Legislação de trânsito e prática de direção veicular.", "B"),
    ("A Carteira Nacional de Habilitação não será conferida ao condutor portador da Permissão para Dirigir no término de um ano, se o mesmo cometer:", "A) Uma infração de natureza média.", "B) Uma infração de natureza grave.", "C) Ser reincidente na infração de natureza leve.", "D) Uma infração de natureza leve.", "B"),
    ("O processo do candidato à habilitação ficará ativado no Órgão ou Entidade Executivo de Trânsito pelo prazo de:", "A) 06 (seis) meses.", "B) 24 (vinte e quatro) meses.", "C) 12 (doze) meses.", "D) Durante a validade do exame de sanidade física e mental.", "C"),
    ("O candidato para se habilitar na categoria A, poderá realizar o exame de prática de direção veicular em veículo de 2 rodas com cilindrada:", "A) De 50 cm3.", "B) De 100 cm3.", "C) De 120 cm3.", "D) Acima de 120 cm3.", "D"),
    ("A não obtenção da Carteira Nacional de Habilitação pelo permissionário, implica em reiniciar todo o processo de habilitação, no prazo de:", "A) 30 dias.", "B) 15 dias.", "C) 360 dias.", "D) A qualquer tempo.", "C"),
    ("A Licença de Aprendizagem para prática de direção veicular em via pública, ou em locais autorizados para este fim, será expedida pelo DETRAN ao candidato que:", "A) Tenha completado 16 (dezesseis) anos de idade.", "B) Tenha completado 18 (dezoito) anos de idade.", "C) Tenha prestado o exame em veículo particular.", "D) Tenha sido aprovado nos exames de aptidão física e mental, avaliação psicológica e de legislação de trânsito.", "D")
    ("Automotor; elétrico, de propulsão humana, de tração animal, reboque ou semirreboque, é a classificação dos veículos quanto a:", "A) Espécie.", "B) Categoria.", "C) Carga.", "D) Tração.", "A"),
    ("É considerado veículo de passageiro:", "A) Carroça.", "B) Caminhão.", "C) Caminhonete.", "D) Bicicleta.", "C"),
    ("De acordo com a legislação de trânsito, os veículos quanto à espécie são:", "A) Oficial, particular, aluguel e de corrida.", "B) Particular, aluguel e escolar.", "C) Passageiros, carga, missão diplomática e aluguel.", "D) Passageiros, carga, misto, competição, tração, especial e coleção.", "D"),
    ("Assinale a alternativa correta. Não é considerado veículo de passageiros:", "A) Motoneta.", "B) Bicicleta.", "C) Carroça", "D) Triciclo.", "B"),
    ("Bonde, triciclo, bicicleta, reboque ou semirreboque são veículos, quanto à espécie, classificados como:", "A) Misto.", "B) Passageiros.", "C) Tração.", "D) Especial.", "A"),
    ("Camioneta e utilitário são veículos, quanto à espécie, classificados como:", "A) Tração.", "B) Passageiros.", "C) Misto.", "D) Carga.", "C"),
    ("Caminhonete e motocicleta são veículos, quanto à espécie, classificados como:", "A) Passageiros.", "B) Carga.", "C) Misto.", "D) Tração.", "A"),
    ("Segundo o Código de Trânsito Brasileiro a identificação externa de um veículo de duas rodas é feita por meio:", "A) Do registro de propriedade do veículo.", "B) Do número do motor.", "C) Das placas dianteira e traseira com caracteres iguais às do registro do veículo.", "D) Da placa traseira com caracteres iguais ao do registro do veículo.", "C"),
    ("Assinale a alternativa que responda a questão. O quadriciclo é um veículo classificado quanto à espécie em de _______ e de ________.", "A) Misto; competição.", "B) Passageiros; tração.", "C) Passageiros; carga.", "D) Espécie; coleção.", "B"),
    ("Veículos destinados à formação de condutores são classificados quanto à categoria, em:", "A) De aluguel.", "B) De aprendizagem.", "C) Particular.", "D) Oficial.", "B"),
    ("As características de um veículo podem ser modificadas quando:", "A) Sempre que for envolvido em acidente.", "B) Houver prévia autorização da autoridade de trânsito.", "C) O proprietário simplesmente quitar seus débitos com o órgão competente.", "D) O infrator não houver completado 20 pontos.", "B"),
    ("As bicicletas deverão ser dotadas dos seguintes equipamentos obrigatórios:", "A) Campainha, sinalização noturna dianteira, traseira, lateral e nos pedais e espelho retrovisor do lado esquerdo.", "B) Campainha e espelho retrovisor do lado esquerdo e do lado direito.", "C) Campainha e sinalização noturna.", "D) Cinto de segurança.", "C"),
    ("O transporte de passageiros em veículo de carga será permitido:", "A) Onde não houver linha regular de ônibus para transportar trabalhadores rurais.", "B) Onde não houver linha regular de ônibus e autorizado pela autoridade competente, obedecidas às condições de segurança.", "C) Desde que obedecidas as condições de segurança, para o transporte de desportistas.", "D) Para o transporte de estudantes nas zonas rurais.", "B"),
    ("Assinale a alternativa que completa a questão: O veículo será identificado internamente por caracteres gravados no _______ ou no ____________ e externamente por meio de ___________ dianteira e traseira.", "A) Radiador; cilindro; lanternas.", "B) Motor; cárter; rodas.", "C) Chassi; monobloco; placas.", "D) Carburador; chassi; placas.", "C"),
    ("O ciclomotor é veículo classificado quanto à espécie como:", "A) Misto.", "B) Tração.", "C) Especial.", "D) Passageiros.", "B"),
    ("São dispensados da placa dianteira, os veículos de:", "A) Quatro rodas.", "B) Mais de quatro rodas.", "C) Duas ou três rodas.", "D) Todos os veículos são obrigados a ter placa dianteira.", "C")
    ("As placas com as cores verde e amarela da Bandeira Nacional são usadas pelos veículos de representação pessoal do(s):", "A) Governadores.", "B) Presidente e Vice-Presidente da República.", "C) Prefeitos.", "D) Secretários municipais.", "B"),
    ("Ao registrar o veículo automotor, o órgão executivo de trânsito expedirá o documento:", "A) Certificado.", "B) Certificado de Segurança Veicular.", "C) Certificado de Registro de Veículo.", "D) Certificado de Registro e Licenciamento de Veículo.", "C"),
    ("Constitui documento de porte obrigatório:", "A) Certificado de Registro de Veículo.", "B) Autorização, Permissão para Dirigir ou Carteira Nacional de Habilitação.", "C) Comprovante do pagamento do Seguro Obrigatório.", "D) Comprovante do pagamento atualizado do IPVA.", "A"),
    ("A expedição de novo Certificado de Registro de Veículo, dar-se-á quando:", "A) Houver transferência de propriedade.", "B) Houver mudanças nos equipamentos obrigatórios.", "C) De doze em doze meses.", "D) Após o pagamento do I P V A.", "A"),
    ("No caso de transferência de propriedade, o prazo para o proprietário adotar as providências necessárias à efetivação da expedição de novo Certificado de Registro de Veículo é de:", "A) 15 dias.", "B) De imediato.", "C) 30 dias.", "D) A qualquer tempo.", "C"),
    ("A expedição de novo Certificado de Registro de Veículo é obrigatória quando:", "A) O proprietário mudar de endereço no mesmo Município.", "B) Houver mudança de categoria.", "C) O veículo circular acoplado a semirreboque.", "D) O veículo for importado por membro de missão diplomática.", "B"),
    ("O proprietário de veículo irrecuperável ou definitivamente desmontado deverá requerer a baixa do registro, sendo vedada à remontagem do veículo sobre o mesmo ______________, de forma a manter o registro anterior.", "A) Chassi.", "B) Agregados.", "C) Monobloco.", "D) Número de Registro.", "A"),
    ("O Licenciamento Anual do Veículo vincula-se ao:", "A) Pagamento de exames de avaliação psicológica e aptidão física.", "B) Pagamento do seguro total e DPVAT.", "C) Pagamento de IPVA, Seguro Obrigatório e inexistência de débitos de multas de trânsito.", "D) Pagamento de IPVA e Seguro Obrigatório.", "C")


]

for pergunta in perguntas:
    cursor.execute(
        'INSERT INTO Perguntas (pergunta, opcao_a, opcao_b, opcao_c, opcao_d, resposta_correta) VALUES (?, ?, ?, ?, ?, ?)',
        pergunta)
conn.commit()

print("Banco de dados criado e perguntas inseridas com sucesso!")

cursor.execute("SELECT * FROM Perguntas")
print(cursor.fetchall())

import sqlite3

conn = sqlite3.connect('questionario.db')
cursor = conn.cursor()

cursor.execute("SELECT opcao_a FROM Perguntas WHERE id = 8")

opcao_a = cursor.fetchone()[0]

print("Opção A da linha 8:", opcao_a)


id_pergunta = 8


cursor.execute("SELECT * FROM Perguntas WHERE id=?", (id_pergunta,))


pergunta = cursor.fetchone()


if pergunta:
    print("Pergunta encontrada:", pergunta)
else:
    print("Pergunta não encontrada.")


conn.close()
