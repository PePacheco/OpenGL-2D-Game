# ***********************************************************************************
#   ExibePoligonos.py
#       Autores: Pedro Pacheco e Lucas Garcia
#       pinho@pucrs.br
#   Este programa exibe um polígono em OpenGL
#   Para construir este programa, foi utilizada a biblioteca PyOpenGL, disponível em
#   http://pyopengl.sourceforge.net/documentation/index.html
#
#   Sugere-se consultar também as páginas listadas
#   a seguir:
#   http://bazaar.launchpad.net/~mcfletch/pyopengl-demo/trunk/view/head:/PyOpenGL-Demo/NeHe/lesson1.py
#   http://pyopengl.sourceforge.net/documentation/manual-3.0/index.html#GLUT
# ***********************************************************************************

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Poligonos import *

# ***********************************************************************************
Mapa = Polygon()

A = Polygon()
B = Polygon()
Uniao = Polygon()
Intersecao = Polygon()
Diferenca = Polygon()

# Limites lógicos da área de desenho
Min = Point()
Max = Point()


Ponto = Point()
Meio = Point()
Terco = Point()
Largura = Point()

# ***********************************************************************************
def ProdEscalar(v1, v2):
    return v1.x*v2.x + v1.y*v2.y+ v1.z*v2.z;

# ***********************************************************************************
def ProdVetorial (v1, v2, vresult):
    vresult.x = v1.y * v2.z - (v1.z * v2.y)
    vresult.y = v1.z * v2.x - (v1.x * v2.z)
    vresult.z = v1.x * v2.y - (v1.y * v2.x)

# ***********************************************************************************
def reshape(w,h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Cria uma folga na Janela de Seleção, com 10% das dimensões do polígono
    BordaX = abs(Max.x-Min.x)*0.1
    BordaY = abs(Max.y-Min.y)*0.1
    #glOrtho(Min.x-BordaX, Max.x+BordaX, Min.y-BordaY, Max.y+BordaY, 0.0, 1.0)
    glOrtho(Min.x, Max.x, Min.y, Max.y, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def DesenhaEixos():
    glBegin(GL_LINES);
    # eixo horizontal
    glVertex2f(Min.x,Meio.y)
    glVertex2f(Max.x,Meio.y)
    #  eixo vertical 1
    glVertex2f(Min.x + Terco.x,Min.y)
    glVertex2f(Min.x + Terco.x,Max.y)
    #  eixo vertical 2
    glVertex2f(Min.x + 2*Terco.x,Min.y)
    glVertex2f(Min.x + 2*Terco.x,Max.y)
    glEnd()

# ***********************************************************************************
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(1)
    DesenhaEixos()
    
    glPushMatrix()
    glTranslatef(0, Meio.y, 0)
    glScalef(0.33, 0.5, 1)
    glLineWidth(2)
    glColor3f(1,1,0); # R, G, B  [0..1]
    A.desenhaPoligono()
    glColor3f(1.0, 0.0, 0.0)
    B.desenhaPoligono()
    glPopMatrix()

    # #Desenha o polígono A no meio, acima
    # glPushMatrix()
    # glTranslatef(Terco.x, Meio.y, 0)
    # glScalef(0.33, 0.5, 1)
    # glLineWidth(2)
    # glColor3f(1,1,0) # R, G, B  [0..1]
    # A.desenhaPoligono()
    # glPopMatrix()

    # # Desenha o polígono B no canto superior direito
    # glPushMatrix()
    # glTranslatef(Terco.x*2, Meio.y, 0)
    # glScalef(0.33, 0.5, 1)
    # glLineWidth(2)
    # glColor3f(1,0,0); # R, G, B  [0..1]
    # B.desenhaPoligono()
    # glPopMatrix()
    
    # # Desenha o polígono A no canto inferior esquerdo
    # glPushMatrix()
    # glTranslatef(0, 0, 0)
    # glScalef(0.33, 0.5, 1)
    # glLineWidth(2)
    # glColor3f(1,1,0); # R, G, B  [0..1]
    # A.desenhaPoligono()
    # glPopMatrix()
    
    # # Desenha o polígono B no meio, abaixo
    # glPushMatrix()
    # glTranslatef(Terco.x, 0, 0)
    # glScalef(0.33, 0.5, 1)
    # glLineWidth(2)
    # glColor3f(1,0,0) # R, G, B  [0..1]
    # B.desenhaPoligono()
    # glPopMatrix()

    glutSwapBuffers()

# ***********************************************************************************
# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)
#ESCAPE = '\033'
ESCAPE = b'\x1b'
def keyboard(*args):
    #print (args)
    # If escape is pressed, kill everything.
    if args[0] == b'q':
        os._exit(0)
    if args[0] == ESCAPE:
        os._exit(0)
    if args[0] == b'1':
        Mapa.imprimeVertices()
    if args[0] == b'2':
        LePontosDeArquivo()
    if args[0] == b'3':
        LePontosDeArquivo()
    if args[0] == b'4':
        LePontosDeArquivo()
# Força o redesenho da tela
    glutPostRedisplay()

# ***********************************************************************************
# LePontosDeArquivo(Nome):
#  Realiza a leitura de uam arquivo com as coordenadas do polígono
# ***********************************************************************************
def LePontosDeArquivo(Nome, P):

    Pt = Point()
    infile = open(Nome)
    line = infile.readline()
    number = int(line)
    for line in infile:
        words = line.split() # Separa as palavras na linha
        x = float (words[0])
        y = float (words[1])
        P.insereVertice(x,y,0)
        #Mapa.insereVertice(*map(float,line.split))
    infile.close()
    #print ("Após leitura do arquivo:")
    #Min.imprime()
    #Max.imprime()

def ObtemMaximo (P1, P2):
    Max = copy.deepcopy(P1)
    
    if (P2.x > Max.x):
        Max.x = P2.x

    if (P2.y > Max.y):
        Max.y = P2.y

    if (P2.z > Max.z):
        Max.z = P2.z

    return Max;

def ObtemMinimo (P1, P2):
    Min = copy.deepcopy(P1)
    
    if (P2.x < Min.x):
        Min.x = P2.x
    
    if (P2.y < Min.y):
        Min.y = P2.y
    
    if (P2.z < Min.z):
        Min.z = P2.z

    return Min;

def hasRetaIntersection(k, l, m, n):
    det = (n.x - m.x) * (l.y - k.y)  -  (n.y - m.y) * (l.x - k.x)

    if (det == 0.0):
        return False # Não há intersecção

    s = ((n.x - m.x) * (m.y - k.y) - (n.y - m.y) * (m.x - k.x))/ det 
    t = ((l.x - k.x) * (m.y - k.y) - (l.y - k.y) * (m.x - k.x))/ det 

    if (s >= 0.0 and s <= 1.0 and t >= 0.0 and t <= 1.0):
        return True
    else:
        return False

def hasPolygonIntersection(S1, S2):
    size1 = len(S1.Vertices)
    size2 = len(S2.Vertices)
    for p1 in range(size1):
        if S1.Vertices[p1] == S1.Vertices[-1]:
            break
        for p2 in range(size2):
            if S2.Vertices[p2] == S2.Vertices[-1]:
                break
            if hasRetaIntersection(S1.Vertices[p1], S1.Vertices[p1+1], S2.Vertices[p2], S2.Vertices[p2+1]):
                return True
    return False

def getRetaIntersection(k, l, m, n):
    det = (n.x - m.x) * (l.y - k.y)  -  (n.y - m.y) * (l.x - k.x)

    s = ((n.x - m.x) * (m.y - k.y) - (n.y - m.y) * (m.x - k.x))/ det 
    t = ((l.x - k.x) * (m.y - k.y) - (l.y - k.y) * (m.x - k.x))/ det 

    return s, t

def getPolygonIntersection(S1, S2):
    size1 = len(S1.Vertices)
    size2 = len(S2.Vertices)
    points = []
    indexForNewVerticeS1 = {}
    indexForNewVerticeS2 = {}
    
    for p1 in range(size1):
        indexP1 = p1
        indexP1P = 0

        if p1 == size1 -1:
            indexP1P = 0
        else:
            indexP1P = p1 + 1

        for p2 in range(size2):
            indexP2 = p2
            indexP2P = 0

            if p2 == size2 -1:
                indexP2P = 0
            else:
                indexP2P = p2 + 1

            if hasRetaIntersection(S1.Vertices[indexP1], S1.Vertices[indexP1P], S2.Vertices[indexP2], S2.Vertices[indexP2P]):
                # Pegando os pontos de intersecção
                temp = getRetaIntersection(S1.Vertices[indexP1], S1.Vertices[indexP1P], S2.Vertices[indexP2], S2.Vertices[indexP2P])
                point1 = getVerticeIntersec(S1.Vertices[indexP1], S1.Vertices[indexP1P], temp[1])
                point2 = getVerticeIntersec(S2.Vertices[indexP2], S2.Vertices[indexP2P], temp[0])

                # Inserindo em ambos poligonos
                S1.insereVerticePosition(point1.x,point1.y,0,indexP1+1)
                S2.insereVerticePosition(point2.x,point2.y,0,indexP2+1)

                # Aumentando os tamanhos e os indices de acesso
                indexP1 += 1
                indexP2 += 1
                size2 += 1
                size1 += 1


#Popula um vetor de tuplas chamado arestas no poligono   
def populaArestasPoligono(P1, P2):
        for p1 in range(len(P1.Vertices)):
            indexP1 = p1
            indexP1P = 0
            if p1 == len(P1.Vertices)-1:
                indexP1P = 0
            else:
                indexP1P = p1 + 1
            if arestaIsInside(P1.Vertices[indexP1], P1.Vertices[indexP1P], P2):
                P1.Arestas['in'].append( (P1.Vertices[indexP1],P1.Vertices[indexP1P]) )
            else:
                P1.Arestas['out'].append( (P1.Vertices[indexP1],P1.Vertices[indexP1P]) )

#Funcionando como deveria
def getPontoMedioAresta(aresta):
    pontoMediox = (aresta[0].x + aresta[1].x)/2 
    pontoMedioy = (aresta[0].y + aresta[1].y)/2 
    return pontoMediox, pontoMedioy


def getVerticeIntersec(r1, r2, t):
    x = r1.x*(1 - t) + r2.x * t
    y = r1.y*(1 - t) + r2.y * t
    return Point(x, y, 0)

def arestaIsInside(p1, p2, P2):
    pontoMedioX, pontoMedioY = getPontoMedioAresta((p1, p2))
    for point in P2.Vertices:
        continue
        point.imprime()
    return False

def init():
    global Min, Max, Meio, Terco, Largura  # Variáveis usadas para definir os limites da Window
    
    LePontosDeArquivo("Retangulo.txt", A)
    Min, Max = A.getLimits()
    LePontosDeArquivo("Triangulo.txt", B)
    MinAux, MaxAux = B.getLimits()
    
    # Atualiza os limites globais após cada leitura
    Min = ObtemMinimo(Min, MinAux)
    Max = ObtemMaximo(Max, MaxAux)

    # Ajusta a largura da janela lógica em função do tamanho dos polígonos
    Largura.x = Max.x-Min.x
    Largura.y = Max.y-Min.y
    
    # Calcula 1/3 da largura da janela
    Terco = Largura
    fator = 1.0/3.0
    Terco.multiplica(fator, fator, fator)
    
    #Calcula 1/2 da largura da janela
    Meio.x = (Max.x+Min.x)/2
    Meio.y = (Max.y+Min.y)/2
    Meio.z = (Max.z+Min.z)/2

    # PEGANDO OS PONTOS DE INTERSECÇÃO
    pointsIntersec = []
    if(hasPolygonIntersection(A,B)):
        getPolygonIntersection(A,B)

    # Criando as arestas dos poligonos
    # populaArestasPoligono(B)
    populaArestasPoligono(A, B)
    populaArestasPoligono(B, A)

    for a,b in B.Arestas['out']:
        continue
        a.imprime()
        b.imprime()
        print('------')

    
    

# ***********************************************************************************
# Programa Principal
# ***********************************************************************************

init()
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 500)
glutInitWindowPosition(100, 100)
wind = glutCreateWindow("Exibe Polignos")
glutDisplayFunc(display)
#glutIdleFunc(showScreen)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)

try:
    glutMainLoop()
except SystemExit:
    pass
