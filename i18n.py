"""Gera en/index.html e es/index.html a partir do index.html em português.

Uso: python3 i18n.py
Edite sempre o index.html (PT) e rode este script para atualizar as traduções.
Se um texto em PT mudar, atualize também a linha correspondente em T abaixo.
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).parent

# (português, inglês, espanhol)
T = [
    # cabeçalho / meta
    ('<html lang="pt-BR">', '<html lang="en">', '<html lang="es">'),
    ('RL Infra | Projetos de infraestrutura viária no Rio de Janeiro',
     'RL Infra | Road infrastructure design in Rio de Janeiro, Brazil',
     'RL Infra | Proyectos de infraestructura vial en Río de Janeiro, Brasil'),
    ('content="Projetos de vias urbanas, rodovias, acessos viários e loteamentos em BIM: projeto geométrico, terraplenagem, drenagem pluvial, pavimentação e sinalização viária. Rio de Janeiro, atendimento em todo o Brasil."',
     'content="Design of urban roads, highways, road access and land subdivisions in BIM: geometric road design, earthworks, stormwater drainage, pavement and road signage. Based in Rio de Janeiro, Brazil."',
     'content="Proyectos de vías urbanas, carreteras, accesos viales y loteos en BIM: diseño geométrico, movimiento de tierras, drenaje pluvial, pavimentación y señalización vial. Río de Janeiro, Brasil."'),
    ('content="Projeto geométrico, terraplenagem, drenagem pluvial, pavimentação e sinalização viária em BIM."',
     'content="Geometric road design, earthworks, stormwater drainage, pavement and road signage in BIM."',
     'content="Diseño geométrico, movimiento de tierras, drenaje pluvial, pavimentación y señalización vial en BIM."'),
    ('<link rel="canonical" href="https://rlinfra.com.br/">', '<link rel="canonical" href="https://rlinfra.com.br/en/">', '<link rel="canonical" href="https://rlinfra.com.br/es/">'),
    ('<meta property="og:url" content="https://rlinfra.com.br/">', '<meta property="og:url" content="https://rlinfra.com.br/en/">', '<meta property="og:url" content="https://rlinfra.com.br/es/">'),
    ('<meta property="og:locale" content="pt_BR">', '<meta property="og:locale" content="en_US">', '<meta property="og:locale" content="es_ES">'),
    ('Rio de Janeiro, RJ · atendimento em todo o Brasil', 'Rio de Janeiro, Brazil · serving clients across Brazil', 'Río de Janeiro, Brasil · atendemos en todo Brasil'),
    ('aria-label="RL Infra, início"', 'aria-label="RL Infra, home"', 'aria-label="RL Infra, inicio"'),
    ('aria-label="Principal"', 'aria-label="Main"', 'aria-label="Principal"'),
    ('>Serviços</a>', '>Services</a>', '>Servicios</a>'),
    ('>Projetos</a>', '>Projects</a>', '>Proyectos</a>'),
    ('>A empresa</a>', '>About</a>', '>La empresa</a>'),
    ('>Contato<', '>Contact<', '>Contacto<'),
    ('aria-label="Idioma"', 'aria-label="Language"', 'aria-label="Idioma"'),
    ('Pedir orçamento', 'Request a quote', 'Solicitar presupuesto'),
    # hero
    ('Engenharia de infraestrutura · Rio de Janeiro', 'Infrastructure engineering · Rio de Janeiro', 'Ingeniería de infraestructura · Río de Janeiro'),
    ('<h1>Projetos de <em>vias urbanas, rodovias, acessos viários e loteamentos</em>.</h1>',
     '<h1>Design of <em>urban roads, highways, road access and land subdivisions</em>.</h1>',
     '<h1>Proyectos de <em>vías urbanas, carreteras, accesos viales y loteos</em>.</h1>'),
    ('Projeto geométrico, terraplenagem, drenagem pluvial, pavimentação e sinalização viária desenvolvidos de forma integrada em BIM, com documentação pronta para aprovação nos órgãos públicos.',
     'Geometric road design, earthworks, stormwater drainage, pavement and road signage, developed as one integrated BIM model, with documentation ready for approval by public authorities.',
     'Diseño geométrico, movimiento de tierras, drenaje pluvial, pavimentación y señalización vial desarrollados de forma integrada en BIM, con documentación lista para la aprobación de los organismos públicos.'),
    ('Ver projetos', 'See projects', 'Ver proyectos'),
    ('alt="Logo da RL Infra"', 'alt="RL Infra logo"', 'alt="Logotipo de RL Infra"'),
    ('Quem já confiou em nós', 'Clients who trusted us', 'Quienes ya confiaron en nosotros'),
    ('<span class="client">Governo do Estado do Rio de Janeiro</span>', '<span class="client">Government of the State of Rio de Janeiro</span>', '<span class="client">Gobierno del Estado de Río de Janeiro</span>'),
    # diferenciais
    ('Por que nos contratar', 'Why work with us', 'Por qué elegirnos'),
    ('Um projeto bem coordenado evita correções caras durante a obra.', 'A well-coordinated design avoids costly fixes during construction.', 'Un proyecto bien coordinado evita correcciones costosas durante la obra.'),
    ('<h3>Metodologia BIM</h3><p>Todas as disciplinas em um único modelo 3D. Cada alteração se reflete em todas as pranchas, sem retrabalho.</p>',
     '<h3>BIM methodology</h3><p>Every discipline in a single 3D model. Each change carries through to every drawing sheet, with no rework.</p>',
     '<h3>Metodología BIM</h3><p>Todas las disciplinas en un único modelo 3D. Cada cambio se refleja en todos los planos, sin retrabajo.</p>'),
    ('<h3>Pronto para aprovação</h3><p>Projetos elaborados conforme as exigências das prefeituras e dos órgãos rodoviários e de trânsito, o que agiliza a aprovação.</p>',
     '<h3>Ready for approval</h3><p>Designs prepared to the requirements of municipalities and highway and traffic authorities, which speeds up approval.</p>',
     '<h3>Listo para aprobación</h3><p>Proyectos elaborados según las exigencias de los municipios y de los organismos viales y de tránsito, lo que agiliza la aprobación.</p>'),
    ('<h3>Solução completa</h3><p>Do traçado geométrico à sinalização, com um único responsável técnico do estudo preliminar ao projeto executivo.</p>',
     '<h3>Complete solution</h3><p>From geometric alignment to signage, with one lead engineer from preliminary study to detailed design.</p>',
     '<h3>Solución completa</h3><p>Del trazado geométrico a la señalización, con un único responsable técnico desde el estudio preliminar hasta el proyecto ejecutivo.</p>'),
    ('<h3>Compatibilização</h3><p>Verificação de interferências entre greide, drenagem e pavimento antes que se tornem problemas na obra.</p>',
     '<h3>Clash detection</h3><p>Conflicts between vertical profile, drainage and pavement are checked before they become problems on site.</p>',
     '<h3>Compatibilización</h3><p>Verificación de interferencias entre rasante, drenaje y pavimento antes de que se conviertan en problemas en la obra.</p>'),
    ('<h3>Quantitativos precisos</h3><p>Volumes de corte e aterro e quantitativos de materiais extraídos diretamente do modelo, prontos para o orçamento.</p>',
     '<h3>Accurate quantities</h3><p>Cut and fill volumes and material quantities taken directly from the model, ready for cost estimating.</p>',
     '<h3>Cantidades precisas</h3><p>Volúmenes de corte y relleno y cantidades de materiales extraídos directamente del modelo, listos para el presupuesto.</p>'),
    ('<h3>Visualização 3D</h3><p>Imagens do empreendimento que facilitam a apresentação aos órgãos aprovadores, investidores e clientes.</p>',
     '<h3>3D visualization</h3><p>Images of the development that make it easier to present to approving authorities, investors and clients.</p>',
     '<h3>Visualización 3D</h3><p>Imágenes del emprendimiento que facilitan la presentación a organismos aprobadores, inversores y clientes.</p>'),
    # serviços
    ('Nossos serviços', 'Our services', 'Nuestros servicios'),
    ('Cinco disciplinas integradas em um só projeto.', 'Five disciplines integrated in one design.', 'Cinco disciplinas integradas en un solo proyecto.'),
    ('<h3>Projeto geométrico</h3><p>Traçado horizontal e vertical, greides, seções-tipo e interseções.</p>',
     '<h3>Geometric road design</h3><p>Horizontal and vertical alignment, profiles, typical cross-sections and intersections.</p>',
     '<h3>Diseño geométrico</h3><p>Trazado en planta y perfil, rasantes, secciones tipo e intersecciones.</p>'),
    ('<h3>Terraplenagem</h3><p>Platôs, taludes e otimização do equilíbrio entre corte e aterro.</p>',
     '<h3>Earthworks</h3><p>Building pads, slopes and an optimized cut and fill balance.</p>',
     '<h3>Movimiento de tierras</h3><p>Plataformas, taludes y optimización del equilibrio entre corte y relleno.</p>'),
    ('<h3>Drenagem pluvial</h3><p>Microdrenagem, galerias, bocas de lobo e dispositivos de dissipação.</p>',
     '<h3>Stormwater drainage</h3><p>Minor drainage, culverts, storm inlets and energy dissipators.</p>',
     '<h3>Drenaje pluvial</h3><p>Microdrenaje, alcantarillas, sumideros y disipadores de energía.</p>'),
    ('<h3>Pavimentação</h3><p>Dimensionamento de pavimentos, passeios e calçadas.</p>',
     '<h3>Pavement</h3><p>Pavement design for roads, walkways and sidewalks.</p>',
     '<h3>Pavimentación</h3><p>Diseño de pavimentos, aceras y veredas.</p>'),
    ('<h3>Sinalização viária</h3><p>Sinalização horizontal e vertical conforme os manuais do CONTRAN.</p>',
     '<h3>Road signage</h3><p>Road markings and vertical signs following Brazil\'s CONTRAN manuals.</p>',
     '<h3>Señalización vial</h3><p>Señalización horizontal y vertical según los manuales del CONTRAN de Brasil.</p>'),
    # sobre
    ('alt="Eng. Ronaldo Lima, responsável técnico da RL Infra"', 'alt="Eng. Ronaldo Lima, lead engineer at RL Infra"', 'alt="Ing. Ronaldo Lima, responsable técnico de RL Infra"'),
    ('<span>Responsável técnico · ', '<span>Lead engineer · ', '<span>Responsable técnico · '),
    ('Quem está à frente', 'Who leads the work', 'Quién está al frente'),
    ('Precisão técnica e foco em custo, do estudo ao projeto executivo.', 'Technical precision and cost focus, from study to detailed design.', 'Precisión técnica y enfoque en costos, del estudio al proyecto ejecutivo.'),
    ('<p>Engenheiro civil formado pela Universidade do Estado do Rio de Janeiro (UERJ), com experiência em projetos de infraestrutura urbana e rodoviária e especialização em projeto geométrico, terraplenagem e drenagem.</p>',
     '<p>Civil engineer graduated from the Rio de Janeiro State University (UERJ), experienced in urban and highway infrastructure design and specialized in geometric road design, earthworks and drainage.</p>',
     '<p>Ingeniero civil egresado de la Universidad del Estado de Río de Janeiro (UERJ), con experiencia en proyectos de infraestructura urbana y vial, y especialización en diseño geométrico, movimiento de tierras y drenaje.</p>'),
    ('<p>Atua em projetos de diferentes portes e níveis de complexidade, com o uso da metodologia BIM e de ferramentas avançadas de modelagem para entregar soluções eficientes, tecnicamente precisas e com custos otimizados.</p>',
     '<p>Works on projects of different sizes and levels of complexity, using BIM methodology and advanced modeling tools to deliver efficient, technically precise and cost-optimized solutions.</p>',
     '<p>Trabaja en proyectos de distintos tamaños y niveles de complejidad, con metodología BIM y herramientas avanzadas de modelado para entregar soluciones eficientes, técnicamente precisas y con costos optimizados.</p>'),
    ('<p>Tem trabalhos de pesquisa científica reconhecidos no Brasil e no exterior. À frente da RL Infra, seu compromisso é transformar desafios de engenharia em soluções inteligentes, com projetos de qualidade, inovadores e confiáveis.</p>',
     '<p>His scientific research has been recognized in Brazil and abroad. At the head of RL Infra, his commitment is to turn engineering challenges into smart solutions, with high-quality, innovative and reliable designs.</p>',
     '<p>Tiene trabajos de investigación científica reconocidos en Brasil y en el exterior. Al frente de RL Infra, su compromiso es transformar los desafíos de ingeniería en soluciones inteligentes, con proyectos de calidad, innovadores y confiables.</p>'),
    ('<span>Engenharia Civil</span>', '<span>Civil Engineering</span>', '<span>Ingeniería Civil</span>'),
    ('<span>modelagem integrada</span>', '<span>integrated modeling</span>', '<span>modelado integrado</span>'),
    ('<strong>Pesquisa</strong><span>reconhecida no Brasil e no exterior</span>', '<strong>Research</strong><span>recognized in Brazil and abroad</span>', '<strong>Investigación</strong><span>reconocida en Brasil y en el exterior</span>'),
    # projetos
    ('Projetos realizados', 'Completed projects', 'Proyectos realizados'),
    ('Trabalhos desenvolvidos.', 'Selected work.', 'Trabajos desarrollados.'),
    ('<h3>Via urbana com viaduto e interseções</h3><p class="meta">Projeto geométrico</p><p>Projeto geométrico de via urbana com transposição da linha férrea por viaduto, ramos de interseção, faixas e transições, integrado a muros de solo reforçado e barreiras de proteção.</p>',
     '<h3>Urban road with overpass and intersections</h3><p class="meta">Geometric road design</p><p>Geometric design of an urban road crossing the railway on an overpass, with intersection ramps, lanes and transitions, integrated with reinforced soil walls and safety barriers.</p>',
     '<h3>Vía urbana con viaducto e intersecciones</h3><p class="meta">Diseño geométrico</p><p>Diseño geométrico de vía urbana con cruce de la línea férrea por viaducto, ramales de intersección, carriles y transiciones, integrado a muros de suelo reforzado y barreras de protección.</p>'),
    ('<h3>Acesso viário em desnível com viaduto</h3><p class="meta">Terraplenagem</p><p>Terraplenagem dos ramos de acesso e da transposição da ferrovia por viaduto, com definição de cortes, aterros e taludes ao longo do traçado.</p>',
     '<h3>Grade-separated road access with overpass</h3><p class="meta">Earthworks</p><p>Earthworks for the access ramps and the railway crossing on an overpass, defining cuts, fills and slopes along the alignment.</p>',
     '<h3>Acceso vial a desnivel con viaducto</h3><p class="meta">Movimiento de tierras</p><p>Movimiento de tierras de los ramales de acceso y del cruce del ferrocarril por viaducto, con definición de cortes, rellenos y taludes a lo largo del trazado.</p>'),
    ('<h3>Rede de drenagem pluvial em modelo 3D</h3><p class="meta">Drenagem pluvial · BIM</p><p>Rede de drenagem pluvial modelada em 3D ao longo de via com retorno, com tubulações, poços de visita e caixas de captação compatibilizados com o greide e a superfície do terreno.</p>',
     '<h3>Stormwater drainage network in 3D</h3><p class="meta">Stormwater drainage · BIM</p><p>Stormwater drainage network modeled in 3D along a road with a turnaround, with pipes, manholes and inlets coordinated with the road profile and the ground surface.</p>',
     '<h3>Red de drenaje pluvial en modelo 3D</h3><p class="meta">Drenaje pluvial · BIM</p><p>Red de drenaje pluvial modelada en 3D a lo largo de una vía con retorno, con tuberías, pozos de inspección y sumideros compatibilizados con la rasante y la superficie del terreno.</p>'),
    ('<h3>Modelagem de interseção</h3><p class="meta">Modelagem BIM · visualização 3D</p><p>Modelagem 3D de interseção viária sobre a superfície do terreno, com taludes de corte e aterro.</p>',
     '<h3>Intersection modeling</h3><p class="meta">BIM modeling · 3D visualization</p><p>3D model of a road intersection on the ground surface, with cut and fill slopes.</p>',
     '<h3>Modelado de intersección</h3><p class="meta">Modelado BIM · visualización 3D</p><p>Modelado 3D de intersección vial sobre la superficie del terreno, con taludes de corte y relleno.</p>'),
    # contato
    ('Conte o que você precisa projetar.', 'Tell us what you need designed.', 'Cuéntenos qué necesita proyectar.'),
    ('Envie as informações do seu empreendimento e receba uma proposta personalizada.', 'Send us details about your development and receive a tailored proposal.', 'Envíe la información de su emprendimiento y reciba una propuesta personalizada.'),
    ('<li><small>Atendimento</small>Rio de Janeiro, RJ · em todo o Brasil</li>', '<li><small>Based in</small>Rio de Janeiro, Brazil</li>', '<li><small>Ubicación</small>Río de Janeiro, Brasil</li>'),
    ('<a href="https://wa.me/5521965968287">(21) 96596-8287</a>', '<a href="https://wa.me/5521965968287">+55 21 96596-8287</a>', '<a href="https://wa.me/5521965968287">+55 21 96596-8287</a>'),
    ('WhatsApp (21) 96596-8287', 'WhatsApp +55 21 96596-8287', 'WhatsApp +55 21 96596-8287'),
    ('<label for="f-nome">Nome<', '<label for="f-nome">Name<', '<label for="f-nome">Nombre<'),
    ('placeholder="Seu nome"', 'placeholder="Your name"', 'placeholder="Su nombre"'),
    ('<label for="f-empresa">Empresa<', '<label for="f-empresa">Company<', '<label for="f-empresa">Empresa<'),
    ('placeholder="Opcional"', 'placeholder="Optional"', 'placeholder="Opcional"'),
    ('placeholder="(21) 9 0000-0000"', 'placeholder="+55 21 9 0000-0000"', 'placeholder="+55 21 9 0000-0000"'),
    ('Tipo de projeto', 'Project type', 'Tipo de proyecto'),
    ('<option>Acesso</option>', '<option>Road access</option>', '<option>Acceso vial</option>'),
    ('<option>Via urbana</option>', '<option>Urban road</option>', '<option>Vía urbana</option>'),
    ('<option>Rodovia</option>', '<option>Highway</option>', '<option>Carretera</option>'),
    ('<option>Loteamento</option>', '<option>Land subdivision</option>', '<option>Loteo</option>'),
    ('<option>Outro</option>', '<option>Other</option>', '<option>Otro</option>'),
    ('Sobre o projeto<', 'About the project<', 'Sobre el proyecto<'),
    ('placeholder="Cidade, extensão ou área aproximada, prazo desejado..."', 'placeholder="City, approximate length or area, desired deadline..."', 'placeholder="Ciudad, longitud o área aproximada, plazo deseado..."'),
    ('Enviar pelo WhatsApp', 'Send via WhatsApp', 'Enviar por WhatsApp'),
    ('O WhatsApp abre com a sua mensagem pronta para enviar.', 'WhatsApp opens with your message ready to send.', 'WhatsApp se abre con su mensaje listo para enviar.'),
    ("'Preencha seu nome para montar a mensagem.'", "'Please enter your name to build the message.'", "'Ingrese su nombre para armar el mensaje.'"),
    ("'Olá! Sou '", "'Hello! I am '", "'¡Hola! Soy '"),
    ("'. Gostaria de um orçamento para: '", "'. I would like a quote for: '", "'. Me gustaría un presupuesto para: '"),
    ('<strong>Eng. Ronaldo Lima</strong>', '<strong>Eng. Ronaldo Lima</strong>', '<strong>Ing. Ronaldo Lima</strong>'),
    # rodapé
    ('Responsável técnico: Eng. Ronaldo Lima', 'Lead engineer: Eng. Ronaldo Lima', 'Responsable técnico: Ing. Ronaldo Lima'),
    # seletor de idioma
    ('<a href="/" hreflang="pt-BR" aria-current="true">PT</a>\n      <a href="/en/" hreflang="en">EN</a>\n      <a href="/es/" hreflang="es">ES</a>',
     '<a href="/" hreflang="pt-BR">PT</a>\n      <a href="/en/" hreflang="en" aria-current="true">EN</a>\n      <a href="/es/" hreflang="es">ES</a>',
     '<a href="/" hreflang="pt-BR">PT</a>\n      <a href="/en/" hreflang="en">EN</a>\n      <a href="/es/" hreflang="es" aria-current="true">ES</a>'),
    # caminhos relativos (a página traduzida fica uma pasta abaixo)
    ('src="img/', 'src="../img/', 'src="../img/'),
    ('href="img/', 'href="../img/', 'href="../img/'),
]


def build(col, folder):
    s = (ROOT / 'index.html').read_text(encoding='utf-8')
    missing = []
    for row in sorted(T, key=lambda r: -len(r[0])):
        if row[0] not in s:
            missing.append(row[0][:70])
        s = s.replace(row[0], row[col])
    out = ROOT / folder / 'index.html'
    out.parent.mkdir(exist_ok=True)
    out.write_text(s, encoding='utf-8')
    return missing


if __name__ == '__main__':
    problems = build(1, 'en') + build(2, 'es')
    if problems:
        print('Textos em PT não encontrados (atualize a tabela T):')
        for m in sorted(set(problems)):
            print('  -', m)
        sys.exit(1)
    print('en/index.html e es/index.html gerados.')
