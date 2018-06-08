#slackAPIの呼び出し
import slackweb

#メイン関数
if __name__ == '__main__':
    temp = 0
    humid = 0

    for line in open('data.txt','r'):
        data = line.split()
        temp += float(data[0])
        humid += float(data[1])

        #指定チャンネルへテキストの送信
        slack = slackweb.Slack(url="https://hooks.slack.com/services/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        slack.notify(text="あおらbotです．\n明日，5月7日（月）から温湿度の報告を再開させて頂きます．\n不具合等ございましたら，M1森本陸までご連絡下さい．よろしくお願い致します．")
