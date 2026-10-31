"""NCM -> MP3/FLAC converter (public NetEase format keys)."""
import base64, json, struct, sys
from pathlib import Path

# Core key (public constant of the NCM format)
CORE_KEY = b"hzHRAmso5kInbaxW"
META_KEY = b"#14ljk_!\\]&0U<'("

try:
    from Crypto.Cipher import AES
except ImportError:
    sys.exit("NEED_PYCRYPTO")

def unpad(data):
    n = data[-1]
    return data[:-n] if 0 < n <= 16 else data

def main(src, dst_dir):
    src = Path(src)
    data = src.read_bytes()
    assert data[:8] == b"CTENFDAM", "not an ncm file"
    p = 8
    p += 2                       # gap (2 bytes)
    kl = struct.unpack("<I", data[p:p+4])[0]; p += 4
    key = bytes(b ^ 0x64 for b in data[p:p+kl]); p += kl
    key = unpad(AES.new(CORE_KEY, AES.MODE_ECB).decrypt(key))[17:]
    # rc4 box
    box = list(range(256))
    j = 0
    for i in range(256):
        j = (j + box[i] + key[i]) & 0xFF
        box[i], box[j] = box[j], box[i]
    # meta (skip)
    ml = struct.unpack("<I", data[p:p+4])[0]; p += 4 + ml
    p += 4            # crc
    p += 5            # gap
    il = struct.unpack("<I", data[p:p+4])[0]; p += 4
    img = data[p:p+il]; p += il
    # audio
    audio = bytearray(data[p:])
    for i in range(len(audio)):
        audio[i] ^= box[(i + 1) & 0xFF]
    out = dst_dir / (src.stem + ".mp3")
    out.write_bytes(audio)
    print("OK", out, len(audio))

if __name__ == "__main__":
    main(sys.argv[1], Path(sys.argv[2]))
