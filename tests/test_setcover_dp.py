from src.setcover import SetCover

def assert_test(req_skills, people):
    print("people arr length = " + str(len(people)))
    sc = SetCover()
    received_dp = sc.find_smallest_team_dp(req_skills, people)
    received = sc.find_smallest_team(req_skills, people)
    assert len(received_dp) == len(received)
    req_skills_set = set(req_skills)
    for ri in received_dp:
        for sk in people[ri]:
            if sk in req_skills_set:
                req_skills_set.remove(sk)
    
    assert len(req_skills_set) == 0

def test1():
    req_skills = ["java","nodejs","reactjs"]
    people = [["java"],["nodejs"],["nodejs","reactjs"]]
    assert_test(req_skills, people)

def test2():
    req_skills = ["algorithms","math","java","reactjs","csharp","aws"]
    people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
    assert_test(req_skills, people)

def test3():
    req_skills = ["uhppib","mgdipkgt","vaostwmycy","bjwxnfbbubpnd"]
    people = [["vaostwmycy"],["mgdipkgt"],["bjwxnfbbubpnd"],[],["uhppib"]]
    assert_test(req_skills, people)

def test4():
    req_skills = ["hdbxcuzyzhliwv","uvwlzkmzgis","sdi","bztg","ylopoifzkacuwp","dzsgleocfpl"]
    people =[["hdbxcuzyzhliwv","dzsgleocfpl"],["hdbxcuzyzhliwv","sdi","ylopoifzkacuwp","dzsgleocfpl"],["bztg","ylopoifzkacuwp"],["bztg","dzsgleocfpl"],["hdbxcuzyzhliwv","bztg"],["dzsgleocfpl"],["uvwlzkmzgis"],["dzsgleocfpl"],["hdbxcuzyzhliwv"],[],["dzsgleocfpl"],["hdbxcuzyzhliwv"],[],["hdbxcuzyzhliwv","ylopoifzkacuwp"],["sdi"],["bztg","dzsgleocfpl"],["hdbxcuzyzhliwv","uvwlzkmzgis","sdi","bztg","ylopoifzkacuwp"],["hdbxcuzyzhliwv","sdi"],["hdbxcuzyzhliwv","ylopoifzkacuwp"],["sdi","bztg","ylopoifzkacuwp","dzsgleocfpl"],["dzsgleocfpl"],["sdi","ylopoifzkacuwp"],["hdbxcuzyzhliwv","uvwlzkmzgis","sdi"],[],[],["ylopoifzkacuwp"],[],["sdi","bztg"],["bztg","dzsgleocfpl"],["sdi","bztg"]]
    assert_test(req_skills, people)   

def test5():
    req_skills = ["mwobudvo","goczubcwnfze","yspbsez","pf","ey","hkq"]
    people =[
    [],
    ["mwobudvo"],
    ["hkq"],
    ["pf"],
    ["pf"],
    ["mwobudvo","pf"],
    [],
    ["yspbsez"],
    [],
    ["hkq"],
    [],
    [],
    ["goczubcwnfze","pf","hkq"], #12
    ["goczubcwnfze"],
    ["hkq"],
    ["mwobudvo"],
    [],
    ["mwobudvo","pf"],
    ["pf","ey"], #18
    ["mwobudvo"],
    ["hkq"],
    [],
    ["pf"],
    ["mwobudvo","yspbsez"], #23
    ["mwobudvo","goczubcwnfze"], #24
    ["goczubcwnfze","pf"],
    ["goczubcwnfze"],
    ["goczubcwnfze"],
    ["mwobudvo"],
    ["mwobudvo","goczubcwnfze"],
    [],
    ["goczubcwnfze"],
    [],
    ["goczubcwnfze"],
    ["mwobudvo"],
    [],
    ["hkq"],
    ["yspbsez"],
    ["mwobudvo"],
    ["goczubcwnfze","ey"] #39
    ]
    assert_test(req_skills, people)  

def test6():
    req_skills = ["mli","krvswogyyanvwhd","jzuhxeqqvkuac","gmwyepsq","nfgilvs","zyqubsiify","pbmmtjcruigt"]
    people =[["pbmmtjcruigt"],["jzuhxeqqvkuac","zyqubsiify","pbmmtjcruigt"],["krvswogyyanvwhd"],[],["mli","krvswogyyanvwhd","pbmmtjcruigt"],[],["mli","pbmmtjcruigt"],[],["mli","pbmmtjcruigt"],["pbmmtjcruigt"],["krvswogyyanvwhd","gmwyepsq","nfgilvs"],["mli"],["krvswogyyanvwhd","jzuhxeqqvkuac","gmwyepsq"],["jzuhxeqqvkuac","pbmmtjcruigt"],[],[],[],["zyqubsiify"],["krvswogyyanvwhd","pbmmtjcruigt"],["krvswogyyanvwhd","jzuhxeqqvkuac","nfgilvs"],[],["krvswogyyanvwhd"],["zyqubsiify"],["mli","krvswogyyanvwhd","jzuhxeqqvkuac"],["pbmmtjcruigt"],["pbmmtjcruigt"],["zyqubsiify"],["mli","nfgilvs"],["mli","jzuhxeqqvkuac","zyqubsiify"],["mli","pbmmtjcruigt"],["mli"],["mli","jzuhxeqqvkuac"],["mli","jzuhxeqqvkuac","pbmmtjcruigt"],["jzuhxeqqvkuac"],["mli"],["mli"],["mli"],[],["krvswogyyanvwhd","pbmmtjcruigt"],[],["jzuhxeqqvkuac"],[],["mli"],["jzuhxeqqvkuac"],["jzuhxeqqvkuac","zyqubsiify","pbmmtjcruigt"],["mli","zyqubsiify"],["mli"],["mli","zyqubsiify"],["krvswogyyanvwhd"],[],["jzuhxeqqvkuac"],[],["zyqubsiify"],[],["krvswogyyanvwhd","gmwyepsq","zyqubsiify"],["krvswogyyanvwhd","zyqubsiify"],["krvswogyyanvwhd","pbmmtjcruigt"],["mli"],["mli","zyqubsiify"],[]]
    assert_test(req_skills, people)

def test7():
    req_skills = ["gkgtfxpvxnxlbhxu","baayobms","yomqrposuurmvisx","vsftojpcp","pjovtkytubbouq","hlmvucyi","chpzrslbtd","uighcqpiteg"]
    people =[["pjovtkytubbouq"],["baayobms"],["baayobms","pjovtkytubbouq"],["chpzrslbtd"],[],["yomqrposuurmvisx"],["uighcqpiteg"],[],["gkgtfxpvxnxlbhxu","yomqrposuurmvisx","uighcqpiteg"],[],["pjovtkytubbouq","uighcqpiteg"],["yomqrposuurmvisx"],[],[],[],["pjovtkytubbouq"],["gkgtfxpvxnxlbhxu","yomqrposuurmvisx","pjovtkytubbouq","uighcqpiteg"],["yomqrposuurmvisx","pjovtkytubbouq"],["chpzrslbtd"],["pjovtkytubbouq"],[],[],["baayobms"],["yomqrposuurmvisx","chpzrslbtd"],["yomqrposuurmvisx","pjovtkytubbouq"],["pjovtkytubbouq"],[],["yomqrposuurmvisx"],[],["yomqrposuurmvisx","pjovtkytubbouq"],[],[],[],["yomqrposuurmvisx"],[],["pjovtkytubbouq"],[],[],[],["vsftojpcp"],[],["yomqrposuurmvisx","pjovtkytubbouq"],[],[],["gkgtfxpvxnxlbhxu"],["yomqrposuurmvisx"],["pjovtkytubbouq","chpzrslbtd"],["uighcqpiteg"],["pjovtkytubbouq"],["yomqrposuurmvisx","pjovtkytubbouq","uighcqpiteg"],[],["pjovtkytubbouq"],[],["chpzrslbtd"],["hlmvucyi"],["yomqrposuurmvisx","pjovtkytubbouq"],["pjovtkytubbouq"],[],["yomqrposuurmvisx"],[]]
    assert_test(req_skills, people)        

def test8():
    req_skills = ["wav","hobqgx","euhrjnpudcvbsjj","cwhunthtwmjfqtz","eqjruombtk","kvpyhqsgoskh","vpntuztaexauy","xyhh","wtvehl"]
    people =[["eqjruombtk"],["euhrjnpudcvbsjj","kvpyhqsgoskh"],["wav","eqjruombtk","kvpyhqsgoskh"],[],["cwhunthtwmjfqtz"],[],["cwhunthtwmjfqtz"],["cwhunthtwmjfqtz"],["euhrjnpudcvbsjj"],["wav","euhrjnpudcvbsjj","wtvehl"],["eqjruombtk"],[],["vpntuztaexauy"],[],["hobqgx","euhrjnpudcvbsjj","vpntuztaexauy","xyhh"],["wav","eqjruombtk","kvpyhqsgoskh"],["wav","euhrjnpudcvbsjj"],["wav","kvpyhqsgoskh"],["kvpyhqsgoskh"],[],["wtvehl"],["cwhunthtwmjfqtz","kvpyhqsgoskh"],["euhrjnpudcvbsjj","kvpyhqsgoskh"],["cwhunthtwmjfqtz","kvpyhqsgoskh"],["euhrjnpudcvbsjj","cwhunthtwmjfqtz","eqjruombtk"],["wav","hobqgx","cwhunthtwmjfqtz","vpntuztaexauy"],["wav","cwhunthtwmjfqtz"],["wav","hobqgx"],["hobqgx","kvpyhqsgoskh","wtvehl"],["euhrjnpudcvbsjj","kvpyhqsgoskh"],["euhrjnpudcvbsjj"],["vpntuztaexauy"],["euhrjnpudcvbsjj"],["euhrjnpudcvbsjj","cwhunthtwmjfqtz"],["wav"],[],["wav"],["euhrjnpudcvbsjj"],[],["euhrjnpudcvbsjj"]]
    assert_test(req_skills, people)

def test9():
    req_skills = ["jzjgkjymmlsv","ryeqispun","pgbxnmcqj","gurg","xweykqj","paiutrvmzg","lmdghrdhqr","dvkplbbs","sxx"]
    people =[["gurg","dvkplbbs"],["xweykqj"],["jzjgkjymmlsv","ryeqispun","gurg","lmdghrdhqr","sxx"],["ryeqispun","gurg"],["ryeqispun","lmdghrdhqr"],[],["xweykqj"],[],["gurg"],["ryeqispun","gurg","lmdghrdhqr"],["ryeqispun"],["gurg","lmdghrdhqr"],[],["ryeqispun","gurg","lmdghrdhqr"],[],["pgbxnmcqj","gurg","sxx"],["lmdghrdhqr"],["gurg"],["ryeqispun"],["xweykqj","sxx"],[],["jzjgkjymmlsv","dvkplbbs"],["ryeqispun"],["ryeqispun","paiutrvmzg","dvkplbbs"],[],["sxx"],[],["jzjgkjymmlsv","xweykqj"],["xweykqj"],["gurg","dvkplbbs"],["lmdghrdhqr","sxx"],["gurg","lmdghrdhqr","dvkplbbs","sxx"],["gurg"],["xweykqj"],[],[],[],["jzjgkjymmlsv"],["ryeqispun"],["xweykqj","lmdghrdhqr"],["xweykqj"],["paiutrvmzg"],[],["jzjgkjymmlsv","gurg"],["gurg","paiutrvmzg","dvkplbbs"],["gurg"],["lmdghrdhqr"],[],[],["ryeqispun","sxx"]]
    assert_test(req_skills, people)

def test10():
    req_skills = ["vgzp","urfys","nvkjkzxrfn","pqznypwpcv","bdfmsjlddbinqo","xvgkyzqpmzwcxol","twlau","vybgxpyq","edpuw","w"]
    people =[["xvgkyzqpmzwcxol"],["w"],["urfys","w"],["urfys"],["bdfmsjlddbinqo"],["xvgkyzqpmzwcxol"],[],[],["w"],["vgzp","w"],["nvkjkzxrfn","bdfmsjlddbinqo","edpuw"],["urfys"],["bdfmsjlddbinqo","xvgkyzqpmzwcxol","twlau"],["nvkjkzxrfn","bdfmsjlddbinqo","vybgxpyq"],["vgzp","edpuw"],["urfys","xvgkyzqpmzwcxol"],["bdfmsjlddbinqo","w"],["nvkjkzxrfn","bdfmsjlddbinqo","w"],["bdfmsjlddbinqo","vybgxpyq"],["urfys","bdfmsjlddbinqo"],["vgzp"],["nvkjkzxrfn","xvgkyzqpmzwcxol"],["nvkjkzxrfn"],["vgzp","edpuw"],[],["bdfmsjlddbinqo"],["vgzp","nvkjkzxrfn","xvgkyzqpmzwcxol"],["vgzp","bdfmsjlddbinqo","edpuw","w"],["xvgkyzqpmzwcxol","vybgxpyq","w"],["pqznypwpcv","vybgxpyq"],["vybgxpyq"],["twlau"],["vgzp"],["vgzp","twlau","edpuw"],["nvkjkzxrfn","bdfmsjlddbinqo"],["bdfmsjlddbinqo"],["vgzp"],["urfys"],["nvkjkzxrfn"],["nvkjkzxrfn","edpuw"],["vgzp","nvkjkzxrfn"],[],["vgzp","nvkjkzxrfn"],["xvgkyzqpmzwcxol"],[],["nvkjkzxrfn","xvgkyzqpmzwcxol","vybgxpyq"],["vybgxpyq"],["nvkjkzxrfn"],["nvkjkzxrfn","edpuw"],["vgzp"]]
    assert_test(req_skills, people) 

def test11():
    req_skills = ["vgzp","urfys","nvkjkzxrfn","pqznypwpcv","bdfmsjlddbinqo","xvgkyzqpmzwcxol","twlau","vybgxpyq","edpuw","w"]
    people =[["xvgkyzqpmzwcxol"],["w"],["urfys","w"],["urfys"],["bdfmsjlddbinqo"],["xvgkyzqpmzwcxol"],[],[],["w"],["vgzp","w"],["nvkjkzxrfn","bdfmsjlddbinqo","edpuw"],["urfys"],["bdfmsjlddbinqo","xvgkyzqpmzwcxol","twlau"],["nvkjkzxrfn","bdfmsjlddbinqo","vybgxpyq"],["vgzp","edpuw"],["urfys","xvgkyzqpmzwcxol"],["bdfmsjlddbinqo","w"],["nvkjkzxrfn","bdfmsjlddbinqo","w"],["bdfmsjlddbinqo","vybgxpyq"],["urfys","bdfmsjlddbinqo"],["vgzp"],["nvkjkzxrfn","xvgkyzqpmzwcxol"],["nvkjkzxrfn"],["vgzp","edpuw"],[],["bdfmsjlddbinqo"],["vgzp","nvkjkzxrfn","xvgkyzqpmzwcxol"],["vgzp","bdfmsjlddbinqo","edpuw","w"],["xvgkyzqpmzwcxol","vybgxpyq","w"],["pqznypwpcv","vybgxpyq"],["vybgxpyq"],["twlau"],["vgzp"],["vgzp","twlau","edpuw"],["nvkjkzxrfn","bdfmsjlddbinqo"],["bdfmsjlddbinqo"],["vgzp"],["urfys"],["nvkjkzxrfn"],["nvkjkzxrfn","edpuw"],["vgzp","nvkjkzxrfn"],[],["vgzp","nvkjkzxrfn"],["xvgkyzqpmzwcxol"],[],["nvkjkzxrfn","xvgkyzqpmzwcxol","vybgxpyq"],["vybgxpyq"],["nvkjkzxrfn"],["nvkjkzxrfn","edpuw"],["vgzp"]]
    assert_test(req_skills, people)   

def test12():
    req_skills =["hfkbcrslcdjq","jmhobexvmmlyyzk","fjubadocdwaygs","peaqbonzgl","brgjopmm","x","mf","pcfpppaxsxtpixd","ccwfthnjt","xtadkauiqwravo","zezdb","a","rahimgtlopffbwdg","ulqocaijhezwfr","zshbwqdhx","hyxnrujrqykzhizm"]
    people =[["peaqbonzgl","xtadkauiqwravo"],["peaqbonzgl","pcfpppaxsxtpixd","zshbwqdhx"],["x","a"],["a"],["jmhobexvmmlyyzk","fjubadocdwaygs","xtadkauiqwravo","zshbwqdhx"],["fjubadocdwaygs","x","zshbwqdhx"],["x","xtadkauiqwravo"],["x","hyxnrujrqykzhizm"],["peaqbonzgl","x","pcfpppaxsxtpixd","a"],["peaqbonzgl","pcfpppaxsxtpixd"],["a"],["hyxnrujrqykzhizm"],["jmhobexvmmlyyzk"],["hfkbcrslcdjq","xtadkauiqwravo","a","zshbwqdhx"],["peaqbonzgl","mf","a","rahimgtlopffbwdg","zshbwqdhx"],["xtadkauiqwravo"],["fjubadocdwaygs"],["x","a","ulqocaijhezwfr","zshbwqdhx"],["peaqbonzgl"],["pcfpppaxsxtpixd","ulqocaijhezwfr","hyxnrujrqykzhizm"],["a","ulqocaijhezwfr","hyxnrujrqykzhizm"],["a","rahimgtlopffbwdg"],["zshbwqdhx"],["fjubadocdwaygs","peaqbonzgl","brgjopmm","x"],["hyxnrujrqykzhizm"],["jmhobexvmmlyyzk","a","ulqocaijhezwfr"],["peaqbonzgl","x","a","ulqocaijhezwfr","zshbwqdhx"],["mf","pcfpppaxsxtpixd"],["fjubadocdwaygs","ulqocaijhezwfr"],["fjubadocdwaygs","x","a"],["zezdb","hyxnrujrqykzhizm"],["ccwfthnjt","a"],["fjubadocdwaygs","zezdb","a"],[],["peaqbonzgl","ccwfthnjt","hyxnrujrqykzhizm"],["xtadkauiqwravo","hyxnrujrqykzhizm"],["peaqbonzgl","a"],["x","a","hyxnrujrqykzhizm"],["zshbwqdhx"],[],["fjubadocdwaygs","mf","pcfpppaxsxtpixd","zshbwqdhx"],["pcfpppaxsxtpixd","a","zshbwqdhx"],["peaqbonzgl"],["peaqbonzgl","x","ulqocaijhezwfr"],["ulqocaijhezwfr"],["x"],["fjubadocdwaygs","peaqbonzgl"],["fjubadocdwaygs","xtadkauiqwravo"],["pcfpppaxsxtpixd","zshbwqdhx"],["peaqbonzgl","brgjopmm","pcfpppaxsxtpixd","a"],["fjubadocdwaygs","x","mf","ulqocaijhezwfr"],["jmhobexvmmlyyzk","brgjopmm","rahimgtlopffbwdg","hyxnrujrqykzhizm"],["x","ccwfthnjt","hyxnrujrqykzhizm"],["hyxnrujrqykzhizm"],["peaqbonzgl","x","xtadkauiqwravo","ulqocaijhezwfr","hyxnrujrqykzhizm"],["brgjopmm","ulqocaijhezwfr","zshbwqdhx"],["peaqbonzgl","pcfpppaxsxtpixd"],["fjubadocdwaygs","x","a","zshbwqdhx"],["fjubadocdwaygs","peaqbonzgl","x"],["ccwfthnjt"]]
    assert_test(req_skills, people)

def test13():
    req_skills = ["algorithms","math","java"]
    people = [
        ["algorithms","math","java"],
        ["math"],
        ["java"],
        ["algorithms"]
        ]
    assert_test(req_skills, people)

def test14():
    req_skills = ["zp","jpphhnhwpw","pscleb","arn","acrsxqvus","fseqih","fpqbjbbxglivyonn","cjozlkyodt","mvtwffgkhjrtibto","kumdvfwsvrht","i","s","ucr","oo","yqkqkhhhwngyjrg","odiwidzqw"]
    people = [["acrsxqvus"],["zp"],[],["fpqbjbbxglivyonn"],[],[],["kumdvfwsvrht"],[],["oo"],[],["fseqih"],[],["arn"],[],[],["yqkqkhhhwngyjrg"],[],[],[],["kumdvfwsvrht"],["s"],[],[],["zp","ucr"],[],["pscleb"],[],[],[],[],[],[],[],["jpphhnhwpw"],[],[],[],["oo"],[],["i"],["pscleb"],[],[],[],[],[],[],["i"],[],["mvtwffgkhjrtibto","odiwidzqw"],[],["cjozlkyodt","odiwidzqw"],["arn"],[],[],["acrsxqvus"],[],[],[],["ucr"]]
    assert_test(req_skills, people)