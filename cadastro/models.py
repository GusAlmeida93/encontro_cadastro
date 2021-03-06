from django.db import models
from datetime import datetime, time, date

# Create your models here.


class Cadastro(models.Model):
    acfarma = "Acfarma"
    agafarma = "Agafarma"
    asfar_desconto_facil = "Asfar Desconto Facil"
    augefarma = "Augefarma"
    bigfort = "Bigfort"
    biodrogas = "Biodrogas"
    boa_farma = "Boa Farma"
    cityfarma = "Cityfarma"
    compre_certo = "Compre Certo"
    coperfarma = "Coperfarma"
    droga_rede = "Droga Rede"
    drogamais = "Drogamais"
    drogaria_atual = "Drogaria Atual"
    drogaria_total = "Drogaria Total"
    drogarias_conceito = "Drogarias Conceito"
    drogarias_maestra = "Drogarias Maestra"
    dsg_farma = "Dsg Farma"
    entrefarma = "Entrefarma"
    farma_100 = "Farma 100"
    farma_e_cia = "Farma E Cia"
    farma_e_farma = "Farma E Farma"
    farmacia_dias = "Rede Carioca"
    farmacias_associadas = "Farmacias Associadas"
    farmacias_conviva = "Farmacias Conviva"
    farmagnus = "Farmagnus"
    farmavale_e_cia = "Farmavale E Cia"
    farmavip = "Farmavip"
    farmelhor = "Farmelhor"
    farmes = "Farmes"
    fazfarma = "Fazfarma"
    grupofarma = "Grupofarma"
    hiperfarma = "Hiperfarma"
    inova_drogarias = "Inova Drogarias"
    legitima = "Legitima"
    lider_saude = "Lider Saude"
    maxifarma = "Maxifarma"
    mg_farma = "Mg Farma"
    multmais = "Multmais"
    nossa_rede = "Nossa Rede"
    nova_rede_drogarias = "Nova Rede Drogarias"
    pix_farma = "Pix Farma"
    rede_farmagente = "Rede Farmagente"
    rede_liga_farma = "Rede Liga Farma"
    rede_minas_farma = "Rede Minas Farma"
    redefarma = "Redefarma"
    redemais_farma = "Redemais Farma"
    sanar = "Sanar"
    sisfarma = "Sisfarma"
    stylofarma = "Stylofarma"
    super_popular = "Super Popular"
    tche_farmacias = "Tche Farmacias"
    uai_farma = "Uai Farma"
    ultra_popular = "Ultra Popular"
    uniao_farma = "Uniao Farma"
    unifarma = "Unifarma"
    vida_farmacias = "Vida Farmacias"
    viva_mais = "Viva Mais"
    abbott_epd = "Abbott Epd"
    abbott_nutricao = "Abbott Nutrição"
    ache = "Ache"
    ache_biosintetica = "Ache Biosintetica"
    althaiaequaliv = "Althaiaequaliv"
    apsen = "Apsen"
    baldacci = "Baldacci"
    bayer_otc = "Bayer Otc"
    biolab_genericos = "Biolab Genericos"
    biolabsanus_farma = "Biolabsanus Farma"
    blau_farmaceutica = "Blau Farmaceutica"
    canonne = "Canonne"
    catarinense = "Catarinense"
    cellera_delta = "Cellera Delta"
    cimed = "Cimed"
    cimed_onefarma = "Cimed Onefarma"
    colgate = "Colgate"
    cristalia = "Cristalia"
    dahuer_gspanasol = "Dahuer Gspanasol"
    danone = "Danone"
    delta = "Delta"
    embelleze = "Embelleze"
    ems_generico = "Ems Genérico"
    ems_marca = "Ems Marca"
    ems_prescricao = "Ems Prescrição"
    eurofarma = "Eurofarma"
    fini = "Fini"
    flora = "Flora"
    fqm_farma = "Fqm Farma"
    galderma = "Galderma"
    geolab = "Geolab"
    germed_pharma = "Germed Pharma"
    gross = "Gross"
    herbarium = "Herbarium"
    hisamitsu = "Hisamitsu"
    hypera_ch = "Hypera Ch"
    hypera_pp = "Hypera Pp"
    incoterm = "Incoterm"
    isdin_pro_farm_ltd = "Isdin Pro Farm Ltd"
    johnson_johnson = "Johnson & Johnson"
    kley_hertz = "Kley Hertz"
    legrand = "Legrand"
    loreal_dpgp = "Loreal Dpgp"
    maxinutri = "Maxinutri"
    medley = "Medley"
    medquimica = "Medquimica"
    melcon = "Melcon"
    merck_generico = "Merck Generico"
    merck_rx = "Merck Rx"
    mylan_brasil = "Mylan Brasil"
    natulab = "Natulab"
    neo_quimica_generico = "Neo Quimica Generico"
    neo_quimica_similar = "Neo Quimica Similar"
    nestle = "Nestle"
    nivea = "Nivea"
    nova_quimica = "Nova Quimica"
    omron = "Omron"
    perrigo = "Perrigo"
    pfizer_pbg = "Pfizer Pbg"
    pfizer_upjohn = "Pfizer Upjohn"
    pharlab = "Pharlab"
    prati_donaduzzi = "Prati Donaduzzi"
    ranbaxy = "Ranbaxy"
    sandoz = "Sandoz"
    sanfarma = "Sanfarma"
    sanofi = "Sanofi"
    semina = "Semina"
    sobral = "Sobral"
    takeda = "Takeda"
    teuto_brasileiro = "Teuto Brasileiro"
    torrent_farma = "Torrent Farma"
    torrent_generico = "Torrent Generico"
    uniao_quimica_f_n = "Uniao Quimica F N"
    unilever = "Unilever"
    vitamedic = "Vitamedic"
    vult = "Vult"
    waldemiro_pereira = "Waldemiro Pereira"
    zanphy = "Zanphy"
    bramed = "Bramed"
    df_farma = "Df Farma"
    distrimed = "Distrimed"
    divimed = "Divimed"
    drogacenter = "Drogacenter"
    elite = "Elite"
    emis_minas = "Emis Minas"
    gam = "Gam"
    gransmed = "Gransmed"
    grupo_acripel = "Grupo Acripel"
    grupo_andorinha = "Andorinha"
    grupo_cordeiro = "Grupo Cordeiro"
    grupo_dimebras = "Dimebras"
    grupo_dimed = "Dimed"
    grupo_dislab = "Dislab"
    grupo_dismed = "Dismed"
    grupo_dp4 = "Dp4"
    grupo_emefarma = "Emefarma "
    grupo_farmix = "Farmix"
    grupo_medicamental = "Medicamental"
    grupo_navarro = "Navarro"
    grupo_orgafarma = "Grupo Orgafarma"
    grupo_panpharma = "Panpharma"
    grupo_profarma = "Profarma"
    grupo_santa_cruz = "Santa Cruz"
    grupo_total = "Total"
    jkmedicamentos = "Jkmedicamentos"
    maxifarma = "Maxifarma"
    meditem = "Meditem"
    oriente_dist = "Oriente Dist"
    prosper = "Prosper"
    rio_drog_s = "Rio Drog S"
    servimed = "Servimed"
    solfarma = "Solfarma"
    stockfarma = "Stockfarma"
    t_farma = "T Farma"
    abc_frama = "ABC Farma"
    brasil_card = "Brasil Card"
    closeup = "Close Up"
    contento = "Contento"
    cote_facil = "Cote Fácil"
    funcional = "Funcional"
    getnet = "Getnet"
    imendes = "IMendes"
    metalfarma = "Metalfarma"
    monta_farma = "Montafarma"
    multifar = "Clube Multifar"
    rede = "Rede"
    smart = "Smart"
    trier = "Trier"
    iqvia = "IQVIA"
    linx = "Linx"
    linx_pay = "Linx Pay"


    mesa1 = "1"
    mesa2 = "2"
    mesa3 = "3"
    mesa4 = "4"
    mesa5 = "5"
    mesa6 = "6"
    mesa7 = "7"
    mesa8 = "8"
    mesa9 = "9"
    mesa10 = "10"
    mesa11 = "11"
    mesa12 = "12"
    mesa13 = "13"
    mesa14 = "14"
    mesa15 = "15"
    mesa16 = "16"
    mesa17 = "17"
    mesa18 = "18"
    mesa19 = "19"
    mesa20 = "20"
    mesa21 = "21"
    mesa22 = "22"
    mesa23 = "23"
    mesa24 = "24"
    mesa25 = "25"
    mesa26 = "26"
    mesa27 = "27"
    mesa28 = "28"
    mesa29 = "29"
    mesa30 = "30"
    mesa31 = "31"
    mesa32 = "32"
    mesa33 = "33"
    mesa34 = "34"
    mesa35 = "35"
    mesa36 = "36"
    mesa37 = "37"
    mesa38 = "38"
    mesa39 = "39"
    mesa40 = "40"
    mesa41 = "41"
    mesa42 = "42"
    mesa43 = "43"
    mesa44 = "44"
    mesa45 = "45"
    mesa46 = "46"
    mesa47 = "47"
    mesa48 = "48"
    mesa49 = "49"
    mesa50 = "50"
    mesa51 = "51"
    mesa52 = "52"
    mesa53 = "53"
    mesa54 = "54"
    mesa55 = "55"
    mesa56 = "56"
    mesa57 = "57"

    associado_choices = (
       (abbott_epd,  "Abbott Epd"),
        (abbott_nutricao,  "Abbott Nutrição"),
        (abc_frama,  "ABC Farma"),
        (acfarma,  "Acfarma"),
        (ache,  "Ache"),
        (ache_biosintetica,  "Ache Biosintetica"),
        (agafarma,  "Agafarma"),
        (althaiaequaliv,  "Althaiaequaliv"),
        (apsen,  "Apsen"),
        (asfar_desconto_facil,  "Asfar Desconto Facil"),
        (augefarma,  "Augefarma"),
        (baldacci,  "Baldacci"),
        (bayer_otc,  "Bayer Otc"),
        (bigfort,  "Bigfort"),
        (biodrogas,  "Biodrogas"),
        (biolab_genericos,  "Biolab Genericos"),
        (biolabsanus_farma,  "Biolabsanus Farma"),
        (blau_farmaceutica,  "Blau Farmaceutica"),
        (boa_farma,  "Boa Farma"),
        (bramed,  "Bramed"),
        (brasil_card,  "Brasil Card"),
        (canonne,  "Canonne"),
        (catarinense,  "Catarinense"),
        (cellera_delta,  "Cellera Delta"),
        (cimed,  "Cimed"),
        (cimed_onefarma,  "Cimed Onefarma"),
        (cityfarma,  "Cityfarma"),
        (closeup,  "Close Up"),
        (multifar,  "Clube Multifar"),
        (colgate,  "Colgate"),
        (compre_certo,  "Compre Certo"),
        (contento,  "Contento"),
        (coperfarma,  "Coperfarma"),
        (cote_facil,  "Cote Fácil"),
        (cristalia,  "Cristalia"),
        (dahuer_gspanasol,  "Dahuer Gspanasol"),
        (danone,  "Danone"),
        (delta,  "Delta"),
        (df_farma,  "Df Farma"),
        (distrimed,  "Distrimed"),
        (divimed,  "Divimed"),
        (droga_rede,  "Droga Rede"),
        (drogacenter,  "Drogacenter"),
        (drogamais,  "Drogamais"),
        (drogaria_atual,  "Drogaria Atual"),
        (drogaria_total,  "Drogaria Total"),
        (drogarias_conceito,  "Drogarias Conceito"),
        (drogarias_maestra,  "Drogarias Maestra"),
        (dsg_farma,  "Dsg Farma"),
        (elite,  "Elite"),
        (embelleze,  "Embelleze"),
        (emis_minas,  "Emis Minas"),
        (ems_generico,  "Ems Genérico"),
        (ems_marca,  "Ems Marca"),
        (ems_prescricao,  "Ems Prescrição"),
        (entrefarma,  "Entrefarma"),
        (eurofarma,  "Eurofarma"),
        (farma_100,  "Farma 100"),
        (farma_e_cia,  "Farma E Cia"),
        (farma_e_farma,  "Farma E Farma"),
        (farmacias_associadas,  "Farmacias Associadas"),
        (farmacias_conviva,  "Farmacias Conviva"),
        (farmagnus,  "Farmagnus"),
        (farmavale_e_cia,  "Farmavale E Cia"),
        (farmavip,  "Farmavip"),
        (farmelhor,  "Farmelhor"),
        (farmes,  "Farmes"),
        (fazfarma,  "Fazfarma"),
        (fini,  "Fini"),
        (flora,  "Flora"),
        (fqm_farma,  "Fqm Farma"),
        (funcional,  "Funcional"),
        (galderma,  "Galderma"),
        (gam,  "Gam"),
        (geolab,  "Geolab"),
        (germed_pharma,  "Germed Pharma"),
        (getnet,  "Getnet"),
        (gransmed,  "Gransmed"),
        (gross,  "Gross"),
        (grupo_acripel,  "Grupo Acripel"),
        (grupo_andorinha,  "Andorinha"),
        (grupo_cordeiro,  "Grupo Cordeiro"),
        (grupo_dimebras,  "Dimebras"),
        (grupo_dimed,  "Dimed"),
        (grupo_dislab,  "Dislab"),
        (grupo_dismed,  "Dismed"),
        (grupo_dp4,  "Dp4"),
        (grupo_emefarma,  "Emefarma "),
        (grupo_farmix,  "Farmix"),
        (grupo_medicamental,  "Medicamental"),
        (grupo_navarro,  "Navarro"),
        (grupo_orgafarma,  "Grupo Orgafarma"),
        (grupo_total,  "Total"),
        (grupofarma,  "Grupofarma"),
        (herbarium,  "Herbarium"),
        (hiperfarma,  "Hiperfarma"),
        (hisamitsu,  "Hisamitsu"),
        (hypera_ch,  "Hypera Ch"),
        (hypera_pp,  "Hypera Pp"),
        (imendes,  "IMendes"),
        (incoterm,  "Incoterm"),
        (inova_drogarias,  "Inova Drogarias"),
        (iqvia, "IQVIA"),
        (isdin_pro_farm_ltd,  "Isdin Pro Farm Ltd"),
        (jkmedicamentos,  "Jkmedicamentos"),
        (johnson_johnson,  "Johnson & Johnson"),
        (kley_hertz,  "Kley Hertz"),
        (legitima,  "Legitima"),
        (legrand,  "Legrand"),
        (lider_saude,  "Lider Saude"),
        (linx, "Linx"),
        (linx_pay, "Linx Pay"),
        (loreal_dpgp,  "Loreal Dpgp"),
        (maxifarma,  "Maxifarma"),
        (maxifarma,  "Maxifarma"),
        (maxinutri,  "Maxinutri"),
        (meditem,  "Meditem"),
        (medley,  "Medley"),
        (medquimica,  "Medquimica"),
        (melcon,  "Melcon"),
        (merck_generico,  "Merck Generico"),
        (merck_rx,  "Merck Rx"),
        (metalfarma,  "Metalfarma"),
        (mg_farma,  "Mg Farma"),
        (monta_farma,  "Montafarma"),
        (multmais,  "Multmais"),
        (mylan_brasil,  "Mylan Brasil"),
        (natulab,  "Natulab"),
        (neo_quimica_generico,  "Neo Quimica Generico"),
        (neo_quimica_similar,  "Neo Quimica Similar"),
        (nestle,  "Nestle"),
        (nivea,  "Nivea"),
        (nossa_rede,  "Nossa Rede"),
        (nova_quimica,  "Nova Quimica"),
        (nova_rede_drogarias,  "Nova Rede Drogarias"),
        (omron,  "Omron"),
        (oriente_dist,  "Oriente Dist"),
        (grupo_panpharma,  "Panpharma"),
        (perrigo,  "Perrigo"),
        (pfizer_pbg,  "Pfizer Pbg"),
        (pfizer_upjohn,  "Pfizer Upjohn"),
        (pharlab,  "Pharlab"),
        (pix_farma,  "Pix Farma"),
        (prati_donaduzzi,  "Prati Donaduzzi"),
        (grupo_profarma,  "Profarma"),
        (prosper,  "Prosper"),
        (ranbaxy,  "Ranbaxy"),
        (rede,  "Rede"),
        (farmacia_dias,  "Rede Carioca"),
        (rede_farmagente,  "Rede Farmagente"),
        (rede_liga_farma,  "Rede Liga Farma"),
        (rede_minas_farma,  "Rede Minas Farma"),
        (redefarma,  "Redefarma"),
        (redemais_farma,  "Redemais Farma"),
        (rio_drog_s,  "Rio Drog S"),
        (sanar,  "Sanar"),
        (sandoz,  "Sandoz"),
        (sanfarma,  "Sanfarma"),
        (sanofi,  "Sanofi"),
        (grupo_santa_cruz,  "Santa Cruz"),
        (semina,  "Semina"),
        (servimed,  "Servimed"),
        (sisfarma,  "Sisfarma"),
        (smart,  "Smart"),
        (sobral,  "Sobral"),
        (solfarma,  "Solfarma"),
        (stockfarma,  "Stockfarma"),
        (stylofarma,  "Stylofarma"),
        (super_popular,  "Super Popular"),
        (t_farma,  "T Farma"),
        (takeda,  "Takeda"),
        (tche_farmacias,  "Tche Farmacias"),
        (teuto_brasileiro,  "Teuto Brasileiro"),
        (torrent_farma,  "Torrent Farma"),
        (torrent_generico,  "Torrent Generico"),
        (trier,  "Trier"),
        (uai_farma,  "Uai Farma"),
        (ultra_popular,  "Ultra Popular"),
        (uniao_farma,  "Uniao Farma"),
        (uniao_quimica_f_n,  "Uniao Quimica F N"),
        (unifarma,  "Unifarma"),
        (unilever,  "Unilever"),
        (vida_farmacias,  "Vida Farmacias"),
        (vitamedic,  "Vitamedic"),
        (viva_mais,  "Viva Mais"),
        (vult,  "Vult"),
        (waldemiro_pereira,  "Waldemiro Pereira"),
        (zanphy,  "Zanphy"),
    )
    rede_choices = (
        (acfarma, "Acfarma"),
        (agafarma, "Agafarma"),
        (asfar_desconto_facil, "Asfar Desconto Facil"),
        (augefarma, "Augefarma"),
        (bigfort, "Bigfort"),
        (biodrogas, "Biodrogas"),
        (boa_farma, "Boa Farma"),
        (cityfarma, "Cityfarma"),
        (compre_certo, "Compre Certo"),
        (coperfarma, "Coperfarma"),
        (droga_rede, "Droga Rede"),
        (drogamais, "Drogamais"),
        (drogaria_atual, "Drogaria Atual"),
        (drogaria_total, "Drogaria Total"),
        (drogarias_conceito, "Drogarias Conceito"),
        (drogarias_maestra, "Drogarias Maestra"),
        (dsg_farma, "Dsg Farma"),
        (entrefarma, "Entrefarma"),
        (farma_100, "Farma 100"),
        (farma_e_cia, "Farma E Cia"),
        (farma_e_farma, "Farma E Farma"),
        (farmacia_dias, "Rede Carioca"),
        (farmacias_associadas, "Farmacias Associadas"),
        (farmacias_conviva, "Farmacias Conviva"),
        (farmagnus, "Farmagnus"),
        (farmavale_e_cia, "Farmavale E Cia"),
        (farmavip, "Farmavip"),
        (farmelhor, "Farmelhor"),
        (farmes, "Farmes"),
        (fazfarma, "Fazfarma"),
        (grupofarma, "Grupofarma"),
        (hiperfarma, "Hiperfarma"),
        (inova_drogarias, "Inova Drogarias"),
        (legitima, "Legitima"),
        (lider_saude, "Lider Saude"),
        (maxifarma, "Maxifarma"),
        (mg_farma, "Mg Farma"),
        (multmais, "Multmais"),
        (nossa_rede, "Nossa Rede"),
        (nova_rede_drogarias, "Nova Rede Drogarias"),
        (pix_farma, "Pix Farma"),
        (rede_farmagente, "Rede Farmagente"),
        (rede_liga_farma, "Rede Liga Farma"),
        (rede_minas_farma, "Rede Minas Farma"),
        (redefarma, "Redefarma"),
        (redemais_farma, "Redemais Farma"),
        (sanar, "Sanar"),
        (sisfarma, "Sisfarma"),
        (stylofarma, "Stylofarma"),
        (super_popular, "Super Popular"),
        (tche_farmacias, "Tche Farmacias"),
        (uai_farma, "Uai Farma"),
        (ultra_popular, "Ultra Popular"),
        (uniao_farma, "Uniao Farma"),
        (unifarma, "Unifarma"),
        (vida_farmacias, "Vida Farmacias"),
        (viva_mais, "Viva Mais"),
    )

    mesa_choices = (
        (mesa1, "1"),
        (mesa2, "2"),
        (mesa3, "3"),
        (mesa4, "4"),
        (mesa5, "5"),
        (mesa6, "6"),
        (mesa7, "7"),
        (mesa8, "8"),
        (mesa9, "9"),
        (mesa10, "10"),
        (mesa11, "11"),
        (mesa12, "12"),
        (mesa13, "13"),
        (mesa14, "14"),
        (mesa15, "15"),
        (mesa16, "16"),
        (mesa17, "17"),
        (mesa18, "18"),
        (mesa19, "19"),
        (mesa20, "20"),
        (mesa21, "21"),
        (mesa22, "22"),
        (mesa23, "23"),
        (mesa24, "24"),
        (mesa25, "25"),
        (mesa26, "26"),
        (mesa27, "27"),
        (mesa28, "28"),
        (mesa29, "29"),
        (mesa30, "30"),
        (mesa31, "31"),
        (mesa32, "32"),
        (mesa33, "33"),
        (mesa34, "34"),
        (mesa35, "35"),
        (mesa36, "36"),
        (mesa37, "37"),
        (mesa38, "38"),
        (mesa39, "39"),
        (mesa40, "40"),
        (mesa41, "41"),
        (mesa42, "42"),
        (mesa43, "43"),
        (mesa44, "44"),
        (mesa45, "45"),
        (mesa46, "46"),
        (mesa47, "47"),
        (mesa48, "48"),
        (mesa49, "49"),
        (mesa50, "50"),
        (mesa51, "51"),
        (mesa52, "52"),
        (mesa53, "53"),
        (mesa54, "54"),
        (mesa55, "55"),
        (mesa56, "56"),
        (mesa57, "57"),
    )

    now = datetime.now()
    mesa = models.CharField(max_length=2, choices=mesa_choices, blank=False)
    associado = models.CharField(max_length=50, choices=associado_choices, blank=False)
    rede = models.CharField(max_length=50, choices=rede_choices, blank=False)
    dia = models.DateField(default=now.strftime("%d/%m/%Y"))
    hora = models.TimeField(default=now.strftime("%H:%M:%S"))

    def __str__(self):
        texto = "{} - {}".format(self.associado, self.rede)
        return texto

