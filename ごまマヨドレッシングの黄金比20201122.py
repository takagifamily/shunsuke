print("★ ★ ★ ★ ★ ごまマヨドレッシング調味料比率プログラム ★ ★ ★ ★ ★")
print("調味料を数字で選択してください!")
choumiryou = int(input("1:マヨネーズ,2:白すりごま,3:醤油,4:砂糖:"))

#　マヨネーズを選択
if choumiryou == 1:
    print("マヨネーズを入れましょう")
    print("大さじ・小さじを選択してください")
    spoon = int(input("1:大さじ、2:小さじ"))
    if spoon == 1:
        mayo  = int(input("マヨネーズは、大さじでいくら入れますか？数字を入れてください"))
        goma  = mayo * 3/5
        shoyu = mayo * 1/5
        sato  = round(((mayo) * (1/5)) / 3,2,)
        print("＜＜マヨネーズ：大さじ",mayo,"／白すりごま：大さじ",goma,"／醤油：大さじ",shoyu,"／砂糖：大さじ",sato,"です＞＞")
    elif spoon == 2:
        mayo  = int(input("マヨネーズは、小さじでいくら入れますか？数字を入れてください"))
        goma  = mayo * 3/5
        shoyu = (mayo * 1/5) 
        sato  = round((mayo) * (1/15),2) 
        print("＜＜マヨネーズ：小さじ",mayo,"／白すりごま：小さじ",goma,"／醤油：小さじ",shoyu,"／砂糖：小さじ",sato,"です＞＞")
    else:
        print("もう一度入力してください")

#　白すりごまを選択
elif choumiryou == 2:
    print("白すりごまを入れましょう")
    print("大さじ・小さじを選択してください")
    spoon = int(input("1:大さじ、2:小さじ"))
    if spoon == 1:
        goma  = int(input("白すりごまは、大さじでいくら入れますか？数字を入れてください"))
        mayo  = goma * 5/3
        shoyu = goma * 1/3
        sato  = round((goma) * (1/9),2)
        print("＜＜マヨネーズ：大さじ",mayo,"／白すりごま：大さじ",goma,"／醤油：大さじ",shoyu,"／砂糖：大さじ",sato,"です＞＞")
    elif spoon == 2:
        goma  = int(input("白すりごまは、小さじでいくら入れますか？数字を入れてください"))
        mayo  = goma * 5/3
        shoyu = goma * 1/3
        sato  = round((goma) * (1/9),2)
        print("＜＜マヨネーズ：小さじ",mayo,"／白すりごま：小さじ",goma,"／醤油：小さじ",shoyu,"／砂糖：小さじ",sato,"です＞＞")
    else:
        print("もう一度入力してください")

#　醤油を選択
elif choumiryou == 3:
    print("醤油を入れましょう")
    print("大さじ・小さじを選択してください")
    spoon = int(input("1:大さじ、2:小さじ"))
    if spoon == 1:
        shoyu = int(input("醤油は、大さじでいくら入れますか？数字を入れてください"))
        mayo  = shoyu * 5
        goma  = shoyu * 3
        sato  = round((shoyu) * (1/3),2)
        print("＜＜マヨネーズ：大さじ",mayo,"／白すりごま：大さじ",goma,"／醤油：大さじ",shoyu,"／砂糖：大さじ",sato,"です＞＞")
    elif spoon == 2:
        shoyu = int(input("醤油は、小さじでいくら入れますか？数字を入れてください"))
        mayo  = shoyu * 5
        goma  = shoyu * 3
        sato  = round((shoyu) * (1/3),2)
        print("＜＜マヨネーズ：小さじ",mayo,"／白すりごま：小さじ",goma,"／醤油：小さじ",shoyu,"／砂糖：小さじ",sato,"です＞＞")
    else:
        print("もう一度入力してください")

#　砂糖を選択
elif choumiryou == 4:
    print("砂糖を入れましょう")
    print("大さじ・小さじを選択してください")
    spoon = int(input("1:大さじ、2:小さじ"))
    if spoon == 1:
        sato  = int(input("砂糖は、大さじでいくら入れますか？数字を入れてください"))
        mayo  = sato * 15
        goma  = sato * 9
        shoyu = sato * 3
        print("＜＜マヨネーズ：大さじ",mayo,"／白すりごま：大さじ",goma,"／醤油：大さじ",shoyu,"／砂糖：大さじ",sato,"です＞＞")
    elif spoon == 2:
        sato  = int(input("砂糖は、小さじでいくら入れますか？数字を入れてください"))
        mayo  = sato * 15
        goma  = sato * 9
        shoyu = sato * 3
        print("＜＜マヨネーズ：小さじ",mayo,"／白すりごま：小さじ",goma,"／醤油：小さじ",shoyu,"／砂糖：小さじ",sato,"です＞＞")
    else:
        print("もう一度入力してください")

#　マヨネーズ、白すりごま、醤油、砂糖以外を選択
else:
    print("もう入力し直してください")