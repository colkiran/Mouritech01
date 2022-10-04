
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):
            import emojis

            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojis.decode(emojized))


            print(emojized)
        return innerMostFun

    return innerFun


engGrt = outerFun("Welcome")

etiger = engGrt("lion")

etiger("Prabhakar")





"""
engGrt = outerFun("Welcome")
hdnGrt = outerFun("Namaskar")
tmlGrt = outerFun("Vanakam")

esngArw = engGrt("----->")
edblArw = engGrt("=====>>")
estrArw = engGrt("******>")
tdblArw = tmlGrt("=====>>")


esngArw("Kholi")
tdblArw("Dhoni")

"""