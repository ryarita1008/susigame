
import random

print("一緒にお皿の色を覚えましょう！")
print("選択肢｛オレンジ、緑、水色、紫、金黒、赤、金、柄｝")

orange = ["玉子","生げそ","げそ梅","げそマヨ","炙りげそ","なすの浅漬け","いなり寿し","マヨコーン","ツナマヨ","軍艦納豆","きゅうり細巻","梅細巻","しんこ細巻"]
green = ["びんとろ","えび","いか","甘えび","だし巻玉子","揚げなす","げそ天にぎり","とびこ","ねぎまぐろ","山かけまぐろ","ツナきゅうり細巻"]
rightblue = ["まぐろ","江戸前風漬けまぐろ","サーモン","サーモンマヨ","炙りサーモン","生たこ","ヤリイカ","つぶ貝","えんがわ","塩炙りえんがわ","キス天にぎり","えび天にぎり"]
purple = ["とろサーモン","塩炙りとろサーモン","炙り土佐ネーズ・サーモン","炙りまぐろ","まぐろのカルパッチョ","サーモンのカルパッチョ","まぐろ細巻","サバの押寿し"]
blackgold = ["鯛","塩炙り鯛","あじ","はまち","塩炙りはまち","江戸前風漬けはまち","赤えび","炙り赤えび","鰹の塩たたき","いくら","揚げねぎまぐろ","えび三種","うなぎの手巻き"]
red = ["かんぱち","ホタテ","炙りホタテ","牛タン","サーモン三種"]
gold = ["シャコ","本鮪中とろ","塩炙り本鮪中とろ","数の子","煮穴子姿にぎり","うに","軍艦三種","穴子天にぎり"]
other = ["本鮪大とろ","塩炙り本鮪大とろ","江戸前風漬け大とろ","カニ","炙り牛ロース","炙りうなぎ","こぼれいくら"]

dish = ["オレンジ","緑","水色","紫","黒金","赤","金","花柄"]
dict = {"オレンジ":orange,"緑":green,"水色":rightblue,"紫":purple,"黒金":blackgold,"赤":red,"金":gold,"花柄":other}

menu = orange + green + rightblue + purple + blackgold + red + gold + other
quiz = random.choice(menu)

print(quiz)


def hantei(a):
    if ans == dish[a]:
        print("正解です。")
        return 1
    else:
        print("不正解です。")
        return 0

flag = 0
while flag == 0:
    ans = input()
    if quiz in dict["オレンジ"]:
        result = hantei(0)
        if result == 1:
            flag = 1
    if quiz in dict["緑"]:
        result = hantei(1)
        if result == 1:
            flag = 1
    if quiz in dict["水色"]:
        result = hantei(2)
        if result == 1:
            flag = 1
    if quiz in dict["紫"]:
        result = hantei(3)
        if result == 1:
            flag = 1
    if quiz in dict["黒金"]:
        result = hantei(4)
        if result == 1:
            flag = 1
    if quiz in dict["赤"]:
        result = hantei(5)
        if result == 1:
            flag = 1
    if quiz in dict["金"]:
        result = hantei(6)
        if result == 1:
            flag = 1
    if quiz in dict["花柄"]:
        result = hantei(7)
        if result == 1:
            flag = 1