import pathlib
import sys

_parentdir = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parentdir))

from lib.vigenere import Vigenere
from example_model import ExampleModel

vigenere = Vigenere()
enc = vigenere.encrypt(
"""
Isaac Asimov (romaniz.: Isaak Yudavich Azimov; Petrovichi, Rússia Soviética,
atual Rússia, 2 de janeiro de 1920 — Brooklyn, 6 de abril de 1992) foi um
escritor e bioquímico norte-americano, nascido na Rússia, autor de obras de
ficção científica e divulgação científica.
Asimov é considerado um dos mestres da ficção científica e, junto com Robert
A. Heinlein e Arthur C. Clarke, foi considerado um dos "três grandes" dessa área
da literatura. A obra mais famosa de Asimov é a Série da Fundação, também conhecida
como Trilogia da Fundação, que faz parte da série do Império Galáctico e que logo
combinou com a Série Robôs. Também escreveu obras de mistério e fantasia, assim
como uma grande quantidade de não-ficção. No total, escreveu ou editou mais de
500 volumes, aproximadamente 90 000 cartas ou postais, e tem obras em cada
categoria importante do sistema de classificação bibliográfica de Dewey, exceto
em filosofia.
""", "minhachave")

chalenge_file = open(str(_parentdir)+"/examples/data/chalenge03.txt", "w")
chalenge_file.write(enc)
chalenge_file.close()

example03 = ExampleModel("data/chalenge03.txt", 10, 13, "pt-br")
example03.run()
