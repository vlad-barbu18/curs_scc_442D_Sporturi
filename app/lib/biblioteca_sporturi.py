INFO_1 = [
    {
        "camp1": "Origine si dezvoltare",
        "camp2": (
            "Padelul a aparut in Mexic in anii 1960, fiind creat ca o varianta "
            "mai accesibila si mai dinamica a tenisului. Ulterior, sportul s-a "
            "raspandit rapid in Spania si America Latina, unde a devenit extrem "
            "de popular. In prezent, padelul este practicat in tot mai multe tari "
            "din Europa, fiind apreciat pentru faptul ca poate fi invatat relativ "
            "usor, dar permite un nivel ridicat de strategie si tehnica."
        ),
    },
    {
        "camp1": "Terenul de joc",
        "camp2": (
            "Terenul de padel este mai mic decat un teren de tenis si este "
            "inconjurat de pereti de sticla si zone de plasa metalica. Acesti "
            "pereti nu au doar rol de delimitare, ci fac parte din joc, deoarece "
            "mingea poate ricosa din ei dupa ce atinge solul. Aceasta caracteristica "
            "face ca padelul sa fie un sport spectaculos, cu schimburi lungi si "
            "lovituri imprevizibile."
        ),
    },
    {
        "camp1": "Formatul meciului",
        "camp2": (
            "Padelul se joaca de obicei la dublu, adica doua echipe formate din "
            "cate doi jucatori. Acest format pune accent pe comunicarea dintre "
            "coechipieri, pe pozitionarea corecta pe teren si pe luarea rapida "
            "a deciziilor. Spre deosebire de tenis, forta loviturii nu este mereu "
            "cel mai important aspect, deoarece plasamentul si strategia pot avea "
            "un rol decisiv."
        ),
    },
    {
        "camp1": "Popularitate",
        "camp2": (
            "Padelul a devenit popular deoarece este mai usor de practicat pentru "
            "incepatori decat alte sporturi de racheta. Regulile sunt relativ simple, "
            "iar dimensiunea redusa a terenului face ca jucatorii sa fie implicati "
            "constant in actiune. La nivel avansat, sportul necesita reflexe bune, "
            "coordonare, rezistenta si o buna intelegere tactica."
        ),
    },
]


INFO_2 = [
    {
        "camp1": "Racheta de padel",
        "camp2": (
            "Racheta de padel este diferita de cea de tenis, deoarece nu are corzi. "
            "Aceasta este solida, perforata si realizata de obicei din materiale "
            "usoare si rezistente. Forma rachetei poate influenta stilul de joc: "
            "unele modele ofera mai mult control, iar altele sunt concepute pentru "
            "lovituri mai puternice."
        ),
    },
    {
        "camp1": "Mingea folosita",
        "camp2": (
            "Mingea de padel seamana cu mingea de tenis, dar are o presiune usor "
            "diferita. Aceasta diferenta influenteaza viteza si inaltimea sariturii, "
            "adaptand mingea la dimensiunea mai mica a terenului si la stilul specific "
            "al jocului."
        ),
    },
    {
        "camp1": "Reguli de baza",
        "camp2": (
            "Serviciul se executa de jos, dupa ce mingea este lasata sa cada o data "
            "pe sol. Mingea trebuie trimisa in terenul advers si trebuie sa atinga "
            "solul inainte de a lovi peretii. Dupa ce mingea a atins terenul, peretii "
            "pot fi folositi pentru a continua punctul."
        ),
    },
    {
        "camp1": "Strategie de joc",
        "camp2": (
            "In padel, strategia este la fel de importanta ca tehnica. Jucatorii "
            "trebuie sa aleaga momentul potrivit pentru atac, sa controleze zona "
            "fileului si sa foloseasca peretii pentru a recupera mingi dificile. "
            "O echipa bine organizata poate castiga puncte prin plasament, rabdare "
            "si coordonare, nu doar prin lovituri puternice."
        ),
    },
    {
        "camp1": "Beneficii fizice",
        "camp2": (
            "Padelul contribuie la imbunatatirea conditiei fizice, deoarece implica "
            "deplasari rapide, schimbari de directie, reflexe si coordonare mana-ochi. "
            "Fiind un sport dinamic, ajuta la dezvoltarea rezistentei, agilitatii si "
            "concentrarii. In plus, fiind jucat la dublu, are si o componenta sociala "
            "importanta."
        ),
    },
]


def functie_1_padel():
    html = "<h2>Informatii generale despre padel</h2>"

    for item in INFO_1:
        html += f"""
        <p>
            <b>{item['camp1']}</b>: {item['camp2']}
        </p>
        """

    return html


def functie_2_padel():
    html = "<h2>Echipament, reguli si strategie in padel</h2>"

    for item in INFO_2:
        html += f"""
        <p>
            <b>{item['camp1']}</b>: {item['camp2']}
        </p>
        """

    return html
