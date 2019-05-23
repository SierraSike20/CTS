a =
b =
c =
if a == 1:
    def CTSone(a, b, c):
     # ("aCTSone"x + "bCTSone")^2 - cCTSone
        aCTSone = 1
        bCTSone = b / 2
        cCTSone = (-(bCTSone**2)) + c

     #strings
        aCTSonestr = str(aCTSone)
        bCTSonestr = str(bCTSone)
        cCTSonestr = str(cCTSone)

     #therfore
        return CTSone == ("(x" + bCTSonestr + ")^2" + cCTSonestr)

     #stringspec
        bCTSonecoordstr = str(-bCTSone)

     #turning points
        print("(" + bCTSonecoordstr + "," + cCTSonestr + ")")

else:
    def CTSother(a, b, c):
        # outerCTSother("aCTSother"x + "bCTSother" )^2 + "cCTSother"
        CTSouter = a
        aCTSother = 1
        bCTS = b / a
        cCTSother = ((-(bCTSother ** 2)) * outerCTSother) + c

        # strings
        CTSouter_str = str(CTSouter)
        aCTSother_str = str(aCTSother)
        bCTSother_str = str(bCTSother)
        cCTSother_str = str(cCTSother)

        # stringspec
        xvalueother = str(-bCTSother)

        # CTS
        return CTSother == CTSouter_str + "(x" + bCTSouter_str + ")^2" + cCTSother_str

        # turning points
        print("(" + xvalueother + "," + cCTSother + ")")