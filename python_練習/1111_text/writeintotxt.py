s = '   ABC 12\n\
    DEF 23\n\
    GHI 34\n\
    PQO 45\n\
    RST 56\n\
    abc 21\n\
    def 32\n\
    ghi 43\n\
    pqo 54\n\
    rst 65\n'
with open('mcuedutw.txt','wt',encoding='utf-8') as fout:
    print(s,file=fout)
    #fout.write(s)
print("資料已寫入 mcuedutw.txt")