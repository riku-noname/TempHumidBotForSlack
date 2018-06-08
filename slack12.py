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
        slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
        slack.notify(text="あおらbotです．\n\n現在のKC104の温度，湿度に関して報告致します．\n\n-----\n時間 : 12時\n温度 : " + str(int(temp)) + " ℃\n湿度 : " + str(int(humid)) + "％\n-----\n\n以上です．")
