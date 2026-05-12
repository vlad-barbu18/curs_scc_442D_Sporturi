"""
Biblioteca pentru tema Sporturi.
Sportul: Ciclism.
"""

def competitii_ciclism(imagine_url=None):
    """
    Returneaza informatii despre competitii importante de ciclism.
    Poate primi optional un URL catre o imagine.
    """
    imagine_html = ""

    if imagine_url:
        imagine_html = f"""
        <figure>
            <img src="{imagine_url}"
                 alt="stage2"
                 width="600">
            <figcaption>
                Imagine personala realizata ca spectator la Turul Italiei 2026,
                etapa a 2-a.
            </figcaption>
        </figure>
        """

    return f"""
    {imagine_html}

    <h2>Competitii importante de ciclism</h2>

    <p>
    Ciclismul este un sport care include mai multe tipuri de competitii:
    curse pe sosea, curse pe etape, mountain bike, ciclism pe pista si BMX.
    Cele mai cunoscute competitii sunt marile tururi si campionatele internationale.
    </p>

    <ul>
        <li><b>Tour de France</b> - una dintre cele mai cunoscute competitii de ciclism pe sosea.</li>
        <li><b>Giro d'Italia / Turul Italiei</b> - mare tur desfasurat in Italia.</li>
        <li><b>La Vuelta a Espana</b> - competitie importanta desfasurata in Spania.</li>
        <li><b>Campionatele Mondiale UCI</b> - competitie internationala pentru mai multe discipline.</li>
        <li><b>Jocurile Olimpice</b> - includ probe de ciclism pe sosea, pista, BMX si mountain bike.</li>
    </ul>

    <p>
    In aceste competitii, ciclistii sunt evaluati dupa timp, etape castigate,
    puncte acumulate si pozitia in clasamentul general.
    </p>

    <p>
    Un exemplu de competitie relevanta pentru aceasta pagina este Turul Italiei,
    una dintre cele trei mari curse pe etape din ciclismul profesionist.
    </p>
    """


def echipament_ciclism(imagine_url=None):
    """
    Returneaza informatii despre echipamentele folosite in ciclism.
    Poate primi optional un URL catre o imagine.
    """
    imagine_html = ""

    if imagine_url:
        imagine_html = f"""
        <figure>
            <img src="{imagine_url}"
                 alt="bicla"
                 width="600">
            <figcaption>
                Bicicleta de sosea folosita ca exemplu pentru echipamentul de ciclism.
            </figcaption>
        </figure>
        """

    return f"""
    {imagine_html}

    <h2>Echipamente folosite in ciclism</h2>

    <p>
    Echipamentul de ciclism este important pentru siguranta, confort si performanta.
    Acesta difera in functie de tipul de ciclism practicat: sosea, mountain bike,
    pista, gravel sau BMX.
    </p>

    <ul>
        <li><b>Bicicleta</b> - principalul echipament, adaptat tipului de traseu.</li>
        <li><b>Casca</b> - protejeaza capul in cazul cazaturilor.</li>
        <li><b>Manusi</b> - ofera aderenta si reduc presiunea asupra palmelor.</li>
        <li><b>Ochelari</b> - protejeaza ochii de vant, praf si insecte.</li>
        <li><b>Tricou de ciclism</b> - realizat din material usor si respirabil.</li>
        <li><b>Pantaloni cu bazon</b> - cresc confortul pe distante lungi.</li>
        <li><b>Incaltaminte speciala</b> - ajuta la transmiterea eficienta a fortei catre pedale.</li>
        <li><b>Computer de bicicleta</b> - poate afisa viteza, distanta, timpul si traseul GPS.</li>
    </ul>

    <p>
    Pentru ciclismul de sosea, bicicleta este gandita pentru viteza si eficienta.
    De obicei are cadru usor, anvelope inguste, ghidon specific si o pozitie
    aerodinamica a ciclistului.
    </p>
    """