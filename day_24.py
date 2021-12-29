import functools
import sys
inf = sys.argv[1] if len(sys.argv) > 1 else 'input'

ll = [x for x in open(inf).read().strip().split('\n')]



# BEGIN <UNUSED SECTION>
vs = 'wxyz'
def simulate(line, state):
	state = list(state)
	cmd = line.split(" ")[0]
	if cmd == 'inp':
		raise Exception("")
	a = line.split(" ")[1]
	b = line.split(" ")[2]
	def parse(x):
		if x in vs:
			return state[vs.index(x)]
		return int(x)
	if cmd == 'add':
		state[vs.index(a)] += parse(b)
	if cmd == 'mul':
		state[vs.index(a)] *= parse(b)
	if cmd == 'div':
		state[vs.index(a)] //= parse(b)
	if cmd == 'mod':
		state[vs.index(a)] %= parse(b)
	if cmd == 'eql':
		state[vs.index(a)] = int(state[vs.index(a)] == parse(b))
	return tuple(state)
@functools.lru_cache(maxsize=None)
def run2(ch, zstart, w):
	state = (w, 0, 0, zstart)
	for i in range(ch*18+1, ch*18+18):
		state = simulate(ll[i], state)
	r = state[3]
	print(run(ch, zstart, w) == r)
	return r
# END </UNUSED SECTION>


# my input
#AX = [13, 11, 15, -11, 14, 0, 12, 12, 14, -6, -10, -12, -3, -5]
#DZ = [1, 1, 1, 26, 1, 26, 1, 1, 1, 26, 26, 26, 26, 26]
#AY = [13, 10, 5, 14, 5, 15, 4, 11, 1, 15, 12, 8, 14, 9]

AX = []
DZ = []
AY = []
for lineno, line in enumerate(ll):
	if "add x " in line and "add x z" not in line:
		AX.append(int(line.split()[2]))
	if "div z " in line:
		DZ.append(int(line.split()[2]))
	if "add y " in line and lineno%18 == 15:
		AY.append(int(line.split()[2]))
print("Extracted from input", AX, DZ, AY)

if len(AX) != 14 or len(DZ) != 14 or len(AY) != 14:
	raise Exception("couldn't understand your input")

def run(ch, z, w):
	x = AX[ch] + (z % 26)
	z = z // DZ[ch]
	if x != w:
		z *= 26
		z += w + AY[ch]
	return z

Zbudget = [26**len([x for x in range(len(DZ)) if DZ[x]==26 and x >= i]) for i in range(len(DZ))]
print("Threshold for giving up due to Z being too high, at each stage has been calculated as", Zbudget)
CANDIDATES = list(range(1, 10))
@functools.lru_cache(maxsize=None)
def search(ch, zsofar):
	if ch == 14:
		if zsofar == 0:
			return [""]
		return []
	if zsofar > Zbudget[ch]:
		return []
	xwillbe = AX[ch] + zsofar % 26
	wopts = CANDIDATES
	if xwillbe in range(1, 10):
		wopts = [xwillbe]
	ret = []
	for w in wopts:
		znext = run(ch, zsofar, w)
		nxt = search(ch + 1, znext)
		for x in nxt:
			ret.append(str(w) + x)
	return ret

solns = search(0, 0)
solns = [int(x) for x in solns]
print("num solutions", len(solns))
print(max(solns), min(solns))

