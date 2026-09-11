with open('C:\semestr1\seminar2\input.txt', encoding='utf-8') as f:
    for st in f.readlines():
        st = ' ' + st
        gl = {'а':'а', 'о':'о', 'е':'э',  'э':'э',  'у':'у',  'ы':'ы',  'я':'а',  'ё':'о',  'и':'и'}
        ans = st[0]
        for i in range(1, len(st)):
            if st[i] in gl and (st[i-1] not in gl and st[i-1] != ' '):
                ans += st[i]
                ans += 'с'
            ans += st[i]
        print(ans)