from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"response": "Success"}), 200

@app.route('/online/', methods=['POST'])
def online():
    data = request.get_json()
    if data.get("packet", {}).get("status") == "online":
        return jsonify({"response": "Success"}), 200
    else:
        return jsonify({"response": "Failed"}), 400

@app.route('/offline', methods=['POST'])
def offline():
    data = request.get_json()
    if data.get("packet", {}).get("status") == "offline":
        return jsonify({"response": "Success"}), 200
    else:
        return jsonify({"response": "Failed"}), 400

@app.route("/password-check-list/", methods=['GET'])
def passwordCheckList():
    return jsonify(
        {"packetInfo": {"node_id": "Master", "status": "Online", "sendData": "True", "lastGeneratedPassword": "j\\"}, "passwords": ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "/", "<", ">", "?", "\\", "aa", "ab", "ac", "ad", "ae", "af", "ag", "ah", "ai", "aj", "ak", "al", "am", "an", "ao", "ap", "aq", "ar", "as", "at", "au", "av", "aw", "ax", "ay", "az", "aA", "aB", "aC", "aD", "aE", "aF", "aG", "aH", "aI", "aJ", "aK", "aL", "aM", "aN", "aO", "aP", "aQ", "aR", "aS", "aT", "aU", "aV", "aW", "aX", "aY", "aZ", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a0", "a!", "a@", "a#", "a$", "a%", "a^", "a&", "a*", "a(", "a)", "a-", "a_", "a=", "a+", "a[", "a]", "a{", "a}", "a|", "a;", "a:", "a'", "a\"", "a,", "a.", "a/", "a<", "a>", "a?", "a\\", "ba", "bb", "bc", "bd", "be", "bf", "bg", "bh", "bi", "bj", "bk", "bl", "bm", "bn", "bo", "bp", "bq", "br", "bs", "bt", "bu", "bv", "bw", "bx", "by", "bz", "bA", "bB", "bC", "bD", "bE", "bF", "bG", "bH", "bI", "bJ", "bK", "bL", "bM", "bN", "bO", "bP", "bQ", "bR", "bS", "bT", "bU", "bV", "bW", "bX", "bY", "bZ", "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b0", "b!", "b@", "b#", "b$", "b%", "b^", "b&", "b*", "b(", "b)", "b-", "b_", "b=", "b+", "b[", "b]", "b{", "b}", "b|", "b;", "b:", "b'", "b\"", "b,", "b.", "b/", "b<", "b>", "b?", "b\\", "ca", "cb", "cc", "cd", "ce", "cf", "cg", "ch", "ci", "cj", "ck", "cl", "cm", "cn", "co", "cp", "cq", "cr", "cs", "ct", "cu", "cv", "cw", "cx", "cy", "cz", "cA", "cB", "cC", "cD", "cE", "cF", "cG", "cH", "cI", "cJ", "cK", "cL", "cM", "cN", "cO", "cP", "cQ", "cR", "cS", "cT", "cU", "cV", "cW", "cX", "cY", "cZ", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c0", "c!", "c@", "c#", "c$", "c%", "c^", "c&", "c*", "c(", "c)", "c-", "c_", "c=", "c+", "c[", "c]", "c{", "c}", "c|", "c;", "c:", "c'", "c\"", "c,", "c.", "c/", "c<", "c>", "c?", "c\\", "da", "db", "dc", "dd", "de", "df", "dg", "dh", "di", "dj", "dk", "dl", "dm", "dn", "do", "dp", "dq", "dr", "ds", "dt", "du", "dv", "dw", "dx", "dy", "dz", "dA", "dB", "dC", "dD", "dE", "dF", "dG", "dH", "dI", "dJ", "dK", "dL", "dM", "dN", "dO", "dP", "dQ", "dR", "dS", "dT", "dU", "dV", "dW", "dX", "dY", "dZ", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d0", "d!", "d@", "d#", "d$", "d%", "d^", "d&", "d*", "d(", "d)", "d-", "d_", "d=", "d+", "d[", "d]", "d{", "d}", "d|", "d;", "d:", "d'", "d\"", "d,", "d.", "d/", "d<", "d>", "d?", "d\\", "ea", "eb", "ec", "ed", "ee", "ef", "eg", "eh", "ei", "ej", "ek", "el", "em", "en", "eo", "ep", "eq", "er", "es", "et", "eu", "ev", "ew", "ex", "ey", "ez", "eA", "eB", "eC", "eD", "eE", "eF", "eG", "eH", "eI", "eJ", "eK", "eL", "eM", "eN", "eO", "eP", "eQ", "eR", "eS", "eT", "eU", "eV", "eW", "eX", "eY", "eZ", "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e0", "e!", "e@", "e#", "e$", "e%", "e^", "e&", "e*", "e(", "e)", "e-", "e_", "e=", "e+", "e[", "e]", "e{", "e}", "e|", "e;", "e:", "e'", "e\"", "e,", "e.", "e/", "e<", "e>", "e?", "e\\", "fa", "fb", "fc", "fd", "fe", "ff", "fg", "fh", "fi", "fj", "fk", "fl", "fm", "fn", "fo", "fp", "fq", "fr", "fs", "ft", "fu", "fv", "fw", "fx", "fy", "fz", "fA", "fB", "fC", "fD", "fE", "fF", "fG", "fH", "fI", "fJ", "fK", "fL", "fM", "fN", "fO", "fP", "fQ", "fR", "fS", "fT", "fU", "fV", "fW", "fX", "fY", "fZ", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f0", "f!", "f@", "f#", "f$", "f%", "f^", "f&", "f*", "f(", "f)", "f-", "f_", "f=", "f+", "f[", "f]", "f{", "f}", "f|", "f;", "f:", "f'", "f\"", "f,", "f.", "f/", "f<", "f>", "f?", "f\\", "ga", "gb", "gc", "gd", "ge", "gf", "gg", "gh", "gi", "gj", "gk", "gl", "gm", "gn", "go", "gp", "gq", "gr", "gs", "gt", "gu", "gv", "gw", "gx", "gy", "gz", "gA", "gB", "gC", "gD", "gE", "gF", "gG", "gH", "gI", "gJ", "gK", "gL", "gM", "gN", "gO", "gP", "gQ", "gR", "gS", "gT", "gU", "gV", "gW", "gX", "gY", "gZ", "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g0", "g!", "g@", "g#", "g$", "g%", "g^", "g&", "g*", "g(", "g)", "g-", "g_", "g=", "g+", "g[", "g]", "g{", "g}", "g|", "g;", "g:", "g'", "g\"", "g,", "g.", "g/", "g<", "g>", "g?", "g\\", "ha", "hb", "hc", "hd", "he", "hf", "hg", "hh", "hi", "hj", "hk", "hl", "hm", "hn", "ho", "hp", "hq", "hr", "hs", "ht", "hu", "hv", "hw", "hx", "hy", "hz", "hA", "hB", "hC", "hD", "hE", "hF", "hG", "hH", "hI", "hJ", "hK", "hL", "hM", "hN", "hO", "hP", "hQ", "hR", "hS", "hT", "hU", "hV", "hW", "hX", "hY", "hZ", "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h0", "h!", "h@", "h#", "h$", "h%", "h^", "h&", "h*", "h(", "h)", "h-", "h_", "h=", "h+", "h[", "h]", "h{", "h}", "h|", "h;", "h:", "h'", "h\"", "h,", "h.", "h/", "h<", "h>", "h?", "h\\", "ia", "ib", "ic", "id", "ie", "if", "ig", "ih", "ii", "ij", "ik", "il", "im", "in", "io", "ip", "iq", "ir", "is", "it", "iu", "iv", "iw", "ix", "iy", "iz", "iA", "iB", "iC", "iD", "iE", "iF", "iG", "iH", "iI", "iJ", "iK", "iL", "iM", "iN", "iO", "iP", "iQ", "iR", "iS", "iT", "iU", "iV", "iW", "iX", "iY", "iZ", "i1", "i2", "i3", "i4", "i5", "i6", "i7", "i8", "i9", "i0", "i!", "i@", "i#", "i$", "i%", "i^", "i&", "i*", "i(", "i)", "i-", "i_", "i=", "i+", "i[", "i]", "i{", "i}", "i|", "i;", "i:", "i'", "i\"", "i,", "i.", "i/", "i<", "i>", "i?", "i\\", "ja", "jb", "jc", "jd", "je", "jf", "jg", "jh", "ji", "jj", "jk", "jl", "jm", "jn", "jo", "jp", "jq", "jr", "js", "jt", "ju", "jv", "jw", "jx", "jy", "jz", "jA", "jB", "jC", "jD", "jE", "jF", "jG", "jH", "jI", "jJ", "jK", "jL", "jM", "jN", "jO", "jP", "jQ", "jR", "jS", "jT", "jU", "jV", "jW", "jX", "jY", "jZ", "j1", "j2", "j3", "j4", "j5", "j6", "j7", "j8", "j9", "j0", "j!", "j@", "j#", "j$", "j%", "j^", "j&", "j*", "j(", "j)", "j-", "j_", "j=", "j+", "j[", "j]", "j{", "j}", "j|", "j;", "j:", "j'", "j\"", "j,", "j.", "j/", "j<", "j>", "j?", "j\\"]}
        ), 200

@app.route("/password-return/", methods=['POST'])
def passwordReturn():
    data = request.get_json()
    print(data)
    if data.get("packetInfo", {}).get("successful") == "True":
        return jsonify({"response": "Success"}), 200
    else:
        return jsonify({"response": "Failed"}), 400

if __name__ == '__main__':
    app.run(port=443)
