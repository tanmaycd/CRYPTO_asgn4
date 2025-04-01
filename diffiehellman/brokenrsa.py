def factor(n):
    # More robust integer factorization
    for i in range(2, min(int(n**0.5) + 1, 1000000)):
        if n % i == 0:
            return i, n // i
    return None

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, min(int(n**0.5) + 1, 1000)):
        if n % i == 0:
            return False
    return True

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def decrypt_rsa(n, e, ct):
    # Multiple attempts to factor
    import itertools
    
    # Custom range generator to explore more factor candidates
    def custom_range():
        candidates = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for start in candidates:
            yield from range(start, min(1000000, int(n**0.5) + 1), 2)
    
    for i in custom_range():
        if n % i == 0:
            p, q = i, n // i
            if is_prime(p) and is_prime(q):
                phi = (p-1) * (q-1)
                d = mod_inverse(e, phi)
                decrypted = pow(ct, d, n)
                
                # Try decoding as hex and ASCII
                try:
                    hex_result = hex(decrypted)[2:]
                    # Pad with zeros if needed
                    if len(hex_result) % 2 != 0:
                        hex_result = '0' + hex_result
                    ascii_result = bytes.fromhex(hex_result).decode('utf-8', errors='ignore')
                    print(f"Factors: {p}, {q}")
                    print(f"Decrypted: {decrypted}")
                    print(f"Hex: {hex_result}")
                    print(f"ASCII: {ascii_result}")
                    return decrypted
                except Exception as e:
                    print(f"Decoding error: {e}")
    
    return None

n = 27772857409875257529415990911214211975844307184430241451899407838750503024323367895540981606586709985980003435082116995888017731426634845808624796292507989171497629109450825818587383112280639037484593490692935998202437639626747133650990603333094513531505209954273004473567193235535061942991750932725808679249964667090723480397916715320876867803719301313440005075056481203859010490836599717523664197112053206745235908610484907715210436413015546671034478367679465233737115549451849810421017181842615880836253875862101545582922437858358265964489786463923280312860843031914516061327752183283528015684588796400861331354873
e = 16
ct = 11303174761894431146735697569489134747234975144162172162401674567273034831391936916397234068346115459134602443963604063679379285919302225719050193590179240191429612072131629779948379821039610415099784351073443218911356328815458050694493726951231241096695626477586428880220528001269746547018741237131741255022371957489462380305100634600499204435763201371188769446054925748151987175656677342779043435047048130599123081581036362712208692748034620245590448762406543804069935873123161582756799517226666835316588896306926659321054276507714414876684738121421124177324568084533020088172040422767194971217814466953837590498718

decrypt_rsa(n, e, ct)