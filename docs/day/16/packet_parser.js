function* bitstream(hexdata) {
    for (let s of hexdata.trim()) {
        let v = parseInt(s,16)
        for (let i = 3; i > -1; --i) {
            yield (v >> i) & 1
        }
    }
}
function* islice(seq, stop) {
    for (let i = 0; i < stop; ++i) {
        let obj = seq.next()
        if (obj.done) { break }
        yield obj.value
    }
}
function iint(seq, w) {
    let x = 0
    for (let i of islice(seq, w)) {
        x = (x << 1) | i
    }
    return x
}
function* parsePacket(bits) {
    while (true) {
        let ver = iint(bits, 3)
        let pid = iint(bits, 3)
        if (pid === 4) {
            let x = 0
            while (true) {
                s = iint(bits, 1)
                c = iint(bits, 4)
                x = (x << 4) | c
                if (!s) { break }
            }
            yield [ver, pid, x]
        }
        else {
            let inner = undefined
            if (iint(bits, 1)) {
                let nsub = iint(bits, 11)
                inner = [...islice(parsePacket(bits), nsub)]
            }
            else {
                let plen = iint(bits, 15)
                if (!plen) { break }
                inner = [...parsePacket(islice(bits, plen))]
            }
            yield [ver, pid, inner]
        }
    }
}